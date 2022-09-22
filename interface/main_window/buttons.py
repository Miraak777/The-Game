from core.constants.button_size_constants import MainWindowButtons
from core.constants.widget_constants import WidgetSizes, WidgetNames as wn
from PyQt6.QtWidgets import QLineEdit, QPushButton, QWidget
from PyQt6.QtGui import QIcon
from core import Paths, WIDGET_TEXTURES
from typing import Dict
from interface.common import set_button_and_icon_sizes


def create_character_create_button(self, text) -> Dict:
    character_create_name_line_edit = QLineEdit()
    character_create_name_line_edit.setMaxLength(15)
    character_create_name_line_edit.setFixedSize(WidgetSizes.CHARACTER_CREATE_NAME_LINE_EDIT)
    character_create_name_line_edit.setStyleSheet(
        f"background-image: url({WIDGET_TEXTURES}:character_creation_line_edit.jpg);"
        "font: bold 20px;"
        "border: 1px solid black")
    character_create_name_line_edit.setPlaceholderText(
        text.CHARACTER_NAME_PLACEHOLDER
    )
    character_create_name_line_edit.textChanged.connect(
        self._event_main_character_name_entered
    )

    character_create_button = QPushButton(text=text.CHARACTER_CREATE_BUTTON)
    character_create_button.setStyleSheet(self._character_creation_button_stylesheet)
    character_create_button.setFixedSize(
        MainWindowButtons.CHARACTER_CREATION_BUTTON_SIZE
    )
    character_create_button.setCheckable(True)
    character_create_button.clicked.connect(self._event_create_new_character)
    character_create_button.setEnabled(False)

    return {wn.CHARACTER_CREATE_NAME_LINE_EDIT: character_create_name_line_edit,
            wn.CHARACTER_CREATE_BUTTON: character_create_button}


def create_character_menu_button(self) -> QWidget:
    character_menu_button = QPushButton(icon=QIcon(Paths.CHARACTER_MENU_ICON))
    character_menu_button = set_button_and_icon_sizes(character_menu_button, MainWindowButtons.MENUS_BUTTONS_SIZE)
    character_menu_button.setCheckable(True)
    character_menu_button.clicked.connect(self._event_open_character_menu)
    character_menu_button.setDisabled(True)
    return character_menu_button


def create_option_menu_button(self) -> QWidget:
    option_menu_button = QPushButton(icon=QIcon(Paths.OPTION_MENU_ICON))
    option_menu_button = set_button_and_icon_sizes(option_menu_button, MainWindowButtons.MENUS_BUTTONS_SIZE)
    option_menu_button.setCheckable(True)
    option_menu_button.clicked.connect(self._event_open_options_menu)
    option_menu_button.setDisabled(True)
    return option_menu_button
