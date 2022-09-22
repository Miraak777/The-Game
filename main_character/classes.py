from dataclasses import dataclass


@dataclass(frozen=True)
class PeasantClass:
    HEALTH_MULTIPLIER: float = 1
    STAMINA_MULTIPLIER: float = 1
    AGILITY_DAMAGE_MULTIPLIER: float = 0.5
    STRENGTH_DAMAGE_MULTIPLIER: float = 0.5
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 1


@dataclass(frozen=True)
class WarriorClass:
    HEALTH_MULTIPLIER: float = 2
    STAMINA_MULTIPLIER: float = 1
    AGILITY_DAMAGE_MULTIPLIER: float = 0
    STRENGTH_DAMAGE_MULTIPLIER: float = 1
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 0.5


@dataclass(frozen=True)
class AssassinClass:
    HEALTH_MULTIPLIER: float = 0.7
    STAMINA_MULTIPLIER: float = 1.5
    AGILITY_DAMAGE_MULTIPLIER: float = 1
    STRENGTH_DAMAGE_MULTIPLIER: float = 0
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 2
