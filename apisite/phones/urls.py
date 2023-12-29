from django.urls import path, include

from . import routers, config
from .views import viewsets

urlpatterns = [
    path("phones/", viewsets.PhoneViewSet.as_view({"get": "get_all"}), name="phone-list"),
    path("phone/", include(routers.phone_router.urls), name="phone"),
    path("brands/", viewsets.BrandViewSet.as_view({"get": "get_all"}), name="brand-list"),
    path("brand/", include(routers.brand_router.urls), name="brands"),
    path("phone/<int:pk>/cards/", viewsets.PhoneCardViewSet.as_view({"get": "get_all"}), name="phone-cards-list"),
    path("phone/<int:pk>/card/", viewsets.PhoneCardViewSet.as_view({"post": "create"}), name="card"),
    path(f"phone/<int:pk>/card/<int:{config.PHONE_POSITION_PK_URL_FIELD}>/",
         viewsets.PhoneCardViewSet.as_view(
             {"get": "retrieve", "put": "update", "patch": "update", "delete": "destroy"}
         ), name="card-options"),
]
