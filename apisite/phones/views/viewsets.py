from django.http import HttpRequest

from phones import config, mixins
from jwt_auth.mixins import jwt

from common.viewsets import base


class PhoneViewSet(mixins.BasePhoneViewSetMixin,
                   jwt.JWTAuthAPIViewMixin,
                   base.DefaultModelViewSet):
    pass


class PhoneCardViewSet(mixins.BasePhoneCardViewSetMixin,
                       jwt.JWTAuthAPIViewMixin,
                       base.DefaultTroughModelViewSet):
    trough_pk_url_kwarg = config.PHONE_POSITION_PK_URL_FIELD


class BrandViewSet(mixins.BaseBrandViewSetMixin,
                   jwt.JWTAuthAPIViewMixin,
                   base.DefaultModelViewSet):
    lookup_url_kwarg = lookup_field = config.BRAND_PK_URL_FIELD
