from django.db import models

from common.services.base import BaseModelService

from users.models import Seller


class SellerService(BaseModelService):
    _model = Seller
