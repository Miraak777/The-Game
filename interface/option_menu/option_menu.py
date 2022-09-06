from PyQt6.QtWidgets import QWidget
from core.constants.windows_constants import WindowSizes


class OptionMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(WindowSizes.OPTION_MENU_SIZE)
