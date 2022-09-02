from dataclasses import dataclass

@dataclass
class Fists:
    WEAPON_NAME: str = "Fists"
    MIN_DAMAGE: int = 1
    MAX_DAMAGE: int = 2
    CRITICAL_STRIKE_CHANCE: float = 0.05
    ACCURACY: int = 0.8
