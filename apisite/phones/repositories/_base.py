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
    def get_all(self, limit: int = None) -> dict:
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
