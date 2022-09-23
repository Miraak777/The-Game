from core.constants.widget_constants import WidgetNames as wn
from PyQt6.QtWidgets import QLineEdit, QPushButton, QWidget
from PyQt6.QtCore import Qt
from typing import Dict
from interface.common import get_key_binds
from core.constants.key_bind_constants import KeyBindNames
from .constants import MainWindowButtons, MainWindowSizes
from .stylesheets import (
    character_create_button_stylesheet,
    character_creation_button_stylesheet,
    character_menu_button_stylesheet,
    option_menu_button_stylesheet
)


def create_character_create_button(self, text) -> Dict:
    character_create_name_line_edit = QLineEdit()
    character_create_name_line_edit.setMaxLength(15)
    character_create_name_line_edit.setFixedSize(MainWindowSizes.CHARACTER_CREATE_NAME_LINE_EDIT)
    character_create_name_line_edit.setStyleSheet(character_create_button_stylesheet)
    character_create_name_line_edit.setPlaceholderText(text.CHARACTER_NAME_PLACEHOLDER)
    character_create_name_line_edit.textChanged.connect(self._event_main_character_name_entered)

    character_create_button = QPushButton(text=text.CHARACTER_CREATE_BUTTON)
    character_create_button.setStyleSheet(character_creation_button_stylesheet)
    character_create_button.setFixedSize(MainWindowButtons.CHARACTER_CREATION_BUTTON_SIZE)
    character_create_button.setCheckable(True)
    character_create_button.clicked.connect(self._event_create_new_character)
    character_create_button.setShortcut(Qt.Key.Key_Enter)
    character_create_button.setEnabled(False)

    return {wn.CHARACTER_CREATE_NAME_LINE_EDIT: character_create_name_line_edit,
            wn.CHARACTER_CREATE_BUTTON: character_create_button}


def create_character_menu_button(self) -> QWidget:

    character_menu_button = QPushButton()
    character_menu_button.setStyleSheet(character_menu_button_stylesheet)
    character_menu_button.setFixedSize(MainWindowButtons.MENUS_BUTTONS_SIZE)
    character_menu_button.setCheckable(True)
    character_menu_button.clicked.connect(self._event_open_character_menu)
    character_menu_button.setShortcut(get_key_binds()[KeyBindNames.CHARACTER_MENU])
    character_menu_button.setToolTip(self._text.CHARACTER_MENU_BUTTON_TOOLTIP)
    character_menu_button.setDisabled(True)
    return character_menu_button


def create_option_menu_button(self) -> QWidget:
    option_menu_button = QPushButton()
    option_menu_button.setStyleSheet(option_menu_button_stylesheet)
    option_menu_button.setFixedSize(MainWindowButtons.MENUS_BUTTONS_SIZE)
    option_menu_button.setCheckable(True)
    option_menu_button.clicked.connect(self._event_open_options_menu)
    option_menu_button.setShortcut(get_key_binds()[KeyBindNames.OPTION_MENU])
    option_menu_button.setToolTip(self._text.OPTION_MENU_BUTTON_TOOLTIP)
    option_menu_button.setDisabled(True)
    return option_menu_button
