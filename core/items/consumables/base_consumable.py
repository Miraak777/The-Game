from core.constants.item_constants import ItemTypes
from ..base_item import BaseItem
from .consumable_stats import ConsumableStats


class BaseConsumable(BaseItem):
    def __init__(self, main_menu, level):
        super().__init__(main_menu=main_menu)
        self.item_type = ItemTypes.CONSUMABLE
        self.stats = ConsumableStats()


class BaseFood(BaseConsumable):
    def __init__(self, main_menu, level):
        super().__init__(main_menu=main_menu, level=level)
        self.heal = 0

    def use_item(self):
        self._main_menu.main_character.restore_percent_health(self.heal)
        self._main_menu.inventory_menu.remove_item(self.item_inventory_id)
