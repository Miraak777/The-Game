from .weapon_stats import WeaponStats
from ..base_item import BaseItem
from core.constants.item_constants import ItemTypes


class BaseWeapon(BaseItem):
    def __init__(self, main_menu, level=1):
        super().__init__(main_menu)
        self.item_type = ItemTypes.WEAPON
        self.stats = WeaponStats()
        self.stats.LEVEL = level
        self._calculate_damage()

    def _calculate_damage(self):
        self.stats.MAX_DAMAGE = self.stats.MAX_DAMAGE * (1 + self.stats.LEVEL * self.stats.LEVEL_DAMAGE_MULTIPLIER)
        self.stats.MIN_DAMAGE = self.stats.MIN_DAMAGE * (1 + self.stats.LEVEL * self.stats.LEVEL_DAMAGE_MULTIPLIER)

    def use_item(self):
        if self.item_equipped:
            self._main_menu.main_character.unequip_weapon()
            self._main_menu.inventory_menu.refresh_inventory()
        else:
            self._main_menu.inventory_menu.unequip_all_weapon()
            self._main_menu.main_character.equip_weapon(self)
            self._main_menu.inventory_menu.refresh_inventory()
