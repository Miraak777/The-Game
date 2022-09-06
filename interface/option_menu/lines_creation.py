from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

from interface.common import upper_font, bold_font


def create_title_line(self):
    title = QLabel(self._text.TITLE)
    title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    title = upper_font(title)
    title = bold_font(title)
    self._layout.addWidget(title, 0, 1)
