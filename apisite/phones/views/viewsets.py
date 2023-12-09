from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet

from phones import mixins, repositories


class PhoneViewSet(mixins.BasePhoneViewSetMixin, ModelViewSet):
    _repository: repositories.PhonesRepository

    def get_all(self, request: HttpRequest):
        return self.get_200_response(data=self._repository.get_all(self.get_request_limit()))

    def retrieve(self, request, *args, **kwargs):
        phone_id = self.get_phone_id()
        return self.get_200_response(data=self._repository.get(pk=phone_id))

    def create(self, request: HttpRequest, **kwargs):
        request_data = self.get_request_data()
        return self.get_201_response(data=self._repository.create(data=request_data))

    def destroy(self, request: HttpRequest, **kwargs):
        self._repository.delete(pk=self.get_phone_id())
        return self.get_200_response()

    def update(self, request: HttpRequest, **kwargs):
        return self.get_200_response(
            data=self._repository.update(pk=self.get_phone_id(), data=self.request.POST)
        )
