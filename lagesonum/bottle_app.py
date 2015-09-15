# coding: utf-8

# Der WSGI-Server auf PythonAnywhere verwendet diese Datei

import sqlite3
import os
import time

import bottle
from bottle import default_app, route, view
from bottle import request
from bottle_utils.i18n import I18NPlugin
from bottle_utils.i18n import lazy_gettext as _

import input_number as ip
from dbhelper import initialize_database
import hashlib

MOD_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.abspath(os.path.join(MOD_PATH, '..', '..', "lagesonr.db"))

if not os.path.exists(DB_PATH):
    initialize_database(DB_PATH)

lagesonrdb = sqlite3.connect(DB_PATH)

LANGS = [
    ('de_DE', 'Deutsch'),
    ('en_US', 'English'),
]
# ('ar_AR', 'Arab'),
DEFAULT_LOCALE = 'en_US'

@route('/')
@view('start_page')
def index():
    """1.Seite: Helfer steht am LaGeSo und gibt Nummern ein [_____] """
    return {'entered': []}

@route('/', method='POST')
@view('start_page')
def do_enter():
    numbers = request.forms.get('numbers')
    timestamp = time.asctime()
    numbers = [num.strip() for num in numbers.split('\n')]
    result_num = []
    usr_agent = str(request.environ.get('HTTP_USER_AGENT'))
    usr_lang = str(request.environ.get('HTTP_ACCEPT_LANGUAGE'))
    usr_ip = str(request.remote_addr)

    usr_fingerprint = usr_agent + usr_lang + usr_ip
    usr_hash = hashlib.md5(usr_fingerprint.encode("utf-8")).hexdigest()

    with lagesonrdb as con:
        cur = con.cursor()
        for num in set(numbers):
            if ip.is_valid_number(num) and ip.is_ok_with_db(
                    num) and ip.is_valid_user():

                num = str(num).capitalize()
                query = 'SELECT NUMBER FROM NUMBERS WHERE NUMBER="%s" AND FINGERPRINT="%s"' % (num, usr_hash)
                if len(list(cur.execute(query))) == 0:

                    insert = 'INSERT INTO NUMBERS(NUMBER, TIME, PLACE, USER, FINGERPRINT) VALUES ("%s", "%s", "-", ' \
                             '"-", "%s")' % (num, timestamp, usr_hash)
                    cur.execute(insert)
                    result_num.append(num)
                else:
                    result_num.append("ALREADY ENTERED BY - %s - %s - %s: %s" % (usr_ip, usr_agent, usr_lang, num))
                    #return {'entered': ["already before - by you!"], 'timestamp': timestamp}
            else:
                result_num.append("INVALID INPUT: %s" % num)

    return {'entered': result_num, 'timestamp': timestamp}


@route('/query')
@view('query_page')
def query():
    return {'result': '-', 'timestamp_first': '-','timestamp_last': '-', 'n': '-'}


@route('/query', method='POST')
@view('query_page')
def do_query():
    number = request.forms.get('number')
    timestamp_first = '-'
    timestamp_last = '-'
    n = '0'

    if ip.is_valid_number(number) and ip.is_ok_with_db(
            number) and ip.is_valid_user():

        with lagesonrdb as con:
            cur = con.cursor()

            number = str(number).capitalize()
            query = 'SELECT TIME FROM NUMBERS WHERE NUMBER="%s" ORDER BY TIME' % number
            result = list(cur.execute(query))
            n = len(result)
            if n > 0:
                timestamp_first, timestamp_last = result[0][0], result[-1][0]
            else:
                timestamp_first = 'NOT FOUND'
    else:
        timestamp_first = 'INVALID INPUT'

    return {'result': number, 'timestamp_first': timestamp_first,
                'timestamp_last': timestamp_last, 'n': n}


@route('/impressum')
@view('impressum')
def impressum():
    pass

# findet templates im gleichen Verzeichnis
bottle.TEMPLATE_PATH.append(MOD_PATH)
app = default_app()
application = I18NPlugin(app, langs=LANGS, default_locale=DEFAULT_LOCALE,
                         domain='messages',
                         locale_dir=os.path.join(MOD_PATH, 'locales'))
