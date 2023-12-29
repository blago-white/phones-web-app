from phones import serializers, repositories, config


class BrandAPIViewMixin:
    serializer_class = serializers.BrandSerializer
    pk_url_kwarg = config.BRAND_PK_URL_FIELD
    _repository = repositories.BrandRepository()


class BaseBrandViewSetMixin(BrandAPIViewMixin):
    pass
