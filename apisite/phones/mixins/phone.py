from django.http import request

from phones import serializers, config, repositories
from . import base


class PhonesAPIViewMixin(base.ModelAPIViewMixin):
    serializer_class = serializers.PhoneSerializer
    pk_url_kwarg = config.PHONE_PK_URL_FIELD
    _repository: repositories.PhonesRepository = repositories.PhonesRepository()


class PhonesListAPIViewMixin(PhonesAPIViewMixin):
    request: request.HttpRequest

    def get_request_limit(self):
        limit = self.request.GET.get(config.PHONES_LIMIT_QUERY_FIELD, None)

        if limit is not None and int(limit) > 0:
            limit = int(limit)
        else:
            limit = None

        return limit


class BasePhoneViewSetMixin(PhonesListAPIViewMixin):
    pass
