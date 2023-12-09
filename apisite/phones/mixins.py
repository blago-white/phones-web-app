from django.http import request

from rest_framework.response import Response
from rest_framework import status

from common import mixins
from . import serializers, config, repositories


class BaseResponseAPIViewMixin:
    _response_class: Response = Response


class PhonesAPIViewMixin(BaseResponseAPIViewMixin):
    serializer_class = serializers.PhoneSerializer
    _repository: repositories.PhonesRepository = repositories.PhonesRepository()

    def get_200_response(self, data: dict = None):
        return self._response_class(
            data=data,
            status=status.HTTP_200_OK
        )

    def get_queryset(self, *args, **kwargs) -> None:
        pass


class PhonesPOSTAPIViewMixin(PhonesAPIViewMixin):
    request: request.HttpRequest

    def get_request_data(self) -> dict:
        return self.request.POST


class PhoneRetrieveAPIViewMixin(PhonesAPIViewMixin):
    kwargs: request.QueryDict

    def get_phone_id(self) -> int:
        return self.kwargs.get(config.PHONE_PK_URL_FIELD)


class PhoneCreateAPIViewMixin(PhonesPOSTAPIViewMixin):
    request: request.HttpRequest

    def get_201_response(self, data: dict = None):
        return self._response_class(
            data=data,
            status=status.HTTP_201_CREATED
        )


class PhonesListAPIViewMixin(PhonesAPIViewMixin):
    request: request.HttpRequest

    def get_request_limit(self):
        limit = self.request.GET.get(config.PHONES_LIMIT_QUERY_FIELD, None)

        if limit is not None and int(limit) > 0:
            limit = int(limit)
        else:
            limit = None

        return limit


class BasePhoneViewSetMixin(PhonesListAPIViewMixin,
                            PhoneCreateAPIViewMixin,
                            PhoneRetrieveAPIViewMixin,
                            PhonesAPIViewMixin):
    pass
