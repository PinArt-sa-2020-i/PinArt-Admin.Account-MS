#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python /code/ConfigAccount/manage.py migrate --noinput

# Start server
echo "Starting server"
python /code/ConfigAccount/manage.py runserver 0.0.0.0:8000
