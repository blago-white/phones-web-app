from common.services import base

__all__ = ["get_initial_card_options"]


def get_initial_card_options(service: base.BaseModelService,
                             phone_id: int) -> dict:
    return service.get_default_instance_options(phone_id=phone_id)
