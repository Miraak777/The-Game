from core.constants.weapon_names import WeaponNames as wn
from core.items.weapon import TwoHandedMace

from .human_like_enemy import HumanLikeEnemy


class Troll(HumanLikeEnemy):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.TROLL
        self.stats.VITALITY_PER_LEVEL = 2
        self.stats.STRENGTH_PER_LEVEL = 2
        self.stats.EXPERIENCE_GAINED = 100
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()


class ArmedTroll(Troll):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self.stats.NAME = self._text.ARMED_TROLL
        self._equipped_weapon = TwoHandedMace(self.stats.LEVEL, self._main_menu)
        self.stats.EXPERIENCE_GAINED = 300
        self.drops.set_drop_rate(wn.TWO_HANDED_MACE, 0.3)
        self._calculate_damage()
        self._calculate_experience_gained()
