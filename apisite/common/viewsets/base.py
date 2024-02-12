from django.http import HttpRequest
from rest_framework.viewsets import ModelViewSet

from common.mixins import api
from common.repositories.base import BaseThroughModelRepository


class DefaultModelViewSet(api.APIViewSetMixin,
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


class DefaultTroughModelViewSet(api.APIViewSetMixin,
                                ModelViewSet):
    trough_pk_url_kwarg: str
    _repository: BaseThroughModelRepository

    def get_all(self, *args, **kwargs):
        object_pk = self.get_requested_pk()

        return self.get_200_response(data=self._repository.get_all(pk=object_pk))

    def get_related(self, *args, **kwargs):
        object_pk = self.get_requested_pk()

        return self.get_200_response(
            data=self._repository.get_related(pk=object_pk)
        )

    def retrieve(self, request: HttpRequest, *args, **kwargs):
        through_pk = self.get_trough_pk()

        data = self._repository.get(through_pk=through_pk)

        return self.get_200_response(data=data)

    def create(self, request: HttpRequest, **kwargs):
        request_data = self.get_request_data()

        return self.get_201_response(
            data=self._repository.create(data=request_data, pk=self.get_requested_pk())
        )

    def destroy(self, request: HttpRequest, **kwargs):
        self._repository.delete(through_pk=self.get_trough_pk())
        return self.get_200_response()

    def update(self, request: HttpRequest, **kwargs):
        return self.get_200_response(
            data=self._repository.update(
                through_pk=self.get_trough_pk(),
                data=self.request.POST)
        )

    def get_trough_pk(self) -> int:
        return self.kwargs.get(self.trough_pk_url_kwarg)
