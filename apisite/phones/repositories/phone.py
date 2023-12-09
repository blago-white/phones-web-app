from rest_framework.response import Response

from phones.services.domain import phones
from phones import serializers

from . import _base
from ._base import _PrimaryKey, _RequestPostData


class PhonesRepository(_base.BaseRepository):
    _service = phones.PhoneService()
    _serializer = serializers.PhoneSerializer

    def get_all(self, limit: int = None) -> dict:
        objects = self._service.get_all(limit=limit)
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data

    def get(self, pk: _PrimaryKey) -> dict:
        phone_instance = self._service.get(pk=pk)

        return self._serializer(instance=phone_instance).data

    def create(self, data: _RequestPostData) -> dict:
        phone_serializer = self._serializer(data=data)

        phone_serializer.is_valid(raise_exception=True)

        self._service.create(data=phone_serializer.validated_data)

        return phone_serializer.data

    def update(self, pk: _PrimaryKey, data: _RequestPostData):
        serializer = self._serializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        updated_instance = self._service.update(pk=pk, data=serializer.validated_data)

        return self._serializer(instance=updated_instance).data

    def delete(self, pk: _PrimaryKey) -> None:
        self._service.delete(pk=pk)
