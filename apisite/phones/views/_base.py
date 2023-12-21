from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet

from phones.mixins import base


class DefaultModelViewSet(base.APIViewSetMixin,
                          ModelViewSet):
    def get_all(self, request: HttpRequest):
        return self.get_200_response(data=self._repository.get_all())

    def retrieve(self, request: HttpRequest, *args, **kwargs):
        object_pk = self.get_requested_pk()

        data = self._repository.get(pk=object_pk)

        return self.get_200_response(data=data)

    def create(self, request: HttpRequest, **kwargs):
        request_data = self.get_request_data()
        return self.get_201_response(
            data=self._repository.create(data=request_data)
        )

    def destroy(self, request: HttpRequest, **kwargs):
        self._repository.delete(pk=self.get_requested_pk())
        return self.get_200_response()

    def update(self, request: HttpRequest, **kwargs):
        return self.get_200_response(
            data=self._repository.update(
                pk=self.get_requested_pk(),
                data=self.request.POST)
        )
