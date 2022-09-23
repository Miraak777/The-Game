from PyQt6.QtWidgets import (
    QGridLayout,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
)
from PyQt6.QtCore import Qt
from core.constants.path_constants import Paths
from interface.option_menu.option_menu import OptionMenu
from interface.character_menu.character_menu import CharacterMenu
from core.constants.widget_constants import WidgetNames as wn
from core.constants.language_constants import LANGUAGE
from main_character import MainCharacter
from yaml import safe_load
from .stylesheets import main_window_stylesheet
from .constants import MainWindowSizes, DUMMY
from .texts import Text
from . import widgets


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.language = self._get_language()
        self._text = Text[self.language]
        self.setWindowTitle(self._text.TITLE)
        self.setFixedSize(MainWindowSizes.MAIN_WINDOW_SIZE)

        self._layout = QGridLayout()
        self._dummy_widget1 = QWidget()
        self._layout.addWidget(self._dummy_widget1, 0, 0)
        self._dummy_widget2 = QWidget()
        self._layout.addWidget(self._dummy_widget2, 2, 2)

        self.setStyleSheet(main_window_stylesheet)
        self._create_menus()
        self._create_buttons()

        self._widget = QWidget()
        self._widget.setLayout(self._layout)
        self.setCentralWidget(self._widget)

    @staticmethod
    def _get_language():
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        return settings[LANGUAGE]

    def _create_menus(self):
        self._main_character_name = DUMMY
        self.main_character = MainCharacter(self._main_character_name)

        self._character_menu = CharacterMenu(self)
        self._character_menu.hide()
        self._option_menu = OptionMenu(self)
        self._option_menu.hide()

        self._layout.addWidget(self._character_menu, 0, 2,
                               alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter))
        self._layout.addWidget(self._option_menu, 0, 1,
                               alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

    def _create_buttons(self):
        character_creation = widgets.create_character_create_button(self, self._text)
        self._character_create_name_line_edit = character_creation[wn.CHARACTER_CREATE_NAME_LINE_EDIT]
        self._character_create_button = character_creation[wn.CHARACTER_CREATE_BUTTON]
        self._character_menu_button = widgets.create_character_menu_button(self)
        self._option_menu_button = widgets.create_option_menu_button(self)

        character_creation_layout = QVBoxLayout()
        character_creation_layout.addWidget(self._character_create_name_line_edit,
                                            alignment=Qt.AlignmentFlag.AlignHCenter)
        character_creation_layout.addWidget(self._character_create_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.menus_buttons_layout = QHBoxLayout()
        self.menus_buttons_layout.addWidget(self._character_menu_button)
        self.menus_buttons_layout.addWidget(self._option_menu_button)

        self._layout.addLayout(character_creation_layout, 1, 1)
        self._layout.addLayout(self.menus_buttons_layout, 2, 2,
                               alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

    def _event_open_character_menu(self) -> None:
        if self._character_menu.isHidden():
            self._character_menu.set_actual_character_stats()
            self._character_menu.show()
        else:
            self._character_menu.hide()

    def _event_open_options_menu(self):
        if self._option_menu.isHidden():
            self._option_menu.show()
        else:
            self._option_menu.hide()

    def _event_create_new_character(self) -> None:
        self.main_character = MainCharacter(self._main_character_name)
        self.main_character.set_max_health()
        self.main_character.set_max_stamina()
        self._character_menu_button.setDisabled(False)
        self._option_menu_button.setDisabled(False)
        self._character_create_button.hide()
        self._character_create_name_line_edit.hide()

    def _event_main_character_name_entered(self, name) -> None:
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)
