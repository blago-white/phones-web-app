from rest_framework.routers import DefaultRouter

from .views import viewsets

__all__ = ["phone_router", "brand_router"]


phone_router = DefaultRouter()
phone_router.register(prefix="", viewset=viewsets.PhoneViewSet, basename="phone")

phone_card_router = DefaultRouter()
phone_card_router.register(prefix="", viewset=viewsets.PhoneCardViewSet, basename="")

brand_router = DefaultRouter()
brand_router.register(prefix="", viewset=viewsets.BrandViewSet, basename="brand")
