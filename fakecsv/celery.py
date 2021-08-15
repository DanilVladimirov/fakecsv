import os

from celery import Celery
from fakecsv.settings import REDIS_URL

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fakecsv.settings')

app = Celery('fakecsv')

app.conf.broker_url = REDIS_URL
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
