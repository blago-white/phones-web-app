from django.contrib import admin

from .models import phone, colors, storages, brands, base

for model in (phone.Phone, colors.PhoneColor, storages.PhoneStorage, brands.Brand, base.PhonePosition):
    admin.site.register(model)
