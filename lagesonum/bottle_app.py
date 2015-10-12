# coding: utf-8

import os
import datetime
import subprocess
from babel.dates import format_datetime
from babel.core import Locale, UnknownLocaleError
from beaker.middleware import SessionMiddleware

from bottle import default_app, route, view, static_file, TEMPLATE_PATH, request, BaseTemplate, hook, auth_basic, \
    response, redirect
from passlib.hash import sha256_crypt

from bottle_utils.i18n import I18NPlugin, i18n_path
from bottle_utils.i18n import lazy_gettext as _
from sqlalchemy import func, exists
from sqlalchemy.exc import IntegrityError

from input_number import is_valid_number, parse_numbers, get_fingerprint
from models import BaseModel, Number, Place, User
from configuration import LANGS, MIN_COUNT, MAX_DAYS, DEFAULT_LOCALE, DISPLAY_SIZE

# store database outside of repository so it is not overwritten by git pull
MOD_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(MOD_PATH, '../', '../', "lagesonr.db"))

model = BaseModel(database=DB_PATH)


def get_valid_locale(l):
    try:
        Locale.parse(l)
        return l
    except UnknownLocaleError:
        return DEFAULT_LOCALE

# set as global variable available in all templates (to be able to call e.g. request.locale)
BaseTemplate.defaults['request'] = request
BaseTemplate.defaults['locale_datetime'] = lambda d: format_datetime(d, format="short", locale=get_valid_locale(request.locale))
BaseTemplate.defaults['locale_translate'] = lambda s: [s.translate(l[2]) for l in LANGS if l[0] == get_valid_locale(request.locale)][0]


@hook('before_request')
def open_session():
    request['orm'] = model.create_session()


@hook('after_request')
def close_session():
    request['orm'].commit()
    request['orm'].close()


@hook('before_request')
def _check_locale():
    """ Determine locale from request if non set """
    if not request.environ.get('LOCALE'):
        accept_language = request.get_header('Accept-Language')
        if not accept_language:
            return

        accepted = []
        for language in accept_language.split(','):
            if language.split(';')[0] == language:
                accepted.append(language.strip())
            else:
                accepted.append(language.split(";")[0].strip())
        # fine tuning order of locale_q_pair according to q-value necessary?!

        lang = Locale.negotiate(accepted, [l[0] for l in LANGS])
        if lang:
            request.environ['LOCALE'] = str(lang)


@route('/')
def index():
    """landing page is page for querying numbers"""
    redirect(i18n_path('/query'))


@route('/enter')
@view('views/start_page', entered=[], nonunique=[], failed=[])
def enter():
    pass


@route('/enter', method='POST')
@view('views/start_page')
def do_enter():
    return enter_save()


def enter_save():
    """Enter numbers into database"""
    db = request['orm']
    numbers = set(parse_numbers(request.forms.get('numbers', '')))
    timestamp = datetime.datetime.now()

    usr_hash = get_fingerprint(request)

    result_num = []
    result_nonuniq = []
    result_failed = []

    # TODO make place variable, depending on current request
    q = db.query(Place).filter_by(name='LAGESO')
    lageso = q.one() if q.count() == 1 else None

    if not numbers:
        result_num.append(_('novalidnumbers'))
    else:
        authed_user = None
        s = request.environ.get('beaker.session')
        username, ignore = request.auth or (None, None)
        try:
            authed_user = db.query(User).filter_by(username=(s.get('user', username))).one() if s else None
        except Exception as e:
            pass

        for num in numbers:
            if is_valid_number(num):
                n = Number(number=num.upper(), timestamp=timestamp, place=lageso, fingerprint=usr_hash, user=authed_user)
                db.add(n)
                try:
                    db.commit()
                except IntegrityError:
                    db.rollback()
                    n = db.query(Number).filter_by(number=num.upper())
                    if (n.count() > 0):
                        result_nonuniq.append(n.first().number)
                    else:
                        result_failed.append(num)
                else:
                    result_num.append(n.number)
            else:
                result_failed.append(num)

    # FIXME result_num is horrible, as it contains success and failures, indistinguishable
    return {'entered': result_num, 'nonunique': result_nonuniq, 'failed': result_failed,
            'timestamp': timestamp}


@route('/query')
@view('views/query_page', result=None)
def query():
    pass


@route('/query', method='POST')
@view('views/query_page')
def do_query():
    """Search for numbers in database"""
    user_input = request.forms.get('number', '')
    numbers = parse_numbers(user_input)

    number = None
    timestamps = []
    invalid_input = None

    if numbers:
        # FIXME WTF? Allow and parse a list and than pick one & silently drop the others?
        number = numbers[0]
        qry = Number.select(Number.time).where(Number.number ** number).order_by(Number.time)
        timestamps = [n.time for n in qry]
    else:
        invalid_input = user_input

    context = {
        'result': number or invalid_input,
        'invalid_input': invalid_input,
        'timestamps': timestamps
    }

    return context


