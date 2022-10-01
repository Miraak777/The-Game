from random import random

from core.constants.weapon_names import WeaponNames as wn
from core.items.weapon import Dagger, Sword

from .human_like_enemy import HumanLikeEnemy


class Human(HumanLikeEnemy):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN
        self.stats.EXPERIENCE_GAINED = 50
        if random() < 0.5:
            self.stats.HEALTH_LEVEL_MULTIPLIER = 40
            self.stats.DAMAGE_MULTIPLIER = 1.15
        else:
            self.stats.HEALTH_LEVEL_MULTIPLIER = 25
            self.stats.DAMAGE_MULTIPLIER = 1.3
        self._calculate_experience_gained()
        self._calculate_health()
        self._calculate_damage()


class HumanWithDagger(Human):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN_WITH_DAGGER
        self.stats.EXPERIENCE_GAINED = 70
        self._equipped_weapon = Dagger(self.stats.LEVEL, main_menu=self._main_menu)
        self.drops.set_drop_rate(wn.DAGGER, 1)
        self._calculate_damage()
        self._calculate_experience_gained()


class HumanWithSword(Human):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN_WITH_SWORD
        self.stats.EXPERIENCE_GAINED = 100
        self._equipped_weapon = Sword(self.stats.LEVEL, main_menu=self._main_menu)
        self.drops.set_drop_rate(wn.SWORD, 1)
        self._calculate_damage()
        self._calculate_experience_gained()
