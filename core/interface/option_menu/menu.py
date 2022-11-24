from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QHBoxLayout, QVBoxLayout
from yaml import safe_dump, safe_load

from core import Paths
from core.constants.language_constants import LANGUAGE, Language
from core.common import clear_layout
from core.scenarios.debug_scenario.scenario import DebugScenario

from . import widgets
from .constants import OptionMenuSizes
from .stylesheets import option_menu_stylesheet
from .texts import Text


class OptionMenu(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self.main_menu = main_menu
        self._language = self.main_menu.language
        self._text = Text[self._language]()
        self.setFixedSize(OptionMenuSizes.OPTION_MENU_SIZE)

        self.setStyleSheet(option_menu_stylesheet)
        self._create_layout()

    def _create_layout(self):
        self._layout = QVBoxLayout()
        self._create_widgets()
        self.setLayout(self._layout)

    def _create_widgets(self):

        exit_menu_button = widgets.create_exit_menu_button(self)
        self._layout.addWidget(exit_menu_button, alignment=Qt.AlignmentFlag.AlignRight)

        self._title = widgets.create_title_widget(self)
        self._layout.addWidget(self._title, alignment=Qt.AlignmentFlag.AlignHCenter)

        self._choose_language_layout = widgets.create_language_choose_title(self)
        self._languages_layout = widgets.create_languages_buttons(self)
        self._choose_language_layout.addLayout(self._languages_layout)
        self._layout.addLayout(self._choose_language_layout)

        self._layout.addStretch()
        self._down_buttons_layout = QHBoxLayout()
        self._layout.addLayout(self._down_buttons_layout)

        self._down_buttons_layout.addWidget(
            widgets.about_menu_button(self),
            alignment=(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignLeft),
        )

        self._down_buttons_layout.addWidget(
            widgets.debug_mode_button(self),
            alignment=(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight),
        )

    def _refresh_menu(self):
        clear_layout(self._layout)
        clear_layout(self._choose_language_layout)
        clear_layout(self._languages_layout)
        self._create_widgets()

    def _event_set_en_language(self):
        with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.EN
        with open(Paths.PATH_TO_SETTINGS, "w") as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)
        self._event_language_changed()

    def _event_set_ru_language(self):
        with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.RU
        with open(Paths.PATH_TO_SETTINGS, "w") as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)
        self._event_language_changed()

    def _event_language_changed(self):
        clear_layout(self._languages_layout)
        clear_layout(self._choose_language_layout)
        clear_layout(self._layout)
        label = widgets.restart_request_label(self)
        button = widgets.exit_button(self)
        self._layout.addWidget(
            label,
            alignment=(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom),
        )
        self._layout.addWidget(button, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop))

    def _event_debug_mode(self):
        DebugScenario(self.main_menu)

    def event_open_about_menu(self):
        if self.main_menu.about_menu.isHidden():
            self.main_menu.about_menu.show()
        else:
            self.main_menu.about_menu.hide()

    @staticmethod
    def _event_exit():
        exit()

    def _event_exit_menu(self):
        self.main_menu.option_menu_widget.hide()