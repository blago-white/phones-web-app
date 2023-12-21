from django.db import models


class PhoneStorageChoises(models.IntegerChoices):
    STORAGE_SIZE_32 = 32
    STORAGE_SIZE_64 = 64
    STORAGE_SIZE_128 = 128
    STORAGE_SIZE_256 = 256
    STORAGE_SIZE_512 = 512
    STORAGE_SIZE_1024 = 1024


class PhoneColorsChoises(models.TextChoices):
    COLOR_RED = "r", "Red"
    COLOR_WHITE = "w", "White"
    COLOR_BLACK = "b", "Black"


def get_max_length(choises: models.enums.ChoicesType):
    return len(max(choises.values, key=len))
