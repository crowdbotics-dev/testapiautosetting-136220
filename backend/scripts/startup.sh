#!/bin/bash

python manage.py migrate --noinput

waitress-serve --port=$PORT testapiautosetting_136220.wsgi:application
