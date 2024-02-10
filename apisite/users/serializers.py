from rest_framework.serializers import ModelSerializer

from .models import Seller


class SellerAccountSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = ["id", "username", "password", "email"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = (self.Meta.model(username=validated_data["username"]))
        user.set_password(validated_data["password"])

        user.save()

        return user
