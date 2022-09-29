from .human_like_enemy import HumanLikeEnemy
from items.weapon.dagger import Dagger


class Goblin(HumanLikeEnemy):
    def __init__(self, level):
        super().__init__(level)
        self._stats.NAME = "goblin"
        self._equipped_weapon = Dagger()
        self._calculate_damage()
        self._stats.HEALTH_LEVEL_MULTIPLIER = 5
        self._calculate_health()

