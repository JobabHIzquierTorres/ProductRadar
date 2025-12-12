from celery import Celery

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProductRadar.settings')

app = Celery('ProductRadar')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
