from core.enemies.enemy import Enemy
from core.items.weapon import Fists


class HumanLikeEnemy(Enemy):
    def __init__(self, level, main_menu):
        super().__init__(level, main_menu)
        self._equipped_weapon = Fists(self.stats.LEVEL, main_menu)
        self.stats.BASE_ENEMY_HEALTH = 15
        self._calculate_health()
        self._calculate_damage()

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
            self._equipped_weapon.stats.MAX_DAMAGE
            * (1 + self.stats.LEVEL / 10)
            * self.stats.DIFFICULTY_MULTIPLIER
            * (1 + self.stats.STRENGTH_PER_LEVEL * self.stats.LEVEL * self.stats.STRENGTH_DAMAGE_MULTIPLIER)
        )
        self.stats.MIN_DAMAGE = (
            self._equipped_weapon.stats.MIN_DAMAGE
            * (1 + self.stats.LEVEL / 10)
            * self.stats.DIFFICULTY_MULTIPLIER
            * (1 + self.stats.STRENGTH_PER_LEVEL * self.stats.LEVEL * self.stats.STRENGTH_DAMAGE_MULTIPLIER)
        )
