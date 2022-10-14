from random import random

from core.constants.weapon_names import WeaponNames as wn, ConsumableNames as cn
from core.items.weapon import Dagger

from .human_like_enemy import HumanLikeEnemy


class Goblin(HumanLikeEnemy):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.GOBLIN
        self.stats.BASE_ENEMY_HEALTH = 10
        self.stats.VITALITY_HEALTH_MULTIPLIER = 10
        if random() < 0.5:
            self.stats.VITALITY_PER_LEVEL = 1
            self.stats.STRENGTH_PER_LEVEL = 1
        else:
            self.stats.VITALITY_PER_LEVEL = 0
            self.stats.STRENGTH_PER_LEVEL = 2
        self.stats.EXPERIENCE_GAINED = 25
        self.drops.set_drop_rate(cn.APPLE, 0.5)
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()


class GoblinWithDagger(Goblin):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.GOBLIN_WITH_DAGGER
        self._equipped_weapon = Dagger(self.stats.LEVEL, self._main_menu)
        self.stats.EXPERIENCE_GAINED = 50
        self.drops.set_drop_rate(wn.DAGGER, 0.3)
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()
