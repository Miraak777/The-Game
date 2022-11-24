from dataclasses import dataclass


@dataclass(frozen=True)
class StatNames:
    NAMES: str = "names"
    STATS: str = "stats"
    WEAPON: str = "weapon"
    BASE_HEALTH: str = "base_health"
    STRENGTH_PER_LEVEL: str = "strength_per_level"
    VITALITY_PER_LEVEL: str = "vitality_per_level"
    STRENGTH_DAMAGE_MULTIPLIER: str = "strength_damage_multiplier"
    VITALITY_HEALTH_MULTIPLIER: str = "vitality_health_multiplier"
    EXPERIENCE_GAINED: str = "experience_gained"
