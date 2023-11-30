from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "library.settings")

app = Celery("library")

app.config_from_object("django.conf:settings", namespace="CELERY")
# app.config_from_object("django.conf:settings")
# app.conf.broker_connection_retry_on_startup = True
# app.autodiscover_tasks(["libraryapp"])
app.autodiscover_tasks()
