from django.db import models

from .options import BasePhoneOption
from ._choises import PhoneStorageChoises


class PhoneStorage(BasePhoneOption):
    size = models.IntegerField(max_length=PhoneStorageChoises.max_length,
                               choices=PhoneStorageChoises.choices,
                               default=PhoneStorageChoises.STORAGE_SIZE_128)

    class Meta:
        db_table = "phones_phone_storages"
