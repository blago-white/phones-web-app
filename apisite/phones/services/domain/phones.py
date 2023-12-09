from django.db import models

from phones.models import phone
from .base import BaseModelService


class PhoneService(BaseModelService):
    _model: phone.Phone = phone.Phone

    def get_all(self, limit: int = None) -> models.QuerySet:
        queryset = super().get_all()

        if limit is not None:
            queryset = queryset[:max(0, limit)]

        return queryset
