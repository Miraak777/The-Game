from dataclasses import dataclass


@dataclass(frozen=True)
class MainStatsNames:
    NAME: str = "character_name"
    LEVEL: str = "level"
    CLASS: str = "class"


@dataclass(frozen=True)
class AttributesNames:
    STRENGTH: str = "strength"
    AGILITY: str = "agility"
    VITALITY: str = "vitality"
    ENDURANCE: str = "endurance"
    ATTRIBUTE_POINTS: str = "attribute_points"


@dataclass(frozen=True)
class BarsNames:
    HEALTH: str = "health"
    STAMINA: str = "stamina"


@dataclass(frozen=True)
class CombatStats:
    MIN_DAMAGE = "min_damage"
    MAX_DAMAGE = "max_damage"
    CRITICAL_STRIKE_CHANCE = "critical_strike_chance"
    CRITICAL_STRIKE_MULTIPLIER = "critical_strike_multiplier"
    ACCURACY = "accuracy"


@dataclass(frozen=True)
class Classes:
    PEASANT = "peasant"
    WARRIOR = "warrior"
    ASSASSIN = "assassin"
