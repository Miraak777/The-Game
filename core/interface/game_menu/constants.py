from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class GameMenuSizes:
    GAME_WINDOW_SIZE: QSize = QSize(780, 685)
    SCROLL_AREA_SIZE: QSize = QSize(760, 470)
    CHARACTER_BARS_SIZE: QSize = QSize(377, 20)
    ENEMY_BAR_SIZE: QSize = QSize(760, 20)


@dataclass(frozen=True)
class GameMenuButtons:
    ACTION_BUTTON_SIZE: QSize = QSize(377, 67)
