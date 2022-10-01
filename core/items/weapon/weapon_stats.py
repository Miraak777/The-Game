from dataclasses import dataclass


@dataclass
class WeaponStats:
    NAME: str = "No Name"
    TWO_HANDED: bool = None
    MIN_DAMAGE: int = 0
    MAX_DAMAGE: int = 0
    CRITICAL_STRIKE_CHANCE: float = 0.025
    ACCURACY: float = 1
    STAMINA_CONSUMPTION_MULTIPLIER: float = 1
    ARMOUR_PENETRATION: float = 0
    LEVEL: int = 0
    LEVEL_DAMAGE_MULTIPLIER: float = 0.3
