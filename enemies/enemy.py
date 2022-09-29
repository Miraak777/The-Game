from .enemy_stats import Stats
from .texts import Text
import random


class Enemy:
    def __init__(self, level, game_menu, language):
        self.name: str = "No Name"
        self._text = Text[language]
        self.is_dead: bool = False
        self.level = level
        self._game_menu = game_menu
        self.stats = Stats()

    def attack(self) -> float:
        min_damage = self.stats.MIN_DAMAGE
        max_damage = self.stats.MAX_DAMAGE
        damage = round(random.uniform(min_damage, max_damage), 2)
        self._game_menu.add_log(self.name + " " + self._text.DEAL + " " + str(damage) + " " + self._text.DAMAGE)
        return damage

    def take_damage(self, damage: float) -> None:
        self.stats.HEALTH -= damage
        if self.stats.HEALTH < 0:
            self.stats.HEALTH = 0
        if damage != 0:
            self._game_menu.add_log(self.name + " " + self._text.TAKEN + " " + str(damage) + " " + self._text.DAMAGE + " " +
                                    str(self.stats.HEALTH) + "/" + str(self.stats.MAX_HEALTH))
        if self.stats.HEALTH == 0:
            self.is_dead = True
            self._game_menu.add_log(self.name + " " + self._text.DIED)

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = (
                self.stats.MAX_DAMAGE *
                (1 + self.level / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )
        self.stats.MIN_DAMAGE = (
                self.stats.MIN_DAMAGE *
                (1 + self.level / 10) *
                self.stats.DAMAGE_MULTIPLIER *
                self.stats.DIFFICULTY_MULTIPLIER
        )

    def _calculate_health(self):
        self.stats.MAX_HEALTH = self.stats.HEALTH_LEVEL_MULTIPLIER * self.level
        self.stats.HEALTH = self.stats.MAX_HEALTH
