from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


__all__ = ["JWTAuthAPIView"]


class JWTAuthAPIView:
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticatedOrReadOnly, )
