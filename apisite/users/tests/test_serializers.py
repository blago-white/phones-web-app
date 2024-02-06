import secrets

from django.test import TransactionTestCase

from users.serializers import SellerAccountSerializer


class SellerAccountSerializerTestCase(TransactionTestCase):
    def setUp(self):
        self.test_username = "test"
        self.test_email = "example@example.com"
        self.test_password = secrets.token_urlsafe(9)

    def test_fields(self):
        credentals = {
            "username": self.test_username,
            "password": self.test_password,
            "email": self.test_email
        }

        serializer = SellerAccountSerializer(data=credentals)

        self.assertTrue(serializer.is_valid())

        self.assertEquals(serializer.validated_data, credentals)
