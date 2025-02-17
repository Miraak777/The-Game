from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QMainWindow, QStackedLayout, QWidget
from yaml import safe_load

from core.common import set_qdirs
from core.constants.language_constants import LANGUAGE
from core.constants.path_constants import Paths
from core.interface.character_menu.menu import CharacterMenu
from core.interface.game_menu.menu import GameMenu
from core.interface.inventory_menu.menu import InventoryMenu
from core.interface.option_menu.menu import OptionMenu
from core.main_character.character import MainCharacter
from core.scenarios.scenario import ScenariosManager, ss
from core.scenarios.event import Event
from core.scenarios.common import read_scenario_stats
from core.server_interactor.verificator import verify_resources_lists

from . import widgets
from .constants import MainMenuSizes
from .stylesheets import main_menu_stylesheet
from .texts import Text


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        set_qdirs()

        self.language = self._get_language()
        self.text = Text[self.language]
        self.setWindowTitle(self.text.TITLE)
        self.setFixedSize(MainMenuSizes.MAIN_MENU_SIZE)
        self.setStyleSheet(main_menu_stylesheet)
        self.setWindowIcon(QIcon(Paths.PATH_TO_MAIN_MENU_ICON))

        self._stacked_layout = QStackedLayout()
        self._stacked_layout.setStackingMode(QStackedLayout.StackingMode.StackAll)

        self.main_character = None

        self._create_layouts()
        self._add_menu_to_stacked_layout()

        self.scenarios_manager = ScenariosManager(self)
        self.chill_event = Event(self, read_scenario_stats("chill_scenario.yml")[ss.START])

        # if not verify_resources_lists():
        #     self.game_menu.add_log(self.text.FILE_VERIFY_FAILED)

    @staticmethod
    def exit() -> None:
        exit()

    def _create_layouts(self) -> None:
        self._main_layout = self._create_main_layout()
        widget = QWidget()
        widget.setLayout(self._main_layout)
        self.setCentralWidget(widget)

        self.character_menu = CharacterMenu(self)
        self._main_layout.addWidget(self.character_menu, 0, 2, alignment=Qt.AlignmentFlag.AlignRight)
        self.character_menu.hide()

        self._main_layout.addLayout(self._stacked_layout, 0, 0, 2, 0)

    def _add_menu_to_stacked_layout(self) -> None:
        self._option_menu = OptionMenu(self)
        layout = QHBoxLayout()
        layout.addWidget(self._option_menu, alignment=Qt.AlignmentFlag.AlignCenter)
        self.option_menu_widget = QWidget()
        self.option_menu_widget.setLayout(layout)

        self.about_menu = widgets.create_about_menu_layout(self)

        self._character_creation_menu_layout = widgets.create_character_creation_menu(self)
        self._character_creation_widget = QWidget()
        self._character_creation_widget.setLayout(self._character_creation_menu_layout)

        self.game_menu = GameMenu(self)
        Event(self, read_scenario_stats("start_scenario.yml")[ss.START]).run_event()

        self.inventory_menu = InventoryMenu(self)
        layout = QHBoxLayout()
        layout.addWidget(self.inventory_menu, alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop))
        widget = QWidget()
        widget.setLayout(layout)

        self._stacked_layout.addWidget(self.about_menu)
        self.about_menu.hide()
        self._stacked_layout.addWidget(self.option_menu_widget)
        self.option_menu_widget.hide()
        self._stacked_layout.addWidget(self._character_creation_widget)
        self._stacked_layout.addWidget(self.game_menu)
        self._stacked_layout.addWidget(widget)

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
        main_layout.addLayout(
            self._menu_buttons,
            2,
            2,
            alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom),
        )
        return main_layout

    def _event_open_character_menu(self) -> None:
        if self.character_menu.isHidden():

            self.character_menu.show()
        else:
            self.character_menu.hide()

    def _event_open_options_menu(self) -> None:
        if self.option_menu_widget.isHidden():
            self.option_menu_widget.show()
        else:
            self.option_menu_widget.hide()

    def _event_create_new_character(self) -> None:
        self._character_creation_widget.hide()
        self.main_character = MainCharacter(self._main_character_name, self)
        self.main_character.set_max_health()
        self.main_character.set_max_stamina()
        self.character_menu_button.setDisabled(False)
        self.character_menu.create_layout()

    def _event_main_character_name_entered(self, name: str) -> None:
        self._main_character_name = name
        if name != "" or None:
            self._character_create_button.setEnabled(True)
        else:
            self._character_create_button.setEnabled(False)

    @staticmethod
    def _get_language() -> str:
        with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
            settings = safe_load(settings_file)
        return settings[LANGUAGE]
