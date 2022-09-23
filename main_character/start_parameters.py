from core.constants.character_constants import Classes as c


class MainStats:
    NAME: str = None
    LEVEL: int = 1
    MAX_EXPERIENCE: int = 100
    EXPERIENCE: int = 0
    CLASS: str = c.PEASANT


class Attributes:
    ATTRIBUTE_POINTS: int = 3
    ENDURANCE: int = 0
    STRENGTH: int = 0
    VITALITY: int = 0
    AGILITY: int = 0


class Bars:
    MAX_HEALTH: float = 5
    HEALTH: float = 0
    MAX_STAMINA: float = 2.5
    STAMINA: float = 0


class CombatStats:
    MIN_DAMAGE: float = 0
    MAX_DAMAGE: float = 0
    CRITICAL_STRIKE_CHANCE: float = 0
    CRITICAL_STRIKE_MULTIPLIER: float = 0
    ACCURACY: float = 0


class ClassMultipliers:
    HEALTH_MULTIPLIER: float = 1
    STAMINA_MULTIPLIER: float = 1
    AGILITY_DAMAGE_MULTIPLIER: float = 0.5
    STRENGTH_DAMAGE_MULTIPLIER: float = 0.5
    CRITICAL_STRIKE_CHANCE_MULTIPLIER: float = 1
