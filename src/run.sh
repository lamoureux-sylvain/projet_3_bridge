#!/bin/sh

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
gunicorn projet_3_bridge.wsgi --bind=0.0.0.0:80
