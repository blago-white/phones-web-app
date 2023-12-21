from phones.services.domain.brands import BrandService
from phones.serializers.brands import BrandSerializer

from . import base


__all__ = ["BrandRepository"]


class BrandRepository(base.DefaultRepository):
    _service = BrandService()
    _serializer = BrandSerializer
