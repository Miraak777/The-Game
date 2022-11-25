from dataclasses import dataclass

from core.constants.character_constants import Classes


@dataclass(frozen=True)
class PeasantClass:
    CLASS_NAME: float = Classes.PEASANT
    HEALTH_MULTIPLIER: float = 1
    STAMINA_MULTIPLIER: float = 1
    AGILITY_DAMAGE_MULTIPLIER: float = 0
    STRENGTH_DAMAGE_MULTIPLIER: float = 2
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 1
    CRITICAL_DAMAGE_MULTIPLIER: float = 1.5


@dataclass(frozen=True)
class WarriorClass:
    CLASS_NAME: float = Classes.WARRIOR
    HEALTH_MULTIPLIER: float = 1.5
    STAMINA_MULTIPLIER: float = 1.1
    AGILITY_DAMAGE_MULTIPLIER: float = 0
    STRENGTH_DAMAGE_MULTIPLIER: float = 2
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 0.5
    CRITICAL_DAMAGE_MULTIPLIER: float = 1.5


@dataclass(frozen=True)
class AssassinClass:
    CLASS_NAME: float = Classes.ASSASSIN
    HEALTH_MULTIPLIER: float = 1
    STAMINA_MULTIPLIER: float = 1.5
    AGILITY_DAMAGE_MULTIPLIER: float = 1
    STRENGTH_DAMAGE_MULTIPLIER: float = 2
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 3
    CRITICAL_DAMAGE_MULTIPLIER: float = 2.5
