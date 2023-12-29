from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from phones import config, mixins
from . import _base


class PhoneViewSet(mixins.BasePhoneViewSetMixin,
                   _base.DefaultModelViewSet,
                   mixins.JWTAuthAPIView):
    pass


class PhoneCardViewSet(mixins.BasePhoneCardViewSetMixin,
                       _base.DefaultTroughModelViewSet,
                       mixins.JWTAuthAPIView):
    trough_pk_url_kwarg = config.PHONE_POSITION_PK_URL_FIELD


class BrandViewSet(mixins.BaseBrandViewSetMixin,
                   _base.DefaultModelViewSet,
                   mixins.JWTAuthAPIView):
    lookup_url_kwarg = "title"
    lookup_field = "title"
