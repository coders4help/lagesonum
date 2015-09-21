# coding: utf-8

import sqlite3
import os
import time

from bottle import default_app, route, view, static_file, TEMPLATE_PATH, request, BaseTemplate, debug
debug(True)

from bottle_utils.i18n import I18NPlugin
#from bottle_utils.i18n import lazy_gettext as _

from input_number import is_valid_number, parse_numbers, get_fingerprint
from dbhelper import initialize_database

MOD_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(MOD_PATH, '.', '.', "lagesonr.db"))

if not os.path.exists(DB_PATH):
    initialize_database(DB_PATH)

lagesonrdb = sqlite3.connect(DB_PATH)

# todo: populate list dynamically based on available/selected translations
LANGS = [
    ('de_DE', 'Deutsch'),
    ('en_US', 'English'),
]
# ('ar_AR', 'Arab'),
DEFAULT_LOCALE = 'en_US'

# set as global variable available in all templates (to be able to call e.g. request.locale)
BaseTemplate.defaults['request'] = request

# landing page is page for querying numbers
@route('/')
@view('views/query_page')
def index():

    context = {
        'result': 'NewNumber',
        'invalid_input': '',
        'timestamps': ''
    }

    return context


@route('/enter')
@view('views/start_page')
def enter():
    """: Helfer steht am LaGeSo und gibt Nummern ein [_____] """
    return {'entered': []}


@route('/enter', method='POST')
@view('views/start_page')
def do_enter():
    numbers = set(parse_numbers(request.forms.get('numbers', '')))
    timestamp = time.asctime()

    usr_hash = get_fingerprint(request)

    result_num = []

    with lagesonrdb as connection:
        cursor = connection.cursor()
        insert_query = 'INSERT INTO numbers (number, fingerprint, place, time) VALUES (?, ?, ?, ?)'

        for num in numbers:
            if is_valid_number(num):
                values = (num.capitalize(), usr_hash, 'LAGESO', timestamp)
                try:
                    cursor.execute(insert_query, values)
                    result_num.append(num)
                except sqlite3.IntegrityError:
                    result_num.append("ALREADY KNOWN: {}".format(num))
            else:
                result_num.append("INVALID INPUT: {}".format(num))

        if not len(numbers):
            result_num.append("NO VALID NUMBERS ENTERED")

    return {'entered': result_num, 'timestamp': timestamp}


@route('/query')
@view('views/query_page')
def query():
    return {'result': None}


@route('/query', method='POST')
@view('views/query_page')
def do_query():
    user_input = request.forms.get('number', '')
    numbers = parse_numbers(user_input)

    number = None
    rowcount = 0
    timestamps = []
    invalid_input = None

    if numbers:
        number = numbers[0]
        with lagesonrdb as connection:
            cursor = connection.cursor()

            select_query = 'SELECT time FROM numbers WHERE number LIKE ? ORDER BY time'
            values = (number,)

            result = cursor.execute(select_query, values).fetchall()
            timestamps = [row[0] for row in result]
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
    pass


@route('/impressum')
@view('views/impressum')
def impressum():
    pass


@route('/static/<filename:path>', no_i18n=True)
def send_static(filename):
    return static_file(filename, root=os.path.join(MOD_PATH, 'static'))


# findet templates im gleichen Verzeichnis
TEMPLATE_PATH.append(MOD_PATH)
app = default_app()
application = I18NPlugin(app, langs=LANGS, default_locale=DEFAULT_LOCALE,
                         domain='messages',
                         locale_dir=os.path.join(MOD_PATH, 'locales'))
