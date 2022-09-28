from .enemy_stats import Stats
import random


class Enemy:
    def __init__(self):
        self._stats = Stats()

    def deal_damage(self) -> float:
        min_damage = self._stats.MIN_DAMAGE
        max_damage = self._stats.MAX_DAMAGE
        return round(random.uniform(min_damage, max_damage), 2)

    def take_damage(self, damage: float) -> None:
        self._stats.HEALTH -= damage
        if self._stats.HEALTH <= 0:
            self._stats.IS_DEAD = True
