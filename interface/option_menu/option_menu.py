from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QImage, QPalette, QBrush
from core.constants.windows_constants import WindowSizes
from core.constants.path_constants import Paths


class OptionMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(WindowSizes.OPTION_MENU_SIZE)
        self._create_background()

    def _create_background(self):
        self.setAutoFillBackground(True)
        background_image = QImage(Paths.OPTION_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.OPTION_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)
