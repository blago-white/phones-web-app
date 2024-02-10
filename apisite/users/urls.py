from django.urls import path, include

from users.routers import registration_router


urlpatterns = [
    path("register/", include(registration_router.urls), name="register"),
]
