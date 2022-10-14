from dataclasses import dataclass


@dataclass(frozen=True)
class ItemTypes:
    WEAPON: str = "weapon"
