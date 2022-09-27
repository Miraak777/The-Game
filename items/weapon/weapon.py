from dataclasses import dataclass


@dataclass
class Weapon:
    WEAPON_NAME: str
    TWO_HANDED: bool
    MIN_DAMAGE: int
    MAX_DAMAGE: int
    CRITICAL_STRIKE_CHANCE: float
    ACCURACY: float
    STAMINA_CONSUMPTION_MULTIPLIER: float
    ARMOUR_PENETRATION: float