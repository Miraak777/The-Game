from .human_like_enemy import HumanLikeEnemy
from items.weapon.dagger import Dagger


class Goblin(HumanLikeEnemy):
    def __init__(self, level, game_menu, language):
        super().__init__(level, game_menu, language)
        self.name = self._text.GOBLIN
        self._equipped_weapon = Dagger()
        self._calculate_damage()
        self.stats.HEALTH_LEVEL_MULTIPLIER = 5
        self._calculate_health()

