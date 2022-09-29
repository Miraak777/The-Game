from PyQt6.QtWidgets import (
    QMainWindow,
    QHBoxLayout,
    QStackedLayout,
    QGridLayout,
    QWidget,
)
from PyQt6.QtCore import Qt
from core.constants.path_constants import Paths
from interface.option_menu.option_menu import OptionMenu
from interface.character_menu.character_menu import CharacterMenu
from interface.game_menu.game_menu import GameMenu
from core.constants.language_constants import LANGUAGE
from main_character import MainCharacter
from yaml import safe_load
from scenarios import StartScenario
from scenarios.base_situation.base_situation import BaseSituation
from .stylesheets import main_menu_stylesheet
from .constants import MainMenuSizes, DUMMY
from .texts import Text
from . import widgets


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.language = self._get_language()
        self.text = Text[self.language]
        self.setWindowTitle(self.text.TITLE)
        self.setFixedSize(MainMenuSizes.MAIN_MENU_SIZE)
        self.setStyleSheet(main_menu_stylesheet)

        self.main_character = MainCharacter(DUMMY, self)

        self._create_layouts()

        BaseSituation(self)

    @staticmethod
    def endgame():
        exit()

    def _create_layouts(self) -> None:
        self._main_layout = self._create_main_layout()
        widget = QWidget()
        widget.setLayout(self._main_layout)
        self.setCentralWidget(widget)

        self.character_menu = CharacterMenu(self)
        self._main_layout.addWidget(self.character_menu, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)
        self.character_menu.hide()

        self._stacked_layout = self._create_stacked_layout()
        self._main_layout.addLayout(self._stacked_layout, 0, 0, 2, 0)

    def _create_stacked_layout(self) -> QStackedLayout:
        stacked_layout = QStackedLayout()
        stacked_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.game_menu = GameMenu(self)
        stacked_layout.addWidget(self.game_menu)

        self._character_creation_menu_layout = widgets.create_character_creation_menu(self)
        self._character_creation_widget = QWidget()
        self._character_creation_widget.setLayout(self._character_creation_menu_layout)
        stacked_layout.addWidget(self._character_creation_widget)

        self._option_menu = OptionMenu(self)
        layout = QHBoxLayout()
        layout.addWidget(self._option_menu, alignment=Qt.AlignmentFlag.AlignCenter)
        self._option_menu_widget = QWidget()
        self._option_menu_widget.setLayout(layout)
        self._option_menu_widget.hide()
        stacked_layout.addWidget(self._option_menu_widget)

        return stacked_layout

    def _create_menu_buttons(self) -> QHBoxLayout:
        menu_buttons_layout = QHBoxLayout()
        self.character_menu_button = widgets.create_character_menu_button(self)
        self.character_menu_button.setDisabled(True)
        self._option_menu_button = widgets.create_option_menu_button(self)

        menu_buttons_layout.addWidget(self.character_menu_button)
        menu_buttons_layout.addWidget(self._option_menu_button)
        return menu_buttons_layout

    def _create_main_layout(self) -> QGridLayout:
        main_layout = QGridLayout()
        self._menu_buttons = self._create_menu_buttons()
        main_layout.addLayout(self._menu_buttons, 2, 2,
                              alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))
        return main_layout

    def _event_open_character_menu(self) -> None:
        if self.character_menu.isHidden():
            self.character_menu.set_actual_character_stats()
            self.character_menu.show()
        else:
            self.character_menu.hide()

    def _event_open_options_menu(self) -> None:
        if self._option_menu_widget.isHidden():
            self._option_menu_widget.show()
        else:
            self._option_menu_widget.hide()

    def _event_create_new_character(self) -> None:
        self._character_creation_widget.hide()
        self.main_character = MainCharacter(self._main_character_name, self)
        self.main_character.set_max_health()
        self.main_character.set_max_stamina()
        self.character_menu_button.setDisabled(False)
        StartScenario(self)

    def _event_main_character_name_entered(self, name: str) -> None:
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)

    @staticmethod
    def _get_language() -> str:
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        return settings[LANGUAGE]
