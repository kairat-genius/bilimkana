#!/bin/bash

python manage.py makemigrations

python manage.py migrate

gunicorn --config gunicorn_config.py settings.wsgi:application
