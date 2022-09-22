from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainWindowButtons:
    MENUS_BUTTONS_SIZE: QSize = QSize(40, 40)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(200, 70)


@dataclass(frozen=True)
class CharacterMenuButtons:
    ATTRIBUTE_BUTTON: QSize = QSize(29, 29)
    ACCEPT_BUTTON: QSize = QSize(122, 45)
