from rest_framework import serializers
from phones.models import brands


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = brands.Brand
