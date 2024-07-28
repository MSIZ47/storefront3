import os
from celery import Celery
#1 :set an enviorment variale called django_settings_module for storefront.settings.dev
os.environ.setdefault('DJANGO_SETTINGS_MODULE','storefront.settings.dev')
#2 :create celery instance and give it a name
celery = Celery('storefront')
#3 :specify where celery can find configuration variables..the answer is settings
# give a namespace means all our configuration settings should start with celery 
celery.config_from_object('django.conf:settings', namespace='CELERY') # : means load settings from django.conf

#4: we give our redis server as an broker to our celery...we should do this in settings.py

#5 :insruct celery to automaticlly discover tasks in task.py
celery.autodiscover_tasks()

#6 :after setting up the celery we should load this in the init module of the currnt package so that python execute this codes for us