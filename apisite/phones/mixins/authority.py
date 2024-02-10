from django.http import HttpRequest

from rest_framework.exceptions import PermissionDenied

from common.repositories.base import BaseRepository


class CheckAuthorityViewSetMixin:
    restrict_no_authority = True
    product_pk_url_kwarg: str = None

    _repository: BaseRepository

    def update(self, request: HttpRequest, **kwargs):
        if self._repository.has_authority(
            product_pk=self.kwargs.get(self.product_pk_url_kwarg),
            user_pk=request.user.pk
        ) or not self.restrict_no_authority:
            return super().update(request=request, **kwargs)

        raise PermissionDenied(
            detail="You are not the seller of this product"
        )
