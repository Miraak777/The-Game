from .human_like_enemy import HumanLikeEnemy
from items.weapon.dagger import Dagger


class Goblin(HumanLikeEnemy):
    def __init__(self, level, main_menu, language):
        super().__init__(level, main_menu, language)
        self.stats.NAME = self._text.GOBLIN
        self._equipped_weapon = Dagger(self.stats.LEVEL, self._main_menu)
        self.stats.HEALTH_LEVEL_MULTIPLIER = 5
        self.stats.EXPERIENCE_GAINED = 50
        self.drops.set_drop_rate("Dagger", 0.5)
        self._calculate_damage()
        self._calculate_health()
        self._calculate_experience_gained()

