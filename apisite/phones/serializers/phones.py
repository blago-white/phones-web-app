from rest_framework import serializers

from phones.services.domain import brands as brands_services
from phones.models import phone, base
from rest_framework import serializers

from phones.models import phone, base
from phones.services.domain import brands as brands_services

__all__ = ["PhoneSerializer", "PhonePositionSerializer"]


class _BrandPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return f"{instance.pk} ({instance.title})"


class PhoneSerializer(serializers.ModelSerializer):
    brand = _BrandPrimaryKeyRelatedField(
        queryset=brands_services.BrandService().get_all(),
        allow_empty=False,
    )

    class Meta:
        fields = ["brand", "title"]
        model = phone.Phone


class PhonePositionSerializer(serializers.ModelSerializer):
    phone = PhoneSerializer(read_only=True)

    price = serializers.IntegerField(max_value=32767)

    class Meta:
        fields = "__all__"
        model = base.PhonePosition
