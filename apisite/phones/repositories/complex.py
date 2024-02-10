from phones import serializers
from phones.services.domain import phones
from phones.utils.options import CardOptions
from common.repositories import base, default

from .default import DefaultAuthorityThroughtModelRepository

__all__ = ("PhonesCardRepository",)


class PhonesCardRepository(DefaultAuthorityThroughtModelRepository):
    _serializer = serializers.PhonePositionSerializer
    _service = phones.PhonePositionService()

    def create(self, data: base.RequestPostData, pk: int = None) -> dict:
        data |= {"phone": [str(pk)]}

        serializer = self._serializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer.data

    def get_related(self, pk: int) -> dict:
        return self._serializer(
            self._service.get_related(phone_id=pk),
            many=True
        ).data

    def get_default_card_options(self, pk: int) -> dict:
        return self._service.get_default_instance_options(phone_id=pk)

    def get_by_option_for_pk(self, pk: int, card_options: CardOptions) -> dict:
        card = self._service.get_by_options(phone_id=pk, options=card_options)
        return self._serializer(card).data
