from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainMenuButtons:
    MENUS_BUTTONS_SIZE: QSize = QSize(42, 42)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(202, 72)
    ABOUT_MENU_EXIT: QSize = QSize(22, 22)


@dataclass(frozen=True)
class MainMenuSizes:
    MAIN_MENU_SIZE: QSize = QSize(1200, 700)
    CHARACTER_CREATE_NAME_LINE_EDIT: QSize = QSize(350, 40)
    ABOUT_MENU_SIZE: QSize = QSize(350, 250)
