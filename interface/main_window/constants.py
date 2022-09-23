from dataclasses import dataclass

from PyQt6.QtCore import QSize

DUMMY = "dummy"


@dataclass(frozen=True)
class MainWindowButtons:
    MENUS_BUTTONS_SIZE: QSize = QSize(42, 42)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(202, 72)


@dataclass(frozen=True)
class MainWindowSizes:
    MAIN_WINDOW_SIZE: QSize = QSize(1200, 700)
    CHARACTER_CREATE_NAME_LINE_EDIT: QSize = QSize(300, 40)
