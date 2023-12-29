from abc import ABCMeta, abstractmethod

from django.core.exceptions import ValidationError
from django.db import models

from common.models import utils


class AbstractModelService(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _model(self) -> models.Model:
        pass

    @abstractmethod
    def get_all(self) -> models.QuerySet:
        pass

    @abstractmethod
    def get(self, pk) -> models.Model:
        pass

    @abstractmethod
    def create(self, data) -> models.Model:
        pass

    @abstractmethod
    def update(self, pk, data) -> models.Model:
        pass

    @abstractmethod
    def delete(self, data) -> None:
        pass


class BaseModelService(AbstractModelService, metaclass=ABCMeta):
    def get_all(self) -> models.QuerySet:
        return self._model.objects.all()

    def get(self, pk) -> models.Model:
        return self._model.objects.get(pk=pk)

    def create(self, data) -> models.Model:
        instance: models.Model = self._model(**data)

        return utils.save_validated(instance=instance)

    def update(self, pk, data) -> models.Model:
        try:
            instance, created = self._model.objects.update_or_create(
                pk=pk,
                defaults=dict(**data)
            )
        except ValidationError:
            raise ValidationError("Object does not exists or data for update is not correct")

        return utils.save_validated(instance=instance)

    def delete(self, pk) -> None:
        self.get(pk=pk).delete()
