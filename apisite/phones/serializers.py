from django.db import models

from rest_framework import serializers

from .services.domain import brands as brands_services
from .models import phone, brands


class BrandPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.pk} ({instance.title})"


class PhoneSerializer(serializers.ModelSerializer):
    brand = BrandPrimaryKeyRelatedField(
        queryset=brands_services.BrandService().get_all(),
        allow_empty=False,
    )

    price = serializers.IntegerField(
        max_value=32767
    )

    class Meta:
        fields = ["id", "brand", "title", "price"]
        read_only_fields = ["id"]
        model = phone.Phone
