from core.items.base_item import BaseItem
from core.constants.item_constants import StatNames, ItemTypes
from typing import List, Dict, Any
from yaml import safe_load
from core.constants.path_constants import Path, Paths
from PyQt6.QtWidgets import QMainWindow


class Weapon(BaseItem):
    def __init__(self, main_menu: QMainWindow, level: int, weapon_file_name: str) -> None:
        super().__init__(main_menu)
        self.level = level
        stats = self.get_weapon_stats(weapon_file_name)

        self._level_damage_multiplier = 0.2
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
        self.max_damage = self.max_damage * (1 + self.level * self._level_damage_multiplier)
        self.min_damage = self.min_damage * (1 + self.level * self._level_damage_multiplier)

    def _calculate_stamina_cost(self) -> None:
        self.stamina_consumption = self._base_stamina_consumption * self.level

    def use_item(self) -> None:
        if self.item_equipped:
            self._main_menu.main_character.unequip_weapon()
            self._main_menu.inventory_menu.refresh_inventory()
        else:
            self._main_menu.inventory_menu.unequip_all_weapon()
            self._main_menu.main_character.equip_weapon(self)
            self._main_menu.inventory_menu.refresh_inventory()

    @staticmethod
    def get_weapon_stats(weapon_file_name) -> Dict[str, Any]:
        with open(str(Path(Paths.PATH_TO_WEAPONS, weapon_file_name)), "r") as weapon_file:
            stats = safe_load(weapon_file)
            return stats

    def get_description_stats(self) -> List[str]:
        pass
