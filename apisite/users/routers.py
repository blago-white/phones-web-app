from rest_framework.routers import DefaultRouter

from users.viewsets import viewsets

__all__ = ["registration_router"]

registration_router = DefaultRouter()
registration_router.register(prefix="",
                             viewset=viewsets.UserRegistrationModelViewSet,
                             basename="register")
