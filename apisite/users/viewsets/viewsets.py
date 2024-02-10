from common.mixins.methods import PostOnlyAPIViewMixin
from common.viewsets.base import DefaultModelViewSet

from users.mixins import UserRegisterMixin


class UserRegistrationModelViewSet(UserRegisterMixin,
                                   PostOnlyAPIViewMixin,
                                   DefaultModelViewSet):
    pass
