from phones import serializers, repositories, config
from common.mixins import api
from .authority import CheckAuthorityViewSetMixin


class PhoneCardAPIViewMixin(api.ModelAPIViewMixin):
    serializer_class = serializers.PhonePositionSerializer
    pk_url_kwarg = config.PHONE_PK_URL_FIELD
    _repository = repositories.PhonesCardRepository()


class BasePhoneCardViewSetMixin(CheckAuthorityViewSetMixin,
                                PhoneCardAPIViewMixin,
                                api.APIViewSetMixin):
    product_pk_url_kwarg = config.PHONE_POSITION_PK_URL_FIELD
