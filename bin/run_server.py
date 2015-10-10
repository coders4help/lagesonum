#!/usr/bin/env python3
# coding: utf-8

# Skript zum lokalen Testen, PythonAnywhere verwendet bottle_app.py direkt

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lagesonum')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from bottle import run, debug
from bottle_werkzeug import WerkzeugDebugger
from lagesonum.bottle_app import application

debug(True)
application.catchall = False
run(WerkzeugDebugger(application), host='localhost', port=8080, reloader=True)
