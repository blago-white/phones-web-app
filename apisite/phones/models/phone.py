from django.db import models

from . import brands


class Phone(models.Model):
    brand = models.ForeignKey(to=brands.Brand, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
