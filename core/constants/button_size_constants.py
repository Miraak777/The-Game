from dataclasses import dataclass

import PyQt6.QtCore
from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainWindowButtons:
    MENUS_BUTTONS_SIZE: QSize = QSize(40, 40)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(150, 40)
#     TODO сделать настройку через конфиг


@dataclass(frozen=True)
class CharacterMenuButtons:
    ATTRIBUTE_BUTTON: QSize = QSize(20, 20)
