from core.constants.path_constants import Paths
from interface.character_menu import CharacterMenu
from interface.windows_parameters import WindowSizes
from core.constants.button_size_constants import MainWindowButtons
from PyQt6.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
    QLabel,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("The Game")
        self.setFixedSize(WindowSizes.MAIN_WINDOW_SIZE)
        self._create_background()
        self._layout = QGridLayout()

        self._create_character_menu_button()

        self._test_label = QLabel()
        self._layout.addWidget(self._test_label, 0, 0)

        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    def _create_background(self):
        background_image = QImage(Paths.MAIN_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.MAIN_WINDOW_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _open_character_menu(self):
        self.character_menu = CharacterMenu()
        self.character_menu.show()

    def _create_character_menu_button(self):
        self._character_menu_button = QPushButton(icon=QIcon(Paths.CHARACTER_MENU_ICON))
        self._character_menu_button.setIconSize(MainWindowButtons.CHARACTER_MENU_BUTTON_SIZE)
        self._character_menu_button.setFixedSize(MainWindowButtons.CHARACTER_MENU_BUTTON_SIZE)
        self._character_menu_button.setCheckable(True)
        self._character_menu_button.clicked.connect(self._open_character_menu)
        self._layout.addWidget(self._character_menu_button, 1, 1)
