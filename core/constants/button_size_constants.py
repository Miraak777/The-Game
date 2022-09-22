from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainWindowButtons:
    MENUS_BUTTONS_SIZE: QSize = QSize(40, 40)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(150, 40)
#     TODO сделать настройку через конфиг


@dataclass(frozen=True)
class CharacterMenuButtons:
    ATTRIBUTE_BUTTON: QSize = QSize(25, 25)
    ACCEPT_BUTTON: QSize = QSize(80, 25)
