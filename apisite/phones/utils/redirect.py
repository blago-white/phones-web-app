from django.urls import reverse

from phones import config

__all__ = ["get_default_card_options_url", "get_default_card_url"]


def get_default_card_options_url(phone_id: int, phone_position_id: int) -> str:
    kwargs: dict = {config.PHONE_PK_URL_FIELD: phone_id} | {}

    return reverse("card-options", kwargs=kwargs)


def get_default_card_url(phone_id: int) -> str:
    return reverse("card", kwargs={config.PHONE_PK_URL_FIELD: phone_id})
