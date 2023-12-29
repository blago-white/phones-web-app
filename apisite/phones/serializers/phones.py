from rest_framework import serializers

from phones.models import phone, base
from phones.services.domain import brands as brands_services, \
    phones as phones_services
from rest_framework import serializers

from phones.models import phone, base
from phones.services.domain import brands as brands_services, \
    phones as phones_services

__all__ = ["PhoneSerializer", "PhonePositionSerializer"]


class _BrandPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.pk} ({instance.title})"


class _PhonePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    _service = phones_services.PhoneService()

    def get_queryset(self):
        return self._service.get_all()


class PhoneSerializer(serializers.ModelSerializer):
    brand = _BrandPrimaryKeyRelatedField(
        queryset=brands_services.BrandService().get_all(),
        allow_empty=False,
    )

    class Meta:
        fields = ["id", "brand", "title"]
        read_only_fields = ["id"]
        model = phone.Phone


class PhonePositionSerializer(serializers.ModelSerializer):
    phone = _PhonePrimaryKeyRelatedField()
    price = serializers.IntegerField(max_value=32767)

    class Meta:
        fields = "__all__"
        model = base.PhonePosition
