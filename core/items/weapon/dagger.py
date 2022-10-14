from .base_weapon import BaseWeapon
from .texts import Text


class Dagger(BaseWeapon):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].DAGGER
        self.item_icon = "dagger.png"
        self.stats.TWO_HANDED = False
        self.stats.MIN_DAMAGE = 2
        self.stats.MAX_DAMAGE = 6
        self.stats.CRITICAL_STRIKE_CHANCE = 0.1
        self.stats.ACCURACY = 0.8
        self.stats.STAMINA_CONSUMPTION = 3
        self.stats.ARMOUR_PENETRATION = 0.5
        self._calculate_damage()


class DualDaggers(Dagger):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].DUAL_DAGGERS
        self.item_icon = "dual_daggers.png"
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 4
        self.stats.MAX_DAMAGE = 12
        self.stats.STAMINA_CONSUMPTION = 5
        self._calculate_damage()
