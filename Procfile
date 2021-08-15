web: gunicorn fakecsv.wsgi
release: python manage.py makemigrations
release: python manage.py migrate
worker: celery -A fakecsv worker -l info