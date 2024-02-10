from django.db import models
from rest_framework.exceptions import APIException

from phones.models import base, phone
from phones.utils.options import CardOptions
from common.services.base import BaseModelService


class PhoneService(BaseModelService):
    _model: phone.Phone = phone.Phone

    def get_all(self, limit: int = None) -> models.QuerySet:
        queryset = super().get_all()

        if limit is not None:
            queryset = queryset[:max(0, limit)]

        return queryset

    def update(self, pk, data) -> models.Model:
        try:
            instances = self._model.objects.filter(pk=pk)
            instance = instances.first()

            instances.update(**data)

        except ValidationError:
            raise ValidationError("Object does not exists or data for update is not correct")

        return instance


class PhonePositionService(BaseModelService):
    _model: base.PhonePosition = base.PhonePosition

    def get_related(self, phone_id: int) -> models.QuerySet:
        return self._model.objects.filter(phone_id=phone_id)

    def get_default_instance_options(self, phone_id: int) -> models.QuerySet:
        try:
            return self._model.objects.filter(phone_id=phone_id).values("color", "storage").first()
        except AttributeError:
            raise APIException(detail="Not a single card exists")

    def get_by_options(self, phone_id: int, options: CardOptions) -> base.PhonePosition:
        try:
            return self._model.objects.get(phone_id=phone_id, **options.as_dict)
        except models.ObjectDoesNotExist:
            raise APIException(detail="Card does not exists")
