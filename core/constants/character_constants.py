from dataclasses import dataclass


@dataclass(frozen=True)
class MainStatsNames:
    NAME: str = "Character Name"
    LEVEL: str = "Level"
    CLASS: str = "Class"


@dataclass(frozen=True)
class AttributesNames:
    ATTRIBUTES: str = "Attributes"
    STRENGTH: str = "Strength"
    AGILITY: str = "Agility"
    VITALITY: str = "Vitality"
    ENDURANCE: str = "Endurance"
    ATTRIBUTE_POINTS: str = "Attribute Points"


@dataclass(frozen=True)
class BarsNames:
    BARS: str = "Bars"
    HEALTH: str = "Health"
    STAMINA: str = "Stamina"


@dataclass(frozen=True)
class CombatStats:
    STATS: str = "Stats"
    DAMAGE: str = "Damage"
    MIN_DAMAGE: str = "min_damage"
    MAX_DAMAGE: str = "max_damage"
    CRITICAL_STRIKE_CHANCE: str = "Critical Strike Chance"
    CRITICAL_STRIKE_MULTIPLIER: str = "Critical Strike Multiplier"
    ACCURACY: str = "Accuracy"


@dataclass(frozen=True)
class Classes:
    PEASANT: str = "Peasant"
    WARRIOR: str = "Warrior"
    ASSASSIN: str = "Assassin"
