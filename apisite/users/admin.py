from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Seller


@admin.register(Seller)
class SellerAdmin(UserAdmin):
    pass
