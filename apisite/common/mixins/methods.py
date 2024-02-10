BASE_HTTP_METHODS_NAMES = ["options", "trace", "head"]


class ReadOnlyAPIViewMixin:
    extra_http_method_names = BASE_HTTP_METHODS_NAMES + ["get"]


class WriteOnlyAPIViewMixin:
    extra_http_method_names = BASE_HTTP_METHODS_NAMES + [
        "post", "put", "delete"
    ]


class PostOnlyAPIViewMixin:
    extra_http_method_names = BASE_HTTP_METHODS_NAMES + ["post"]


class DeleteAPIViewMixin:
    extra_http_method_names = BASE_HTTP_METHODS_NAMES + ["delete"]


class UpdateAPIViewMixin:
    extra_http_method_names = BASE_HTTP_METHODS_NAMES + ["put"]
