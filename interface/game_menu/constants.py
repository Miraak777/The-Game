from dataclasses import dataclass
from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class GameMenuSizes:
    GAME_WINDOW_SIZE: QSize = QSize(780, 685)
    SCROLL_AREA_SIZE: QSize = QSize(760, 565)
    LABEL_HEIGHT: int = 25


@dataclass(frozen=True)
class GameMenuButtons:
    ACTION_BUTTON_SIZE: QSize = QSize(377, 47)

