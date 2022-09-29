from enemies.enemy import Enemy
from items.weapon.fists import Fists


class HumanLikeEnemy(Enemy):
    def __init__(self, level, game_menu, language):
        super().__init__(level, game_menu, language)
        self._equipped_weapon = Fists()

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
                self._equipped_weapon.MAX_DAMAGE *
                (1 + self.level / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )
        self.stats.MIN_DAMAGE = (
                self._equipped_weapon.MIN_DAMAGE *
                (1 + self.level / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )
