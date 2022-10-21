from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class CharacterMenuSizes:
    ATTRIBUTE_LINE: QSize = QSize(200, 20)
    CHARACTER_MENU_SIZE: QSize = QSize(400, 600)


@dataclass(frozen=True)
class CharacterMenuButtons:
    ATTRIBUTE_BUTTON: QSize = QSize(31, 31)
    ACCEPT_BUTTON: QSize = QSize(124, 47)
    EXIT_MENU_BUTTON: QSize = QSize(22, 22)
