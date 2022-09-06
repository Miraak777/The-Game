from PyQt6.QtWidgets import QWidget, QGridLayout
from PyQt6.QtGui import QImage, QPalette, QBrush
from core.constants.windows_constants import WindowSizes
from core.constants.path_constants import Paths
from interface.interface_language.option_menu_text import Text
import interface.option_menu.lines_creation as lines


class OptionMenu(QWidget):
    def __init__(self, language):
        super().__init__()
        self._text = Text[language]
        self.setFixedSize(WindowSizes.OPTION_MENU_SIZE)
        self._create_background()
        self._create_layout()

    def _create_background(self):
        self.setAutoFillBackground(True)
        background_image = QImage(Paths.OPTION_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.OPTION_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _create_layout(self):
        self._layout = QGridLayout()

        self._dummy_widget1 = QWidget()
        self._layout.addWidget(self._dummy_widget1, 0, 0)

        self._dummy_widget2 = QWidget()
        self._layout.addWidget(self._dummy_widget2, 2, 2)

        lines.create_title_line(self)

        self.setLayout(self._layout)
