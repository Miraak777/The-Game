from .human_like_enemy import HumanLikeEnemy
from items.weapon.fists import Fists
from items.weapon.mace import TwoHandedMace


class Troll(HumanLikeEnemy):
    def __init__(self, level, game_menu, language):
        super().__init__(level, game_menu, language)
        self.name = self._text.TROLL
        self._equipped_weapon = Fists()
        self.stats.DAMAGE_MULTIPLIER = 3
        self._calculate_damage()
        self.stats.HEALTH_LEVEL_MULTIPLIER = 25
        self._calculate_health()


class ArmedTroll(Troll):
    def __init__(self, level, game_menu, language):
        super().__init__(level, game_menu, language)
        self.name = self._text.ARMED_TROLL
        self._equipped_weapon = TwoHandedMace()
        self._calculate_damage()
