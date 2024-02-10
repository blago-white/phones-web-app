from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Seller(AbstractUser):
    email = models.EmailField(_("email address"), blank=False)

    class Meta:
        verbose_name = "Seller"
        verbose_name_plural = "Sellers"
