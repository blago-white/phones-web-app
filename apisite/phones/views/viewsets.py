from common import celery

from phones import config, mixins
from jwt_auth.mixins import jwt
from django.http import HttpResponse

from . import _base


class PhoneViewSet(mixins.BasePhoneViewSetMixin,
                   jwt.JWTAuthAPIViewMixin,
                   _base.DefaultModelViewSet):
    pass


class PhoneCardViewSet(mixins.BasePhoneCardViewSetMixin,
                       jwt.JWTAuthAPIViewMixin,
                       _base.DefaultTroughModelViewSet):
    trough_pk_url_kwarg = config.PHONE_POSITION_PK_URL_FIELD


class BrandViewSet(mixins.BaseBrandViewSetMixin,
                   jwt.JWTAuthAPIViewMixin,
                   _base.DefaultModelViewSet):
    lookup_url_kwarg = lookup_field = config.BRAND_PK_URL_FIELD
