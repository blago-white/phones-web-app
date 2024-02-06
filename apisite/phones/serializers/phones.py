from rest_framework import serializers

from django.db import models

from phones.models import phone, base
from phones.services.domain import brands as brands_services, \
    phones as phones_services
from rest_framework import serializers

from phones.models import phone, base
from phones.services.domain import brands as brands_services, \
    phones as phones_services

from users.config import DEFAULT_SERIALIZER_SELLER_FIELD_NAME


__all__ = ["PhoneSerializer", "PhonePositionSerializer"]


class _BrandPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.pk} ({instance.title})"


class _PhonePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    _service = phones_services.PhoneService()

    def get_queryset(self):
        return self._service.get_all()


class CurrentUserDefault:
    """
    "May be applied as a `default=...` value on a serializer field. Returns the current user."
    """
    requires_context = True

    def __call__(self, serializer_field) -> int | models.Model:
        return serializer_field.parent.initial_data.get(
            DEFAULT_SERIALIZER_SELLER_FIELD_NAME
        )


class PhoneSerializer(serializers.ModelSerializer):
    seller = serializers.HiddenField(default=CurrentUserDefault())

    brand = _BrandPrimaryKeyRelatedField(
        queryset=brands_services.BrandService().get_all(),
        allow_empty=False,
    )

    class Meta:
        fields = ["id", "brand", "title", DEFAULT_SERIALIZER_SELLER_FIELD_NAME]
        read_only_fields = ["id"]
        model = phone.Phone


class PhonePositionSerializer(serializers.ModelSerializer):
    phone = _PhonePrimaryKeyRelatedField(required=False)
    price = serializers.IntegerField(max_value=32767)

    class Meta:
        fields = "__all__"
        model = base.PhonePosition
