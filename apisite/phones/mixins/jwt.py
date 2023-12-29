from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

__all__ = ["JWTAuthAPIView"]


class JWTAuthAPIView:
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
