from phones.serializers import phones as phones_serializers
from phones.services.domain import phones
from . import default

__all__ = ("PhonesRepository", )


class PhonesRepository(default.DefaultRepository):
    _service = phones.PhoneService()
    _serializer = phones_serializers.PhoneSerializer

    def get_all(self, limit: int = None) -> dict:
        objects = self._service.get_all(limit=limit)
        serialized_objects = self._serializer(
            instance=objects,
            many=True
        )

        return serialized_objects.data
