from PyQt6.QtWidgets import QFrame, QGridLayout, QMainWindow

from core.common import clear_layout
from core.constants.item_constants import ItemTypes

from .constants import InventoryMenuSizes
from .inventory_map import inventory_map
from .stylesheets import inventory_menu_stylesheet
from .texts import Text
from .item_slot import ItemSlot


class InventoryMenu(QFrame):
    def __init__(self, main_menu: QMainWindow) -> None:
        super().__init__()
        self._main_menu = main_menu
        self._log = self._main_menu.game_menu.add_log
        self._language = main_menu.language
        self._text = Text[self._language]
        self._layout = None
        self._inventory_map = inventory_map

        self.setFixedSize(InventoryMenuSizes.INVENTORY_MENU_SIZE)
        self.setStyleSheet(inventory_menu_stylesheet)
        self.create_layout()
        self._create_item_buttons()

    def create_layout(self) -> None:
        self._layout = QGridLayout()
        self.setLayout(self._layout)
        self._layout.setSpacing(0)

    def _create_item_buttons(self) -> None:
        item_id = 0
        for vertical in range(InventoryMenuSizes.ITEMS_VERTICAL_NUMBER):
            for horizontal in range(InventoryMenuSizes.ITEMS_HORIZONTAL_NUMBER):
                item_button = ItemSlot(self._inventory_map[item_id])
                item_id += 1
                self._layout.addWidget(item_button, vertical, horizontal)

    def refresh_inventory(self) -> None:
        clear_layout(self._layout)
        self._create_item_buttons()

    def unequip_all_weapon(self) -> None:
        for item_id in range(InventoryMenuSizes.ITEMS_VERTICAL_NUMBER * InventoryMenuSizes.ITEMS_HORIZONTAL_NUMBER):
            if (
                self._inventory_map[item_id]
                and self._inventory_map[item_id].item_type == ItemTypes.WEAPON
                and self._inventory_map[item_id].item_equipped
            ):
                self._inventory_map[item_id].item_equipped = False
        self.refresh_inventory()

    def add_item(self, item) -> None:
        if self._inventory_map[len(self._inventory_map) - 1]:
            self._log(self._text.INVENTORY_IS_FULL)
        else:
            for item_id in self._inventory_map:
                if not self._inventory_map[item_id]:
                    self._inventory_map[item_id] = item
                    item.item_inventory_id = item_id
                    break
        self.refresh_inventory()

    def remove_item(self, item_id) -> None:
        self._inventory_map[item_id] = None
        self.refresh_inventory()
