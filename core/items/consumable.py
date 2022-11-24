from core.items.base_item import BaseItem
from typing import List
from yaml import safe_load
from core.constants.path_constants import Path, Paths
from core.constants.item_constants import StatNames, ItemTypes


class Consumable(BaseItem):
    def __init__(self, main_menu, consumable_file_name):
        super().__init__(main_menu=main_menu)
        self.item_type = ItemTypes.CONSUMABLE
        stats = self.get_consumable_stats(consumable_file_name)
        self.name = stats[StatNames.NAMES][main_menu.language]
        self.consumable_type = stats[StatNames.CONSUMABLE_TYPE]
        self.item_icon = stats[StatNames.ICON]
        if self.consumable_type == ItemTypes.FOOD:
            self.restore_value = stats[StatNames.STATS][StatNames.RESTORE_VALUE]

    def use_item(self) -> None:
        if self.consumable_type == ItemTypes.FOOD:
            self._main_menu.main_character.restore_percent_health(self.restore_value)
            self._main_menu.inventory_menu.remove_item(self.item_inventory_id)

    def get_description_stats(self) -> List[str]:
        pass

    @staticmethod
    def get_consumable_stats(consumable_file_name):
        with open(str(Path(Paths.PATH_TO_CONSUMABLES, consumable_file_name)), "r") as consumable_file:
            stats = safe_load(consumable_file)
            return stats
