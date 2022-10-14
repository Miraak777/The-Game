from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class InventoryMenuSizes:
    INVENTORY_MENU_SIZE: QSize = QSize(393, 600)
    ITEM_SIZE: QSize = QSize(50, 50)
    ITEM_ICON_SIZE: QSize = QSize(48, 48)
    ITEMS_HORIZONTAL_NUMBER = 6
    ITEMS_VERTICAL_NUMBER = 9
