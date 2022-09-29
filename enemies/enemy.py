from .enemy_stats import Stats
import random


class Enemy:
    def __init__(self, level):
        self._stats = Stats()
        self._stats.LEVEL = level

    def deal_damage(self) -> float:
        min_damage = self._stats.MIN_DAMAGE
        max_damage = self._stats.MAX_DAMAGE
        return round(random.uniform(min_damage, max_damage), 2)

    def take_damage(self, damage: float) -> None:
        self._stats.HEALTH -= damage
        if self._stats.HEALTH <= 0:
            self._stats.IS_DEAD = True

    def _calculate_damage(self):
        self._stats.MAX_DAMAGE = (
                self._stats.MAX_DAMAGE *
                (1 + self._stats.LEVEL / 10) *
                self._stats.DAMAGE_MULTIPLIER *
                self._stats.DIFFICULTY_MULTIPLIER
        )
        self._stats.MIN_DAMAGE = (
                self._stats.MIN_DAMAGE *
                (1 + self._stats.LEVEL / 10) *
                self._stats.DAMAGE_MULTIPLIER *
                self._stats.DIFFICULTY_MULTIPLIER
        )

    def _calculate_health(self):
        self._stats.MAX_HEALTH = self._stats.HEALTH_LEVEL_MULTIPLIER * self._stats.LEVEL
