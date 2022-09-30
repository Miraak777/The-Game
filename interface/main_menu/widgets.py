from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLineEdit, QPushButton, QVBoxLayout, QWidget

from core.constants.key_bind_constants import KeyBindNames
from interface.common import get_key_binds

from .constants import MainMenuSizes, MainWindowButtons
from .stylesheets import (
    character_create_button_stylesheet,
    character_creation_button_stylesheet,
    character_menu_button_stylesheet,
    option_menu_button_stylesheet,
)


def create_character_creation_menu(self) -> QVBoxLayout:
    character_creation_layout = QVBoxLayout()

    character_create_name_line_edit = QLineEdit()
    character_create_name_line_edit.setMaxLength(15)
    character_create_name_line_edit.setFixedSize(MainMenuSizes.CHARACTER_CREATE_NAME_LINE_EDIT)
    character_create_name_line_edit.setStyleSheet(character_create_button_stylesheet)
    character_create_name_line_edit.setPlaceholderText(self.text.CHARACTER_NAME_PLACEHOLDER)
    character_create_name_line_edit.textChanged.connect(self._event_main_character_name_entered)

    self._character_create_button = QPushButton(text=self.text.CHARACTER_CREATE_BUTTON)
    self._character_create_button.setStyleSheet(character_creation_button_stylesheet)
    self._character_create_button.setFixedSize(MainWindowButtons.CHARACTER_CREATION_BUTTON_SIZE)
    self._character_create_button.setCheckable(True)
    self._character_create_button.clicked.connect(self._event_create_new_character)
    self._character_create_button.setShortcut(Qt.Key.Key_Enter)
    self._character_create_button.setEnabled(False)

    character_creation_layout.addWidget(
        character_create_name_line_edit,
        alignment=(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom),
    )
    character_creation_layout.addWidget(
        self._character_create_button,
        alignment=(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop),
    )

    return character_creation_layout


def create_character_menu_button(self) -> QWidget:
    character_menu_button = QPushButton()
    character_menu_button.setStyleSheet(character_menu_button_stylesheet)
    character_menu_button.setFixedSize(MainWindowButtons.MENUS_BUTTONS_SIZE)
    character_menu_button.setCheckable(True)
    character_menu_button.clicked.connect(self._event_open_character_menu)
    character_menu_button.setShortcut(get_key_binds()[KeyBindNames.CHARACTER_MENU])
    character_menu_button.setToolTip(self.text.CHARACTER_MENU_BUTTON_TOOLTIP)
    return character_menu_button


def create_option_menu_button(self) -> QWidget:
    option_menu_button = QPushButton()
    option_menu_button.setStyleSheet(option_menu_button_stylesheet)
    option_menu_button.setFixedSize(MainWindowButtons.MENUS_BUTTONS_SIZE)
    option_menu_button.setCheckable(True)
    option_menu_button.clicked.connect(self._event_open_options_menu)
    option_menu_button.setShortcut(get_key_binds()[KeyBindNames.OPTION_MENU])
    option_menu_button.setToolTip(self.text.OPTION_MENU_BUTTON_TOOLTIP)
    return option_menu_button
