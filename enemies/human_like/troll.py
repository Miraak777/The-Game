from .human_like_enemy import HumanLikeEnemy
from items.weapon.fists import Fists
from items.weapon.mace import TwoHandedMace


class Troll(HumanLikeEnemy):
    def __init__(self, level):
        super().__init__(level)
        self._stats.NAME = "troll"
        self._equipped_weapon = Fists()
        self._stats.DAMAGE_MULTIPLIER = 3
        self._calculate_damage()
        self._stats.HEALTH_LEVEL_MULTIPLIER = 25
        self._calculate_health()


class ArmedTroll(Troll):
    def __init__(self, level):
        super().__init__(level)
        self._stats.NAME = "armed_troll"
        self._equipped_weapon = TwoHandedMace()
        self._calculate_damage()
