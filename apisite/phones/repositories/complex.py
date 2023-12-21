from phones import serializers
from phones.services.domain import phones

from . import base

__all__ = ("PhonesCardRepository",)


class PhonesCardRepository(base.DefaultRepository):
    _serializer = serializers.PhonePositionSerializer
    _service = phones.PhonePositionService()

    def get_all_for_pk(self, pk: int) -> dict:
        return self._serializer(self._service.get_related(phone_id=pk), many=True).data
