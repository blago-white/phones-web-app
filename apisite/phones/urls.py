from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import viewsets

router = DefaultRouter()
router.register(prefix="", viewset=viewsets.PhoneViewSet, basename="phone")
router.register(prefix="card", viewset=viewsets.PhoneCardViewSet, basename="card")

urlpatterns = [
    path("phones/", viewsets.PhoneViewSet.as_view({"get": "get_all"}), name="phone-list"),
    path("phone/<int:pk>/cards/", viewsets.PhoneCardViewSet.as_view({"get": "get_all"}), name="phone-cards-list"),
    path("phone/", include(router.urls), name="phone")
]
