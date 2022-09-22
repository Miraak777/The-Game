from PyQt6.QtWidgets import QLabel, QHBoxLayout
from PyQt6.QtCore import Qt

from interface.common import upper_font, bold_font


def create_title_line(self) -> QLabel:
    title = QLabel(self._text.TITLE)
    title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    title = upper_font(title)
    title = bold_font(title)
    return title


def create_language_choose_line(self):
    language_choose_layout = QHBoxLayout()
    label = QLabel(text=self._text.LANGUAGE_CHANGE_LABEL)
