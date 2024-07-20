#!/bin/bash

python manage.py makemigrations

python manage.py migrate

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser(username='admin', email='', password='admin')" | python manage.py shell

python manage.py runserver 0.0.0.0:8000