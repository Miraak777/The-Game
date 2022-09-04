from dataclasses import dataclass

import PyQt6.QtCore
from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainWindowButtons:
    CHARACTER_MENU_BUTTON_SIZE: QSize = QSize(40, 40)
    CHARACTER_CREATION_BUTTON_SIZE: QSize = QSize(100, 40)
