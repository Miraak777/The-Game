from core.constants.button_size_constants import MainWindowButtons
from PyQt6.QtWidgets import QVBoxLayout, QLineEdit, QPushButton
from PyQt6.QtGui import QIcon
from core import Paths
from interface.interface_language.en_lang import MainMenuText


def create_character_create_button(self) -> None:
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


def create_character_menu_button(self) -> None:
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
