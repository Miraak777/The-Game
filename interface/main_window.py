from PyQt6.QtGui import QBrush, QIcon, QImage, QPalette
from PyQt6.QtWidgets import (
    QGridLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from core.constants.button_size_constants import MainWindowButtons
from core.constants.path_constants import Paths
from interface.character_menu import CharacterMenu
from interface.interface_language.en_lang import MainMenuText
from interface.windows_parameters import WindowSizes
from main_character import MainCharacter


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._main_character_name = None
        self._main_character = None

        self._main_window_init()

        self._create_character_menu_button()

        self._create_character_create_button()

        self._test_label = QLabel()
        self._layout.addWidget(self._test_label, 0, 0)

        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    def _main_window_init(self):
        self.setWindowTitle(MainMenuText.TITLE)
        self.setFixedSize(WindowSizes.MAIN_WINDOW_SIZE)
        self._create_background()
        self._layout = QGridLayout()

    def _create_background(self):
        background_image = QImage(Paths.MAIN_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.MAIN_WINDOW_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _create_character_create_button(self):
        self._character_creation_layout = QVBoxLayout()
        self._character_create_name_line_edit = QLineEdit()
        self._character_create_name_line_edit.setMaxLength(15)
        self._character_create_name_line_edit.setPlaceholderText(
            MainMenuText.CHARACTER_NAME_PLACEHOLDER
        )
        self._character_create_name_line_edit.textChanged.connect(
            self._main_character_name_entered
        )

        self._character_create_button = QPushButton(
            text=MainMenuText.CHARACTER_CREATE_BUTTON
        )
        self._character_create_button.setFixedSize(
            MainWindowButtons.CHARACTER_CREATION_BUTTON_SIZE
        )
        self._character_create_button.setCheckable(True)
        self._character_create_button.clicked.connect(self._create_new_character)
        self._character_create_button.setEnabled(False)

        self._character_creation_layout.addWidget(self._character_create_name_line_edit)
        self._character_creation_layout.addWidget(self._character_create_button)
        self._layout.addLayout(self._character_creation_layout, 1, 1)

    def _create_character_menu_button(self):
        self._character_menu_button = QPushButton(icon=QIcon(Paths.CHARACTER_MENU_ICON))
        self._character_menu_button.setIconSize(
            MainWindowButtons.CHARACTER_MENU_BUTTON_SIZE
        )
        self._character_menu_button.setFixedSize(
            MainWindowButtons.CHARACTER_MENU_BUTTON_SIZE
        )
        self._character_menu_button.setCheckable(True)
        self._character_menu_button.clicked.connect(self._open_character_menu)
        self._character_menu_button.hide()
        self._layout.addWidget(self._character_menu_button, 2, 2)

    def _open_character_menu(self):
        self.character_menu = CharacterMenu(self._main_character)
        self.character_menu.show()

    def _create_new_character(self):
        self._main_character = MainCharacter(self._main_character_name)
        self._character_menu_button.show()
        self._character_create_button.hide()
        self._character_create_name_line_edit.hide()

    def _main_character_name_entered(self, name):
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)
