
# Datei zum lokalen testen, PythonAnywhere verwendet bottle_app.py direkt

from bottle_app import application
from bottle import run

run(application, host='localhost', port=8080)