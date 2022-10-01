from .base_weapon import BaseWeapon
from .texts import Text


class BattleAxe(BaseWeapon):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].BATTLE_AXE
        self.stats.TWO_HANDED = False
        self.stats.MIN_DAMAGE = 7
        self.stats.MAX_DAMAGE = 14
        self.stats.ACCURACY = 0.8
        self.stats.STAMINA_CONSUMPTION = 6
        self.stats.ARMOUR_PENETRATION = 0.2
        self._calculate_damage()


class TwoHandedBattleAxe(BattleAxe):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].TWO_HANDED_BATTLE_AXE
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 10
        self.stats.MAX_DAMAGE = 20
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 9
        self._calculate_damage()


class DualBattleAxes(BattleAxe):
    def __init__(self, level, main_menu):
        super().__init__(level=level, main_menu=main_menu)
        self.stats.NAME = Text[self._language].DUAL_BATTLE_AXES
        self.stats.TWO_HANDED = True
        self.stats.MIN_DAMAGE = 14
        self.stats.MAX_DAMAGE = 28
        self.stats.ACCURACY = 0.6
        self.stats.STAMINA_CONSUMPTION = 1.6
        self._calculate_damage()
