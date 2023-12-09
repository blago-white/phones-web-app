from django.db import models

from .options import BasePhoneOption
from ._choises import PhoneColorsChoises


class PhoneColor(BasePhoneOption):
    color = models.CharField(max_length=PhoneColorsChoises.max_length,
                             choices=PhoneColorsChoises.choices)

    class Meta:
        db_table = "phones_phone_colors"
