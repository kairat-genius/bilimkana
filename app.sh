#!/bin/bash

python manage.py makemigrations

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', email='', password='admin')" | python manage.py shell

gunicorn --config gunicorn_config.py settings.wsgi:application