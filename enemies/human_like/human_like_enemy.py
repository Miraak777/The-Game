from enemies.enemy import Enemy
from items.weapon.fists import Fists


class HumanLikeEnemy(Enemy):
    def __init__(self, level):
        super().__init__(level)
        self._equipped_weapon = Fists()

    def _calculate_damage(self):
        self._stats.MAX_DAMAGE = (
                self._equipped_weapon.MAX_DAMAGE *
                (1 + self._stats.LEVEL / 10) *
                self._stats.DAMAGE_MULTIPLIER *
                self._stats.DIFFICULTY_MULTIPLIER
        )
        self._stats.MIN_DAMAGE = (
                self._equipped_weapon.MIN_DAMAGE *
                (1 + self._stats.LEVEL / 10) *
                self._stats.DAMAGE_MULTIPLIER *
                self._stats.DIFFICULTY_MULTIPLIER
        )
