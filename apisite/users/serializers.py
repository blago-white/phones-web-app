from rest_framework.serializers import ModelSerializer

from .models import Seller


class SellerAccountSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ["id", "username", "password", "email"]
        read_only_fields = ["id"]
