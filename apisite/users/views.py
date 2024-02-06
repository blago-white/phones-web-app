from rest_framework.generics import CreateAPIView
from common.mixins import PostOnlyAPIViewMixin


class UserRegistrationApiView(PostOnlyAPIViewMixin, CreateAPIView):
    def post(self, request, *args, **kwargs):
        pass
