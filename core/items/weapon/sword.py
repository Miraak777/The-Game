from .base_weapon import BaseWeapon
from .texts import Text


class Sword(BaseWeapon):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].SWORD
        self.stats.TWO_HANDED = False
        self.stats.MIN_DAMAGE = 9
        self.stats.MAX_DAMAGE = 12
        self.stats.CRITICAL_STRIKE_CHANCE = 0.04
        self.stats.ACCURACY = 0.8
        self.stats.STAMINA_CONSUMPTION = 5
        self.stats.ARMOUR_PENETRATION = 0.1
        self._calculate_damage()


class TwoHandedSword(Sword):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].TWO_HANDED_SWORD
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 12
        self.stats.MAX_DAMAGE = 18
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 7
        self._calculate_damage()


class DualSwords(Sword):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].DUAL_SWORDS
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 18
        self.stats.MAX_DAMAGE = 24
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 8
        self._calculate_damage()
