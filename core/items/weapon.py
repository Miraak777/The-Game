from typing import Any, Dict, List

from PyQt6.QtWidgets import QMainWindow
from yaml import safe_load

from core.constants.item_constants import ItemTypes, StatNames
from core.constants.path_constants import Path, Paths
from core.items.base_item import BaseItem


class Weapon(BaseItem):
    def __init__(self, main_menu: QMainWindow, level: int, weapon_file_name: str, rarity: float) -> None:
        super().__init__(main_menu)
        self.level = level
        self.rarity = rarity
        stats = self.get_weapon_stats(weapon_file_name)

        self._level_damage_multiplier = 0.15
        self.weapon_type = stats[StatNames.WEAPON_TYPE]
        self.item_type = ItemTypes.WEAPON
        self.name = stats[StatNames.NAMES][main_menu.language]
        self.item_icon = stats[StatNames.ICON]
        self.max_damage = stats[StatNames.STATS][StatNames.MAX_DAMAGE]
        self.min_damage = stats[StatNames.STATS][StatNames.MIN_DAMAGE]
        self.critical_strike_chance = stats[StatNames.STATS][StatNames.CRITICAL_STRIKE_CHANCE]
        self.accuracy = stats[StatNames.STATS][StatNames.ACCURACY]
        self._base_stamina_consumption = stats[StatNames.STATS][StatNames.BASE_STAMINA_CONSUMPTION]

        self._calculate_damage()
        self._calculate_stamina_cost()

    def _calculate_damage(self) -> None:
        self.max_damage = self.max_damage * (1 + (self.level - 1) * self._level_damage_multiplier) * (
                    0.8 + self.rarity * 0.2)
        self.min_damage = self.min_damage * (1 + (self.level - 1) * self._level_damage_multiplier) * (
                    0.8 + self.rarity * 0.2)

    def _calculate_stamina_cost(self) -> None:
        self.stamina_consumption = self._base_stamina_consumption * self.level / (0.8 + self.rarity * 0.1)

    def use_item(self) -> None:
        self.main_menu.game_menu.hide_item_info()
        if self.item_equipped:
            self.main_menu.main_character.unequip_weapon()
            self.main_menu.inventory_menu.refresh_inventory()
            self.main_menu.character_menu.refresh_character_copy()
            self.main_menu.character_menu.refresh_character_menu()
        else:
            self.main_menu.inventory_menu.unequip_all_weapon()
            self.main_menu.main_character.equip_weapon(self)
            self.main_menu.inventory_menu.refresh_inventory()
            self.main_menu.character_menu.refresh_character_copy()
            self.main_menu.character_menu.refresh_character_menu()

    @staticmethod
    def get_weapon_stats(weapon_file_name) -> Dict[str, Any]:
        with open(str(Path(Paths.PATH_TO_WEAPONS, weapon_file_name)), "r") as weapon_file:
            stats = safe_load(weapon_file)
            return stats
