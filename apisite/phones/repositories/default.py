from abc import ABCMeta, abstractmethod

from common.repositories.default import DefaultRepository, DefaultThroughtModelRepository
from common.services.base import BaseModelService

from phones.models.phone import Phone
from phones.models.base import PhonePosition


class DefaultAuthorityModelRepository(DefaultRepository,
                                      metaclass=ABCMeta):
    def has_authority(self, product_pk: int, user_pk: int) -> bool:
        product: Phone = self._service.get(pk=product_pk)

        return product.seller.pk == user_pk


class DefaultAuthorityThroughtModelRepository(DefaultThroughtModelRepository,
                                              metaclass=ABCMeta):
    def has_authority(self, product_pk: int, user_pk: int) -> bool:
        through_obj: PhonePosition = self._service.get(pk=product_pk)

        return through_obj.phone.seller.pk == user_pk
