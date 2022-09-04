from dataclasses import dataclass

import PyQt6.QtCore
from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class MainWindowButtons:
    CHARACTER_MENU_BUTTON_SIZE: PyQt6.QtCore.QSize = QSize(40, 40)
