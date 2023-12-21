from phones import serializers, repositories, config
from . import base


class PhoneCardAPIViewMixin(base.ModelAPIViewMixin):
    serializer_class = serializers.PhonePositionSerializer
    pk_url_kwarg = config.PHONE_PK_URL_FIELD
    _repository = repositories.PhonesCardRepository()


class BasePhoneCardViewSetMixin(PhoneCardAPIViewMixin, base.APIViewSetMixin):
    pass
