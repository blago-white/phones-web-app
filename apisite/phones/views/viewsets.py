from phones import config, mixins
from . import _base


class PhoneViewSet(mixins.BasePhoneViewSetMixin, _base.DefaultModelViewSet):
    pass


class PhoneCardViewSet(mixins.BasePhoneCardViewSetMixin,
                       _base.DefaultTroughModelViewSet):
    trough_pk_url_kwarg = config.PHONE_POSITION_PK_URL_FIELD


class BrandViewSet(mixins.BaseBrandViewSetMixin, _base.DefaultModelViewSet):
    lookup_url_kwarg = "title"
    lookup_field = "title"
