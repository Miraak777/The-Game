from dataclasses import dataclass

import PyQt6.QtCore
from PyQt6.QtCore import QSize


@dataclass
class WindowSizes:
    MAIN_WINDOW_SIZE: PyQt6.QtCore.QSize = QSize(1200, 700)
    CHARACTER_MENU_SIZE: PyQt6.QtCore.QSize = QSize(400, 700)


@dataclass
class WindowsFonts:
    FONT_SIZE: int = 15


@dataclass
class ButtonSizes:
    CHARACTER_CREATE_NAME_LINE_EDIT: PyQt6.QtCore.QSize = QSize(150, 30)
