from typing import Callable

from django.http import request
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from phones import config
from phones.repositories.base import BaseRepository


class BaseResponseAPIViewMixin:
    request: request.HttpRequest
    kwargs: request.QueryDict

    _response_class: Callable = Response


class ModelAPIViewMixin(BaseResponseAPIViewMixin):
    serializer_class: ModelSerializer
    _repository: BaseRepository

    def get_200_response(self, data: dict = None) -> Response:
        return self._response_class(
            data=data,
            status=status.HTTP_200_OK
        )

    def get_queryset(self, *args, **kwargs) -> None:
        pass


class POSTAPIViewMixin(BaseResponseAPIViewMixin):
    def get_request_data(self) -> dict:
        return self.request.POST


class RetrieveAPIViewMixin(ModelAPIViewMixin):
    def get_requested_pk(self) -> int:
        return self.kwargs.get(config.PHONE_PK_URL_FIELD)


class CreateAPIViewMixin(ModelAPIViewMixin, POSTAPIViewMixin):
    request: request.HttpRequest

    def get_201_response(self, data: dict = None):
        return self._response_class(
            data=data,
            status=status.HTTP_201_CREATED
        )
