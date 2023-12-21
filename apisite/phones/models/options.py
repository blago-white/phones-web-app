from django.db import models


class BasePhoneOption(models.Model):
    class Meta:
        abstract = True
