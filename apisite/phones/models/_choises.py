from django.db import models


class _BasePhoneChoises(models.IntegerChoices):
    _MAX_LENGTH: int

    @property
    def max_length(self):
        return self._MAX_LENGTH


class PhoneStorageChoises(_BasePhoneChoises):
    STORAGE_SIZE_32 = 1, 32
    STORAGE_SIZE_64 = 2, 64
    STORAGE_SIZE_128 = 3, 128
    STORAGE_SIZE_256 = 4, 256
    STORAGE_SIZE_1024 = 5, 1024

    _MAX_LENGTH = 1


class PhoneColorsChoises(_BasePhoneChoises):
    COLOR_RED = "r", "Red"

    _MAX_LENGTH = 1
