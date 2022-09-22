from dataclasses import dataclass

from PyQt6.QtCore import QSize


@dataclass(frozen=True)
class CharacterMenuSizes:
    ATTRIBUTE_LINE: QSize = QSize(200, 20)
    TITLE_LINE: QSize = QSize(247, 20)
