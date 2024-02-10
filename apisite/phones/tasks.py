import time

from django.db.models import Model

from celery import shared_task


@shared_task
def test_sleep_task():
    time.sleep(10)
