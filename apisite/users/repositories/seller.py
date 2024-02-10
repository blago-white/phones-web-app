from common.repositories.default import DefaultRepository

from users.serializers import SellerAccountSerializer
from users.services.sellers import SellerService


class SellersRepository(DefaultRepository):
    _service = SellerService()
    _serializer = SellerAccountSerializer
