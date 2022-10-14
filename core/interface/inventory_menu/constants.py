from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class InventoryMenuSizes:
    INVENTORY_MENU_SIZE: QSize = QSize(393, 700)
