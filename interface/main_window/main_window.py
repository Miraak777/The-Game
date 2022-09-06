from PyQt6.QtGui import QBrush, QImage, QPalette
from PyQt6.QtWidgets import (
    QGridLayout,
    QMainWindow,
    QWidget,
)
from PyQt6.QtCore import Qt
import interface.main_window.buttons as buttons
from core.constants.path_constants import Paths
from interface.character_menu.character_menu import CharacterMenu
from interface.interface_language.en_lang import MainMenuText
from core.constants.windows_constants import WindowSizes
from main_character import MainCharacter
from core.constants.common_constants import DUMMY


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle(MainMenuText.TITLE)
        self.setFixedSize(WindowSizes.MAIN_WINDOW_SIZE)
        self._layout = QGridLayout()

        self._create_background()

        self._create_menu()

        buttons.create_character_menu_button(self)

        buttons.create_character_create_button(self)

        self._dummy_widget1 = QWidget()
        self._layout.addWidget(self._dummy_widget1, 0, 0)

        self._dummy_widget2 = QWidget()
        self._layout.addWidget(self._dummy_widget2, 2, 2)

        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    def _create_menu(self):
        self._main_character_name = DUMMY
        self._main_character = MainCharacter(self._main_character_name)
        self._character_menu = CharacterMenu(self._main_character)
        self._layout.addWidget(self._character_menu, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)
        self._character_menu.hide()

    def _create_background(self) -> None:
        background_image = QImage(Paths.MAIN_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.MAIN_WINDOW_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _open_character_menu(self) -> None:
        if self._character_menu.isHidden():
            self._character_menu.refresh_character_menu(self._main_character)
            self._character_menu.show()
        else:
            self._character_menu.hide()

    def _create_new_character(self) -> None:
        self._main_character = MainCharacter(self._main_character_name)
        self._main_character.set_max_health()
        self._main_character.set_max_stamina()
        self._character_menu_button.show()
        self._dummy_widget2.hide()
        self._character_create_button.hide()
        self._character_create_name_line_edit.hide()

    def _main_character_name_entered(self, name) -> None:
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)
