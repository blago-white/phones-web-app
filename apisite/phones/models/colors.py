from django.db import models

from ._choises import PhoneColorsChoises, get_max_length
from .options import BasePhoneOption


class PhoneColor(BasePhoneOption):
    color = models.CharField(max_length=get_max_length(PhoneColorsChoises), choices=PhoneColorsChoises.choices)

    def __str__(self):
        return f"{self.get_color_display()}"

    class Meta:
        db_table = "phones_phone_colors"
