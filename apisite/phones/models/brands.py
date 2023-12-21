from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=100, primary_key=True, unique=True)

    def __str__(self):
        return self.title.capitalize()
