from .human_like_enemy import HumanLikeEnemy
from items.weapon.fists import Fists
from items.weapon.mace import TwoHandedMace


class Troll(HumanLikeEnemy):
    def __init__(self, level, main_menu, language):
        super().__init__(level, main_menu, language)
        self.stats.NAME = self._text.TROLL
        self._equipped_weapon = Fists(self.stats.LEVEL, main_menu)
        self.stats.DAMAGE_MULTIPLIER = 3
        self.stats.HEALTH_LEVEL_MULTIPLIER = 25
        self.stats.EXPERIENCE_GAINED = 100
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()


class ArmedTroll(Troll):
    def __init__(self, level, main_menu, language):
        super().__init__(level, main_menu, language)
        self.stats.NAME = self._text.ARMED_TROLL
        self._equipped_weapon = TwoHandedMace(self.stats.LEVEL, self._main_menu)
        self.stats.EXPERIENCE_GAINED = 1000
        self.drops.set_drop_rate("TwoHandedMace", 0.5)
        self._calculate_damage()
        self._calculate_experience_gained()
