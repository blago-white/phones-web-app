from django.db import models

from phones.models import base, phone
from .base import BaseModelService


class PhoneService(BaseModelService):
    _model: phone.Phone = phone.Phone

    def get_all(self, limit: int = None) -> models.QuerySet:
        queryset = super().get_all()

        if limit is not None:
            queryset = queryset[:max(0, limit)]

        return queryset


class PhonePositionService(BaseModelService):
    _model: base.PhonePosition = base.PhonePosition

    def get_related(self, phone_id: int):
        return self._model.objects.filter(phone_id=phone_id)
