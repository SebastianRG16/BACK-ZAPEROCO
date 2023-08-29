#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate

# if python manage.py createsuperuser --no-input; then
#     echo "Superuser created successfully"
#     python manage.py shell -c "from django.contrib.auth.models import User; user = User.objects.get(username='admin@admin.com'); user.is_staff = True; user.is_superuser = True; user.save()" && echo "Permissions granted"
# else
#     echo "Error creating superuser"
# fi