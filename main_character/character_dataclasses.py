from dataclasses import dataclass


@dataclass
class Parameters:
    LEVEL: int = 0
    PARAMETERS_POINTS: int = 0
    ENDURANCE: int = 0
    STRENGTH: int = 0
    VITALITY: int = 0
    AGILITY: int = 0


@dataclass
class ClassMultipliers:
    HEALTH_MULTIPLIER: float = 1
    STAMINA_MULTIPLIER: float = 1
    AGILITY_DAMAGE_MULTIPLIER: float = 0.75
    STRENGTH_DAMAGE_MULTIPLIER: float = 0.75
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 1


@dataclass
class Stats:
    MAX_HEALTH: float = 0
    HEALTH: float = 0
    MAX_STAMINA: float = 0
    STAMINA: float = 0
    MIN_DAMAGE: float = 0
    MAX_DAMAGE: float = 0
    CRITICAL_STRIKE_CHANCE: float = 0
    CRITICAL_STRIKE_MULTIPLIER: float = 0
    ACCURACY: float = 0
