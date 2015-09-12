
# Der WSGI-Server auf PythonAnywhere verwendet diese Datei

# A very simple Bottle Hello World app for you to get started with...
import bottle
from bottle import default_app, route, view
from bottle import response, request
import os, time
import lagesonum.input_number as ip

"""
ENCODING: Default ist UTF-8, ändern mit:

    response.charset = 'ISO-8859-15'
    response.content_type = 'text/html; charset=latin9'
"""

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
    for num in numbers:
        print ('NUMBER TO STORE: ', num, timestamp)

        if ip.is_valid_number(num) and ip.is_ok_with_db(num) and ip.is_valid_user():
            print ("Input validated")

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
    return {'result': '-', 'timestamp_first': '-', 'timestamp_last': '-'}

FAKE_DATA = {
    '123': ('Jan 1st', 'Dec 31st'),
    '456': ('Apr 11th', 'Apr 12th'),
}

@route('/query', method='POST')
@view('query_page')
def do_query():
    number = request.forms.get('number')
    print ('NUMBER TO QUERY: ', number)
    timestamp_first, timestamp_last = FAKE_DATA.get(number, ('NOT FOUND', '-'))
    return {'result': number, 'timestamp_first': timestamp_first, 'timestamp_last': timestamp_last}


bottle.TEMPLATE_PATH.append(os.path.split(__file__)[0]) # findet templates im gleichen Verzeichnis
application = default_app()

