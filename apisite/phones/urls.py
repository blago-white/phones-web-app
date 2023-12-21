from django.urls import path, include

from . import routers
from .views import viewsets


urlpatterns = [
    path("phones/", viewsets.PhoneViewSet.as_view({"get": "get_all"}), name="phone-list"),
    path("phone/<int:pk>/cards/", viewsets.PhoneCardViewSet.as_view({"get": "get_all"}), name="phone-cards-list"),
    path("phone/", include(routers.phone_router.urls), name="phone"),
    path("brands/", viewsets.BrandViewSet.as_view({"get": "get_all"}), name="brand-list"),
    path("brand/", include(routers.brand_router.urls), name="brands")
]
