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
    id = serializers.HiddenField(default=None)

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
# '_kwargs': {'default': <phones.serializers.phones.CurrentUserDefault object at 0x0000013CC09A7350>},
# '_creation_counter': 10,
# 'read_only': False,
# 'write_only': True,
# 'required': False,
# 'default': <phones.serializers.phones.CurrentUserDefault object at 0x0000013CC09A7350>,
# 'source': 'seller',
# 'initial': None,
# 'label': 'Seller',
# 'help_text': None,
# 'style': {},
# 'allow_null': False,
# 'field_name': 'seller',
# 'parent': PhoneSerializer(data={'title': 'iphone 15 pro max', 'brand': 'apple', 'seller': 1}):
