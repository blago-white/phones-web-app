from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from common import mixins as common_mixins
from phones import repositories, mixins, config

__all__ = ('PhonesListAPIView', 'PhoneCreateAPIView', 'PhoneRetrieveAPIView')


class PhonesListAPIView(common_mixins.ReadOnlyAPIViewMixin, mixins.PhonesListAPIViewMixin, ListAPIView):
    _repository: repositories.PhonesRepository

    def get(self, request, *args, **kwargs):
        return self.get_200_response(data=self._repository.get_all(self.get_request_limit()))

    def get_view_description(self, html=False):
        return (f"This view returns all phones, to limit the "
                f"count of objects use '{config.PHONES_LIMIT_QUERY_FIELD}' query arg")


class PhoneRetrieveAPIView(common_mixins.ReadOnlyAPIViewMixin,
                           mixins.PhoneRetrieveAPIViewMixin,
                           RetrieveAPIView):
    _repository: repositories.PhonesRepository

    def get(self, request, *args, **kwargs):
        phone_id = self.get_phone_id()
        return self.get_200_response(data=self._repository.get(pk=phone_id))


class PhoneCreateAPIView(common_mixins.PostOnlyAPIViewMixin,
                         mixins.PhoneCreateAPIViewMixin,
                         CreateAPIView):
    _repository: repositories.PhonesRepository

    def post(self, request, *args, **kwargs):
        request_data = self.get_request_data()
        return self.get_201_response(data=self._repository.create(data=request_data))


class PhoneDeleteAPIView(common_mixins.DeleteAPIViewMixin,
                         mixins.PhoneRetrieveAPIViewMixin,
                         DestroyAPIView):
    _repository: repositories.PhonesRepository

    def post(self, request, *args, **kwargs):
        self._repository.delete(pk=self.get_phone_id())

        return self.get_200_response()


class PhoneUpdateAPIView(common_mixins.UpdateAPIViewMixin,
                         mixins.PhoneRetrieveAPIViewMixin,
                         UpdateAPIView):
    _repository: repositories.PhonesRepository

    def put(self, request, *args, **kwargs):
        return self.get_200_response(
            data=self._repository.update(pk=self.get_phone_id(), data=self.request.POST)
        )
