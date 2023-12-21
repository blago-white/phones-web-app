from django.db import models

from ._choises import PhoneStorageChoises
from .options import BasePhoneOption


class PhoneStorage(BasePhoneOption):
    size = models.IntegerField(choices=PhoneStorageChoises.choices, default=PhoneStorageChoises.STORAGE_SIZE_128)

    def __str__(self):
        return self.get_size_display()

    class Meta:
        db_table = "phones_phone_storages"
