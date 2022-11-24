from random import random, uniform
from typing import List, Any, Dict
from core.constants.path_constants import Path, Paths
from yaml import safe_load
from core.common import get_enemy_stats
from core.constants.enemy_constants import StatNames
from core.items import Weapon, Consumable, get_weapon_table, get_consumables_table
from .texts import Text


class Enemy:
    def __init__(self, level: int, main_menu, enemy_file_name: str) -> None:
        self._main_menu = main_menu
        self.level = level
        self.game_menu = self._main_menu.game_menu
        self._text = Text[self._main_menu.language]
        stats = get_enemy_stats(enemy_file_name)

        self.difficulty_multiplier = 1
        self.is_dead = False
        self.name = stats[StatNames.NAMES][self._main_menu.language]
        self.weapon = Weapon(self._main_menu, self.level, stats[StatNames.WEAPON])
        self.base_health = stats[StatNames.STATS][StatNames.BASE_HEALTH]
        self.strength_per_level = stats[StatNames.STATS][StatNames.STRENGTH_PER_LEVEL]
        self.vitality_per_level = stats[StatNames.STATS][StatNames.VITALITY_PER_LEVEL]
        self.strength_damage_multiplier = stats[StatNames.STATS][StatNames.STRENGTH_DAMAGE_MULTIPLIER]
        self.vitality_health_multiplier = stats[StatNames.STATS][StatNames.VITALITY_HEALTH_MULTIPLIER]
        self.experience_gained = stats[StatNames.STATS][StatNames.EXPERIENCE_GAINED]
        self.weapon_drop_type = self.weapon.weapon_type

        self._calculate_health()
        self._calculate_damage()
        self._calculate_experience_gained()

    def attack(self) -> float:
        min_damage = self.min_damage
        max_damage = self.max_damage
        damage = round(uniform(min_damage, max_damage), 2)
        self.game_menu.add_log(f"{self.name} {self._text.DEAL} {str(damage)} {self._text.DAMAGE}")
        return damage

    def take_damage(self, damage: float) -> None:
        self.health = round(self.health - damage, 2)
        self.game_menu.add_log(self.name + self._text.RECEIVED + str(damage) + self._text.RECEIVED_DAMAGE)

        if self.health < 0:
            self.health = 0
        if damage != 0:
            self.game_menu.refresh_enemy_bar(self)
        if self.health == 0:
            self.is_dead = True
            self.game_menu.add_log(f"{self.name} {self._text.DIED}")

    def calculate_drop(self) -> List[Any]:
        dropped = []
        consumables_table = get_consumables_table()
        weapon_table = [weapon_file_name for weapon_file_name, weapon_type in get_weapon_table().items() if
                        weapon_type == self.weapon_drop_type]
        for consumable in consumables_table:
            if random() < 0.2:
                dropped.append(Consumable(self._main_menu, consumable))
        for weapon in weapon_table:
            if random() < 0.2:
                dropped.append(Weapon(self._main_menu, self.level, weapon))
                break
        return dropped

    def _calculate_damage(self) -> None:
        self.max_damage = (
                self.weapon.max_damage
                * (1 + self.level / 10)
                * self.difficulty_multiplier
                * (1 + self.strength_per_level * self.level * self.strength_damage_multiplier)
        )
        self.min_damage = (
                self.weapon.min_damage
                * (1 + self.level / 10)
                * self.difficulty_multiplier
                * (1 + self.strength_per_level * self.level * self.strength_damage_multiplier)
        )

    def _calculate_health(self) -> None:
        self.max_health = (
                                  self.base_health * self.level + self.vitality_per_level * self.level *
                                  self.vitality_health_multiplier
                          ) * self.difficulty_multiplier
        self.health = self.max_health

    def _calculate_experience_gained(self):
        self.experience_gained *= 1 + self.level * 0.5

    @staticmethod
    def get_enemy_stats(enemy_file_name: str) -> Dict[str, Any]:
        with open(str(Path(Paths.PATH_TO_ENEMIES, enemy_file_name)), "r") as enemy_file:
            stats = safe_load(enemy_file)
            return stats
