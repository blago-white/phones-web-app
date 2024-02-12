from abc import ABCMeta
from rest_framework.serializers import ModelSerializer

from common.services import base
from common.repositories.base import (BaseModelRepository, BaseThroughModelRepository,
                                      PrimaryKey, RequestPostData)


class DefaultRepository(BaseModelRepository, metaclass=ABCMeta):
    @property
    def service(self) -> base.BaseModelService:
        return self._service

    def get_all(self) -> dict:
        objects = self._service.get_all()
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data

    def get(self, pk: PrimaryKey) -> dict:
        return self._serializer(instance=self._service.get(pk=pk)).data

    def create(self, data: RequestPostData) -> dict:
        serializer = self._serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer = self._serializer(
            instance=self._service.create(data=serializer.validated_data)
        )

        return serializer.data

    def update(self, pk: PrimaryKey, data: RequestPostData):
        serializer = self._serializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_instance = self._service.update(pk=pk, data=serializer.validated_data)

        return self._serializer(instance=updated_instance).data

    def delete(self, pk: PrimaryKey) -> None:
        self._service.delete(pk=pk)


class DefaultThroughtModelRepository(BaseThroughModelRepository, metaclass=ABCMeta):
    @property
    def service(self) -> base.BaseModelService:
        return self._service

    def get_all(self, pk: PrimaryKey) -> dict:
        objects = self._service.get_all()
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data

    def get(self, through_pk: PrimaryKey) -> dict:
        return self._serializer(instance=self._service.get(pk=through_pk)).data

    def create(self, data: RequestPostData, pk: PrimaryKey) -> dict:
        serializer: ModelSerializer = self._serializer(data=data)

        serializer.is_valid(raise_exception=True)

        self._service.create(data=serializer.validated_data)

        return serializer.data

    def update(self, through_pk: PrimaryKey, data: RequestPostData) -> None:
        serializer = self._serializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_instance = self._service.update(pk=through_pk, data=serializer.validated_data)

        return self._serializer(instance=updated_instance).data

    def delete(self, through_pk: PrimaryKey) -> None:
        self._service.delete(pk=through_pk)

