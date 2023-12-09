from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100)
