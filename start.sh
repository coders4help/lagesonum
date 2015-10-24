#!/bin/bash
#
# Runs 3 steps to keep source and serve in sync.
# Works with and was build to use with docker.
# 1. Migrate db to sync model and db.
# 2. Compile I18n messages
# 3. Run Server with dev settings and listen on all interfaces.
# 
export DJANGO_SETTINGS_MODULE="lagesonum.settings_dev"

python3 manage.py migrate --noinput
cd website
python3 ../manage.py compilemessages
cd ..
python3 manage.py runserver 0.0.0.0:8000
