from rest_framework.exceptions import PermissionDenied

from common.repositories.base import PrimaryKey, RequestPostData
from common.repositories import default

from phones.serializers import phones as phones_serializers
from phones.services.domain import phones
from phones.repositories.default import DefaultAuthorityModelRepository

__all__ = ("PhonesRepository", )


class PhonesRepository(DefaultAuthorityModelRepository):
    _service = phones.PhoneService()
    _serializer = phones_serializers.PhoneSerializer

    def get_all(self, limit: int = None) -> dict:
        objects = self._service.get_all(limit=limit)
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data
