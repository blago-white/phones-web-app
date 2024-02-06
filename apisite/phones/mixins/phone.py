from django.http.request import HttpRequest
from django.http.request import QueryDict

from phones import serializers, config, repositories
from users import config as users_config

from . import base


class PhonesAPIViewMixin(base.ModelAPIViewMixin):
    serializer_class = serializers.PhoneSerializer
    pk_url_kwarg = config.PHONE_PK_URL_FIELD
    _repository: repositories.PhonesRepository = repositories.PhonesRepository()


class PhonesListAPIViewMixin(PhonesAPIViewMixin):
    request: HttpRequest

    def get_all(self, *args, **kwargs):
        return self.get_200_response(
            data=self._repository.get_all(self.get_request_limit())
        )

    def get_request_limit(self):
        limit = self.request.GET.get(config.PHONES_LIMIT_QUERY_FIELD, None)

        if limit is not None and int(limit) > 0:
            limit = int(limit)
        else:
            limit = None

        return limit


class PhonesCreateApiView(PhonesAPIViewMixin):
    def get_request_data(self) -> dict:
        request_copy = self.request.POST.copy()

        request_copy.setdefault(
            key=users_config.DEFAULT_SERIALIZER_SELLER_FIELD_NAME,
            default=self.request.user
        )

        return request_copy


class BasePhoneViewSetMixin(PhonesListAPIViewMixin, PhonesCreateApiView):
    pass
