from .enemy_stats import Stats
from .texts import Text
from .drop_rates import BaseDropRate
import random


class Enemy:
    def __init__(self, level, main_menu, language):
        self.stats = Stats()
        self.drops = BaseDropRate()
        self._text = Text[language]
        self.stats.LEVEL = level
        self._main_menu = main_menu
        self._game_menu = self._main_menu.game_menu

    def attack(self) -> float:
        min_damage = self.stats.MIN_DAMAGE
        max_damage = self.stats.MAX_DAMAGE
        damage = round(random.uniform(min_damage, max_damage), 2)
        self._game_menu.add_log(self.stats.NAME + " " + self._text.DEAL + " " + str(damage) + " " + self._text.DAMAGE)
        return damage

    def take_damage(self, damage: float) -> None:
        self.stats.HEALTH -= damage
        if self.stats.HEALTH < 0:
            self.stats.HEALTH = 0
        if damage != 0:
            self._game_menu.add_log(self.stats.NAME + " " + self._text.TAKEN + " " + str(damage) + " " + self._text.DAMAGE + " " +
                                    str(self.stats.HEALTH) + "/" + str(self.stats.MAX_HEALTH))
        if self.stats.HEALTH == 0:
            self.stats.IS_DEAD = True
            self._game_menu.add_log(self.stats.NAME + " " + self._text.DIED)

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
                self.stats.MAX_DAMAGE *
                (1 + self.stats.LEVEL / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )
        self.stats.MIN_DAMAGE = (
                self.stats.MIN_DAMAGE *
                (1 + self.stats.LEVEL / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )

    def _calculate_health(self):
        self.stats.MAX_HEALTH = self.stats.HEALTH_LEVEL_MULTIPLIER * self.stats.LEVEL
        self.stats.HEALTH = self.stats.MAX_HEALTH

    def _calculate_experience_gained(self):
        self.stats.EXPERIENCE_GAINED *= self.stats.LEVEL