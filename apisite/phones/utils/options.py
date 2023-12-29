from dataclasses import dataclass


@dataclass(frozen=True)
class CardOptions:
    color: str
    storage: int

    @property
    def as_dict(self) -> dict:
        return dict(
            color=self.color,
            storage=self.storage
        )
