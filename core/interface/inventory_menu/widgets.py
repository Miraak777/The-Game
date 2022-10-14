from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from pathlib import Path
from .constants import InventoryMenuSizes
from .stylesheets import item_button_stylesheet, equipped_item_button_stylesheet
from core.constants.path_constants import path_to_item_icons_map


class ItemSlot(QPushButton):
    def __init__(self, item):
        super().__init__()
        self.setFixedSize(InventoryMenuSizes.ITEM_SIZE)
        self.setStyleSheet(item_button_stylesheet)
        if item:
            self.setIconSize(InventoryMenuSizes.ITEM_ICON_SIZE)
            icon_path = str(Path(path_to_item_icons_map[item.item_type], item.item_icon))
            self.setIcon(QIcon(icon_path))
            self.clicked.connect(item.use_item)
            if item.item_equipped:
                self.setStyleSheet(equipped_item_button_stylesheet)
        else:
            self.setDisabled(True)


