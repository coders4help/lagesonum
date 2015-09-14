# coding: utf-8

# Datei zum lokalen testen, PythonAnywhere verwendet bottle_app.py direkt

from bottle import run

from bottle_app import application

run(application, host='localhost', port=8080)
