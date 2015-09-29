# coding: utf-8

# Datei zum lokalen testen, PythonAnywhere verwendet bottle_app.py direkt

from bottle import run, debug

from bottle_app import application

#debug(True)
run(application, host='172.31.1.100', port=80, reloader=True)
