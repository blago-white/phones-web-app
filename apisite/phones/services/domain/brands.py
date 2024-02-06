from phones.models import brands
from common.services.base import BaseModelService


class BrandService(BaseModelService):
    _model: brands.Brand = brands.Brand
