from core.constants.button_size_constants import MainWindowButtons
from core.constants.windows_constants import ButtonSizes, WidgetNames as wn
from PyQt6.QtWidgets import QLineEdit, QPushButton, QWidget
from PyQt6.QtGui import QIcon
from core import Paths
from typing import Dict
from interface.interface_language.en_lang import MainMenuText


def set_menus_button_and_icon_sizes(menu_button: QPushButton) -> QPushButton:
    menu_button.setIconSize(
        MainWindowButtons.MENUS_BUTTONS_SIZE
    )
    menu_button.setFixedSize(
        MainWindowButtons.MENUS_BUTTONS_SIZE
    )
    return menu_button


def create_character_create_button(self) -> Dict:
    character_create_name_line_edit = QLineEdit()
    character_create_name_line_edit.setMaxLength(15)
    character_create_name_line_edit.setFixedSize(ButtonSizes.CHARACTER_CREATE_NAME_LINE_EDIT)
    character_create_name_line_edit.setPlaceholderText(
        MainMenuText.CHARACTER_NAME_PLACEHOLDER
    )
    character_create_name_line_edit.textChanged.connect(
        self._event_main_character_name_entered
    )

    character_create_button = QPushButton(
        text=MainMenuText.CHARACTER_CREATE_BUTTON
    )
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
    character_menu_button = set_menus_button_and_icon_sizes(character_menu_button)
    character_menu_button.setCheckable(True)
    character_menu_button.clicked.connect(self._event_open_character_menu)
    character_menu_button.setDisabled(True)
    return character_menu_button


def create_option_menu_button(self) -> QWidget:
    option_menu_button = QPushButton(icon=QIcon(Paths.OPTION_MENU_ICON))
    option_menu_button = set_menus_button_and_icon_sizes(option_menu_button)
    option_menu_button.setCheckable(True)
    option__menu_button.clicked.connect()
    return option_menu_button