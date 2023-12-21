from phones.models import brands
from .base import BaseModelService


class BrandService(BaseModelService):
    _model: brands.Brand = brands.Brand
