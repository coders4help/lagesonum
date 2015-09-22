# coding: utf-8

# Skript zum lokalen Testen, PythonAnywhere verwendet bottle_app.py direkt

from bottle import run, debug
from lagesonum.bottle_app import application

debug(True)
run(application, host='localhost', port=8080, reloader=True)
