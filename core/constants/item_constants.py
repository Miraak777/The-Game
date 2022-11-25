from dataclasses import dataclass


@dataclass(frozen=True)
class ItemTypes:
    WEAPON: str = "weapon"
    CONSUMABLE: str = "consumable"
    FOOD: str = "food"


@dataclass(frozen=True)
class StatNames:
    WEAPON_TYPE: str = "weapon_type"
    NAMES: str = "names"
    STATS: str = "stats"
    ICON: str = "icon"
    MAX_DAMAGE: str = "max_damage"
    MIN_DAMAGE: str = "min_damage"
    ACCURACY: str = "accuracy"
    CRITICAL_STRIKE_CHANCE: str = "critical_strike_chance"
    BASE_STAMINA_CONSUMPTION: str = "base_stamina_consumption"
    CONSUMABLE_TYPE: str = "consumable_type"
    RESTORE_VALUE: str = "restore_value"
    MIN_LEVEL: str = "min_level"
    RARITY: str = "rarity"
