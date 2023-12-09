from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import viewsets


router = DefaultRouter()
router.register(prefix="", viewset=viewsets.PhoneViewSet, basename="phone")

urlpatterns = [
    path("phones/", viewsets.PhoneViewSet.as_view({"get": "get_all"}), name="phone-list"),
    path("phone/", include(router.urls), name="phone")
]
