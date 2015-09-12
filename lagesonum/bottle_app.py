
# Der WSGI-Server auf PythonAnywhere verwendet diese Datei

# A very simple Bottle Hello World app for you to get started with...
import bottle
from bottle import default_app, route, view
from bottle import response, request
import sqlite3
import os, time
import lagesonum.input_number as ip

"""
ENCODING: Default ist UTF-8, ändern mit:

    response.charset = 'ISO-8859-15'
    response.content_type = 'text/html; charset=latin9'
"""

MOD_PATH = os.path.split(__file__)[0]
lagesonrdb = sqlite3.connect(MOD_PATH + os.sep + "lagesonr.db")

@route('/')
@view('start_page')
def index():
    """1.Seite: Helfer steht am LaGeSo und gibt Nummern ein [_____] """
    return {'entered': []}

@route('/arab')
@view('start_page_arab')
def index_arab():
    return {'entered': []}


@route('/enter', method='POST')
@view('start_page')
def do_enter():
    numbers = request.forms.get('numbers')
    timestamp = time.asctime()
    numbers = [num.strip() for num in numbers.split('\n')]
    with lagesonrdb as con:
        cur = con.cursor()
        for num in numbers:
            if ip.is_valid_number(num) and ip.is_ok_with_db(num) and ip.is_valid_user():
                insert = 'INSERT INTO NUMBERS(NUMBER, TIME, PLACE, USER) VALUES ("%s", "%s", "-", "-")' % (num, timestamp)
                cur.execute(insert)
            else:
                return "INVALID INPUT: " + "num"

    return {'entered': numbers, 'timestamp': timestamp}


@route('/query')
@view('query_page')
def query_number():
    """
    2. Seite: Flüchtling fragt ab: Wurde meine Nummer gezogen? [_____] 
    => Antwort: X mal am LaGeSo eingetragen von (Erste Eintragung) 
    DD.MM.YY hh bis DD.MM.YY hh (LetzteEintragung)
    application = default_app()
    """
    return {'result': '-', 'timestamp_first': '-', 'timestamp_last': '-', 'n':'0'}


@route('/query', method='POST')
@view('query_page')
def do_query():
    number = request.forms.get('number')
    with lagesonrdb as con:
        cur = con.cursor()
        query = 'SELECT TIME FROM NUMBERS WHERE NUMBER="%s" ORDER BY TIME' % number
        result = list(cur.execute(query))
        n = len(result)
        if n > 0:
            timestamp_first, timestamp_last = result[0][0], result[-1][0]
            return {'result': number, 'timestamp_first': timestamp_first, 'timestamp_last': timestamp_last, 'n':n}
    return {'result': 'number', 'timestamp_first': 'NOT FOUND', 'timestamp_last': '-', 'n':'0'}


bottle.TEMPLATE_PATH.append(MOD_PATH) # findet templates im gleichen Verzeichnis
application = default_app()

