from django.db import models

from . import brands, colors, storages, base


class Phone(models.Model):
    brand = models.ForeignKey(to=brands.Brand, on_delete=models.SET_NULL, null=True, blank=False)
    title = models.CharField(max_length=100)
    colors = models.ManyToManyField(to=colors.PhoneColor,
                                    related_name="colors",
                                    through=base.PhonePosition)
    storages = models.ManyToManyField(to=storages.PhoneStorage,
                                      related_name="storages",
                                      through=base.PhonePosition)

    def __str__(self):
        return f"{self.brand} {self.title.capitalize()}"
