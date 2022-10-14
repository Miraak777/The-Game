from random import random

from core.constants.weapon_names import WeaponNames as wn
from core.items.weapon import Dagger, Sword, TwoHandedSword

from .human_like_enemy import HumanLikeEnemy


class Human(HumanLikeEnemy):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN
        self.stats.EXPERIENCE_GAINED = 50
        if random() < 0.5:
            self.stats.VITALITY_PER_LEVEL = 2
            self.stats.STRENGTH_PER_LEVEL = 1
        else:
            self.stats.VITALITY_PER_LEVEL = 1
            self.stats.STRENGTH_PER_LEVEL = 2
        self._calculate_experience_gained()
        self._calculate_health()
        self._calculate_damage()


class HumanWithDagger(Human):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN_WITH_DAGGER
        self.stats.EXPERIENCE_GAINED = 70
        self._equipped_weapon = Dagger(self.stats.LEVEL, main_menu=self._main_menu)
        self.drops.set_drop_rate(wn.DAGGER, 0.3)
        self._calculate_damage()
        self._calculate_experience_gained()


class HumanWithSword(Human):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN_WITH_SWORD
        self.stats.EXPERIENCE_GAINED = 100
        self._equipped_weapon = Sword(self.stats.LEVEL, main_menu=self._main_menu)
        self.drops.set_drop_rate(wn.SWORD, 0.3)
        self._calculate_damage()
        self._calculate_experience_gained()


class HumanWithTwoHandedSword(Human):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = self._text.HUMAN_WITH_TWO_HANDED_SWORD
        self.stats.EXPERIENCE_GAINED = 150
        self._equipped_weapon = TwoHandedSword(self.stats.LEVEL, main_menu=self._main_menu)
        self.drops.set_drop_rate(wn.TWO_HANDED_SWORD, 0.3)
        self._calculate_damage()
        self._calculate_experience_gained()
