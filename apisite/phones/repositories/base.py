from abc import ABCMeta, abstractmethod

from rest_framework import serializers

from phones.services.domain import base

_RequestPostData = dict[str, int | str]
_PrimaryKey = int


class BaseRepository(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _service(self) -> base.BaseModelService:
        pass

    @property
    @abstractmethod
    def _serializer(self) -> serializers.Serializer:
        pass

    @abstractmethod
    def get_all(self) -> dict:
        pass

    @abstractmethod
    def get(self, pk: _PrimaryKey) -> dict:
        pass

    @abstractmethod
    def create(self, data: _RequestPostData) -> dict:
        pass

    @abstractmethod
    def update(self, pk: _PrimaryKey, data: _RequestPostData):
        pass

    @abstractmethod
    def delete(self, pk: _PrimaryKey) -> None:
        pass


class DefaultRepository(BaseRepository, metaclass=ABCMeta):
    def get_all(self) -> dict:
        objects = self._service.get_all()
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data

    def get(self, pk: _PrimaryKey) -> dict:
        return self._serializer(instance=self._service.get(pk=pk)).data

    def create(self, data: _RequestPostData) -> dict:
        serializer = self._serializer(data=data)

        serializer.is_valid(raise_exception=True)

        self._service.create(data=serializer.validated_data)

        return serializer.data

    def update(self, pk: _PrimaryKey, data: _RequestPostData):
        serializer = self._serializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_instance = self._service.update(pk=pk, data=serializer.validated_data)

        return self._serializer(instance=updated_instance).data

    def delete(self, pk: _PrimaryKey) -> None:
        self._service.delete(pk=pk)
