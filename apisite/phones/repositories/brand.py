from phones.serializers.brands import BrandSerializer
from phones.services.domain.brands import BrandService
from . import default

__all__ = ["BrandRepository"]


class BrandRepository(default.DefaultRepository):
    _service = BrandService()
    _serializer = BrandSerializer
