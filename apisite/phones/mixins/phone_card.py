from phones import serializers, repositories
from . import base


class PhoneCardAPIViewMixin(base.ModelAPIViewMixin):
    serializer_class = serializers.PhonePositionSerializer
    _repository: repositories.PhonesCardRepository = (
        repositories.PhonesCardRepository()
    )


class BasePhoneCardViewSetMixin(PhoneCardAPIViewMixin,
                                base.RetrieveAPIViewMixin,
                                base.CreateAPIViewMixin,):
    pass