@route('/about')
@view('views/about')
def about():
    """Return page with information about this project"""
    pass


@route('/impressum')
@view('views/impressum')
def impressum():
    """Return page with contact information"""
    pass


@route('/static/<filename:path>', no_i18n=True)
def send_static(filename):
    return static_file(filename, root=os.path.join(MOD_PATH, 'static'))


@route('/favicon.ico', no_i18n=True)
def send_static():
    return static_file("favicon.png", root=os.path.join(MOD_PATH, 'static'))


# Numbers to be shown there:
# All numbers that have been entered 3 or more times and where the last time of entry is not older than X minutes.
# For the "last time of entry age" it would be great to collect stats how long numbers are displayed in average.
# Until the stats are actually being collected, we should use 15 minutes as an "inactive" time setting.
# There should also be a link "history" where those numbers are then listed with a note "last seen".
@route('/display')
@view('views/display')
def display():

    oldest_to_be_shown = datetime.datetime.combine(datetime.date.today() - datetime.timedelta(days=MAX_DAYS),
                                                   datetime.datetime.min.time())
    # TODO optimize query, so we don't need to iterate manually, e.g. by selecing only count > min_count!
    # TODO make Place variable and part of WHERE

    verified_numbers = request['orm'].query(Number.number, Number.timestamp, User.username).join(User).\
        filter(Number.timestamp >= oldest_to_be_shown).order_by(Number.timestamp.desc(), Number.number).all()
    numbers = request['orm'].query(Number.number, Number.timestamp, func.count(Number.number).label('count')).\
        filter(Number.timestamp >= oldest_to_be_shown).filter_by(user=None).group_by(Number.number).\
        order_by(Number.timestamp.desc(), Number.number).all()

    # filter numbers entered often enough
    # format numbers for later output
    verified_output = set([n.number for n in verified_numbers][:DISPLAY_SIZE])
    unverified_output = [{'num': n.number, 'count': int(n.count)}
                         for n in numbers if int(n.count) >= MIN_COUNT][:DISPLAY_SIZE]
    for n in unverified_output:
        if n['num'] in verified_output:
            verified_output.remove(n['num'])

    display_output = sorted([{'num': n, 'count': 1} for n in verified_output] + unverified_output,
                            key=lambda n: n['num'])

    since = format_datetime(oldest_to_be_shown, 'short', locale=get_valid_locale(request.locale))
    return {'numbers': display_output,
            'since': since,
            'min_count': MIN_COUNT
            }


@route('/pm-start')
@view('static/pm-start.html')
def press_release():
    pass


def check_username(username, password):
    user = None
    s = request.environ.get('beaker.session')
    if s:
        user = s.get('user', None)
    if not user or user != username:
        try:
            user = User.get(username=username)
            sha256_crypt.verify(password, user.password)
        except User.DoesNotExist:
            # print(u'No, not you: {}'.format(username))
            user = None
        except ValueError:
            # print(u'Wrong password')
            user = None
        finally:
            if user:
                s['user'] = user.username
            else:
                del(s['user'])
            s.save()
            s.persist()

    return user


@route('/authenticated')
@auth_basic(check_username, realm='Authenticated access', text='Please authenticate to enter')
@view('views/start_page_authed', entered=[], nonunique=[], failed=[])
def authenticated():
    pass


@route('/authenticated', method='POST')
@auth_basic(check_username, realm='Authenticated access', text='Please authenticate to enter')
@view('views/start_page_authed')
def do_authenticated():
    return enter_save()


@route('/version', no_i18n=True)
def show_version():
    git_status = subprocess.Popen(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], stdout=subprocess.PIPE,
                                  universal_newlines=True)
    (version, err) = git_status.communicate(timeout=5)
    response.content_type = 'text/plain'
    return u'{}'.format(version)


# findet templates im gleichen Verzeichnis
TEMPLATE_PATH.append(MOD_PATH)
app = default_app()
application = I18NPlugin(app, langs=LANGS, default_locale=DEFAULT_LOCALE,
                         domain='messages',
                         locale_dir=os.path.join(MOD_PATH, 'locales'))
session_opts = {
    'session.key': 'lagesonum_sess',
    'session.type': 'ext:database',
    'session.url': 'sqlite:///' + DB_PATH,
    'session.table_name': 'session_storage',
    'session.cookie_expires': 1800,
    'session.httponly': True,
}
application = SessionMiddleware(application, session_opts)
