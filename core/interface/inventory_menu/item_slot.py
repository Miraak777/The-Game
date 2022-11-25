from pathlib import Path

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

from core.constants.path_constants import path_to_item_icons_map

from .constants import InventoryMenuSizes
from .stylesheets import item_button_stylesheet


class ItemSlot(QPushButton):
    hover = pyqtSignal(str)

    def __init__(self, item) -> None:
        super().__init__()
        self.setFixedSize(InventoryMenuSizes.ITEM_SIZE)
        self.setStyleSheet(item_button_stylesheet)
        self.item = item
        if self.item:
            rarity_map = {
                0: "#8a582f",
                1: "black",
                2: "#0ee647",
                3: "#1a87ed",
                4: "#eb0cf2",
                5: "orange",
                6: "red",
                7: "white",
            }
            self.rarity = rarity_map[self.item.rarity]
            self.setIconSize(InventoryMenuSizes.ITEM_ICON_SIZE)
            icon_path = str(Path(path_to_item_icons_map[self.item.item_type], self.item.item_icon))
            self.setIcon(QIcon(icon_path))
            self.clicked.connect(self.item.use_item)
            self.hover.connect(self.item.main_menu.game_menu.event_hover_item_show)
            if item.item_equipped:
                equipped_border = "border-radius: 10px"
            else:
                equipped_border = ""
            self.setStyleSheet("QPushButton {background-color: rgba(0, 0, 0, 0.15);"
                               f"border: 2px solid {self.rarity};"
                               f"{equipped_border}"
                               "}"
                               "QPushButton:hover {background-color: rgba(0, 255, 0, 0.15);}")

        else:
            self.setDisabled(True)

    def enterEvent(self, event):
        self.hover.emit("enterEvent")

    def leaveEvent(self, event):
        self.hover.emit("leaveEvent")
