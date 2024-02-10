from typing import OrderedDict

from django.contrib.auth.models import AbstractUser
from django.db import models

from common.services.base import BaseModelService
from common.models import utils

from users.models import Seller


class SellerService(BaseModelService):
    _model = Seller

    def create(self, data: OrderedDict) -> models.Model:
        user = self._model(**data)

        self._set_password(user=user, data=data)

        return utils.save_validated(user)

    def _set_password(self, user: AbstractUser, data: OrderedDict):
        user.set_password(
            raw_password=dict(data).pop("password")
        )
