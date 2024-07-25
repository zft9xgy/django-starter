#!/bin/sh

rm $(pwd)/db.sqlite3
python $(pwd)/manage.py makemigrations
python $(pwd)/manage.py migrate
#python manage.py collectstatic --noinput 
export DJANGO_SUPERUSER_PASSWORD='hola1234'
python $(pwd)/manage.py createsuperuser --noinput --username jade --email jade@email.es

