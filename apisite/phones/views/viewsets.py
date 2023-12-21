from django.http import HttpRequest
from django.http.response import HttpResponseNotAllowed

from phones import mixins, repositories
from . import _base


class PhoneViewSet(mixins.BasePhoneViewSetMixin, _base.DefaultModelViewSet):
    _repository: repositories.PhonesRepository

    def get_all(self, request: HttpRequest):
        return self.get_200_response(data=self._repository.get_all(self.get_request_limit()))


class PhoneCardViewSet(mixins.BasePhoneCardViewSetMixin, _base.DefaultModelViewSet):
    _repository: repositories.PhonesCardRepository

    def get_all(self, request: HttpRequest, **kwargs):
        cards = self._repository.get_all_for_pk(pk=self.get_requested_pk())
        return self.get_200_response(data=cards)
