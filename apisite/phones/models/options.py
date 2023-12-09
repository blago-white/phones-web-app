from django.db import models

from . import phone


class BasePhoneOption(models.Model):
    phone = models.ForeignKey(to=phone.Phone, on_delete=models.CASCADE)

    class Meta:
        abstract = True
