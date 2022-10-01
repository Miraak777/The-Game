from core.enemies.enemy import Enemy
from core.items.weapon import Fists


class HumanLikeEnemy(Enemy):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self._equipped_weapon = Fists(self.stats.LEVEL, main_menu)

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
            self._equipped_weapon.stats.MAX_DAMAGE
            * (1 + self.stats.LEVEL / 10)
            * self.stats.DAMAGE_MULTIPLIER
            * self.stats.DIFFICULTY_MULTIPLIER
        )
        self.stats.MIN_DAMAGE = (
            self._equipped_weapon.stats.MIN_DAMAGE
            * (1 + self.stats.LEVEL / 10)
            * self.stats.DAMAGE_MULTIPLIER
            * self.stats.DIFFICULTY_MULTIPLIER
        )
