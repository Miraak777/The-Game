from PyQt6.QtGui import QBrush, QImage, QPalette
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QMainWindow,
    QWidget,
)
from interface.main_window.buttons import (
    _create_character_create_button,
    _create_character_menu_button,
)
from core.constants.path_constants import Paths
from interface.main_window.character_menu import CharacterMenu
from interface.interface_language.en_lang import MainMenuText
from interface.windows_parameters import WindowSizes
from main_character import MainCharacter


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(MainMenuText.TITLE)
        self.setFixedSize(WindowSizes.MAIN_WINDOW_SIZE)
        self._layout = QGridLayout()

        self._create_background()

        _create_character_menu_button(self)

        _create_character_create_button(self)

        self._dummy_widget = QWidget()
        self._layout.addWidget(self._dummy_widget, 0, 0)

        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    def _create_background(self) -> None:
        background_image = QImage(Paths.MAIN_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.MAIN_WINDOW_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _open_character_menu(self) -> None:
        self.character_menu = CharacterMenu(self._main_character)
        self.character_menu.show()

    def _create_new_character(self) -> None:
        self._main_character = MainCharacter(self._main_character_name)
        self._character_menu_button.show()
        self._character_create_button.hide()
        self._character_create_name_line_edit.hide()

    def _main_character_name_entered(self, name) -> None:
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)
