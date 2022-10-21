import random

from .drop_rates import BaseDropRate
from .enemy_stats import Stats
from .texts import Text


class Enemy:
    def __init__(self, level, main_menu):
        self._main_menu = main_menu
        self._game_menu = self._main_menu.game_menu
        self.stats = Stats()
        self.drops = BaseDropRate()
        self._text = Text[self._main_menu.language]
        self.stats.LEVEL = level

    def attack(self) -> float:
        min_damage = self.stats.MIN_DAMAGE
        max_damage = self.stats.MAX_DAMAGE
        damage = round(random.uniform(min_damage, max_damage), 2)
        self._game_menu.add_log(self.stats.NAME + " " + self._text.DEAL + " " + str(damage) + " " + self._text.DAMAGE)
        return damage

    def take_damage(self, damage: float) -> None:
        self.stats.HEALTH = round(self.stats.HEALTH - damage, 2)

        if self.stats.HEALTH < 0:
            self.stats.HEALTH = 0
        if damage != 0:
            self._game_menu.refresh_enemy_bar(self)
        if self.stats.HEALTH == 0:
            self.stats.IS_DEAD = True
            self._game_menu.add_log(self.stats.NAME + " " + self._text.DIED)

    def set_name(self, name: str):
        self.stats.NAME = name

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
            self.stats.MAX_DAMAGE
            * self.stats.DIFFICULTY_MULTIPLIER
            * (1 + self.stats.STRENGTH_PER_LEVEL * self.stats.LEVEL * self.stats.STRENGTH_DAMAGE_MULTIPLIER)
        )
        self.stats.MIN_DAMAGE = self.stats.MIN_DAMAGE * self.stats.DIFFICULTY_MULTIPLIER

    def _calculate_health(self):
        self.stats.MAX_HEALTH = (
            self.stats.BASE_ENEMY_HEALTH * self.stats.LEVEL + self.stats.VITALITY_PER_LEVEL * self.stats.LEVEL *
            self.stats.VITALITY_HEALTH_MULTIPLIER
        ) * self.stats.DIFFICULTY_MULTIPLIER
        self.stats.HEALTH = self.stats.MAX_HEALTH

    def _calculate_experience_gained(self):
        self.stats.EXPERIENCE_GAINED *= 1 + self.stats.LEVEL * 0.5
