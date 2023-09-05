#!/usr/bin/env bash
# exit on error
set -o errexit

python -m pip install -U pip

pip install -r requirements.txt

pyhton manage.py collectstatic --no-input
python manage.py migrate
