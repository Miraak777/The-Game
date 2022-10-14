from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel

from .constants import InventoryMenuSizes
from .stylesheets import inventory_menu_stylesheet
from .texts import Text


class InventoryMenu(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._language = main_menu.language
        self._text = Text[self._language]
        self.setFixedSize(InventoryMenuSizes.INVENTORY_MENU_SIZE)
        self.setStyleSheet(inventory_menu_stylesheet)
        self.create_layout()

    def create_layout(self):
        self._layout = QGridLayout()
        self.setLayout(self._layout)
