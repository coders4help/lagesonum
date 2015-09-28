# coding: utf-8

# Datei zum lokalen testen, PythonAnywhere verwendet bottle_app.py direkt

from bottle import run, debug

from lagesonum.bottle_app import application

#debug(True)
run(application, host='78.46.177.127', port=80, reloader=True)
