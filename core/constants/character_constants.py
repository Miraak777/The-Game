from dataclasses import dataclass


@dataclass(frozen=True)
class StatsNames:
    ATTRIBUTES: str = "attributes"
    MAIN_STATS: str = "main_stats"
    CLASS_MULTIPLIERS: str = "class_multipliers"
    EQUIPPED_WEAPON: str = "equipped_weapon"


@dataclass(frozen=True)
class MainStatsNames:
    NAME: str = "character_name"
    LEVEL: str = "level"
    MAX_EXPERIENCE: str = "max_experience"
    EXPERIENCE: str = "experience"
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
    MAX_HEALTH: str = "max_health"
    HEALTH: str = "health"
    MAX_STAMINA: str = "max_stamina"
    STAMINA: str = "stamina"


@dataclass(frozen=True)
class CombatStatsNames:
    MIN_DAMAGE: str = "min_damage"
    MAX_DAMAGE: str = "max_damage"
    CRITICAL_STRIKE_CHANCE: str = "critical_strike_chance"
    CRITICAL_STRIKE_MULTIPLIER: str = "critical_strike_multiplier"
    ACCURACY: str = "accuracy"


@dataclass(frozen=True)
class Classes:
    PEASANT: str = "peasant"
    WARRIOR: str = "warrior"
    ASSASSIN: str = "assassin"
