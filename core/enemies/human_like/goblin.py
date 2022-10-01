from random import random

from core.constants.weapon_names import WeaponNames as wn
from core.items.weapon import Dagger

from .human_like_enemy import HumanLikeEnemy


class Goblin(HumanLikeEnemy):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.GOBLIN
        if random() < 0.5:
            self.stats.HEALTH_LEVEL_MULTIPLIER = 12.5
            self.stats.DAMAGE_MULTIPLIER = 0.9
        else:
            self.stats.HEALTH_LEVEL_MULTIPLIER = 7.5
            self.stats.DAMAGE_MULTIPLIER = 1.05
        self.stats.EXPERIENCE_GAINED = 25
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()


class GoblinWithDagger(Goblin):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.GOBLIN_WITH_DAGGER
        self._equipped_weapon = Dagger(self.stats.LEVEL, self._main_menu)
        self.stats.EXPERIENCE_GAINED = 50
        self.drops.set_drop_rate(wn.DAGGER, 1)
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()
