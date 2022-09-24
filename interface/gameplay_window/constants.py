from dataclasses import dataclass
from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class GameWindowSizes:
    GAME_WINDOW_SIZE: QSize = QSize(800, 685)
    SCROLL_AREA_SIZE: QSize = QSize(780, 565)


@dataclass(frozen=True)
class GameWindowButtons:
    ACTION_BUTTON_SIZE: QSize = QSize(387, 47)
