from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class OptionMenuButtons:
    LANGUAGE_BUTTON: QSize = QSize(100, 30)


@dataclass(frozen=True)
class OptionMenuSizes:
    OPTION_MENU_TITLE: QSize = QSize(150, 40)
    OPTION_MENU_LANGUAGE: QSize = QSize(150, 40)
    OPTION_MENU_SIZE: QSize = QSize(1000, 600)
