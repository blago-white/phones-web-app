from django.db import models
from phones.tasks import test_sleep_task


def save_validated(instance: models.Model) -> models.Model:
    instance.full_clean()
    instance.save()

    # test_sleep_task.delay()

    return instance
