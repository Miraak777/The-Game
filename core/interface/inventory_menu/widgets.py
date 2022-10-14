from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from pathlib import Path
from .constants import InventoryMenuSizes
from .stylesheets import item_button_stylesheet
from core.constants.path_constants import path_to_item_icons_map


def create_item_button(item) -> QPushButton:
    button = QPushButton()
    button.setFixedSize(InventoryMenuSizes.ITEM_SIZE)
    button.setStyleSheet(item_button_stylesheet)
    if item:
        button.setIconSize(InventoryMenuSizes.ITEM_ICON_SIZE)
        icon_path = str(Path(path_to_item_icons_map[item.item_type], item.item_icon))
        button.setIcon(QIcon(icon_path))
        button.clicked.connect(item.use_item)
    return button
