from django.db import models


def save_validated(instance: models.Model) -> models.Model:
    instance.full_clean()
    instance.save()

    return instance
