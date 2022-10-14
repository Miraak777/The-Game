from .base_weapon import BaseWeapon
from .texts import Text


class Mace(BaseWeapon):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].MACE
        self.item_icon = "mace.png"
        self.stats.TWO_HANDED = False
        self.stats.MIN_DAMAGE = 14
        self.stats.MAX_DAMAGE = 16
        self.stats.ACCURACY = 0.8
        self.stats.STAMINA_CONSUMPTION = 7
        self.stats.ARMOUR_PENETRATION = 0.4
        self._calculate_damage()


class TwoHandedMace(Mace):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].TWO_HANDED_MACE
        self.item_icon = "two_handed_mace.png"
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 18
        self.stats.MAX_DAMAGE = 22
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 11
        self._calculate_damage()


class DualMaces(Mace):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].DUAL_MACES
        self.item_icon = "dual_maces.png"
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 26
        self.stats.MAX_DAMAGE = 32
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 14
        self._calculate_damage()
