from users.repositories.seller import SellersRepository

from users.serializers import SellerAccountSerializer


class UserRegisterMixin:
    serializer_class = SellerAccountSerializer
    _repository = SellersRepository()
