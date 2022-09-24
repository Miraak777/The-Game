from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from PyQt6.QtCore import Qt
from core import Paths
from core.constants.language_constants import Language, LANGUAGE
from yaml import safe_load, safe_dump
from interface.common import clear_layout
from .stylesheets import option_menu_stylesheet
from .constants import OptionMenuSizes
from .texts import Text
from . import widgets


class OptionMenu(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._language = self._main_menu.language
        self._text = Text[self._language]()
        self.setFixedSize(OptionMenuSizes.OPTION_MENU_SIZE)

        self.setStyleSheet(option_menu_stylesheet)
        self._create_layout()

    def _create_layout(self):
        self._layout = QGridLayout()
        self._create_widgets()
        self.setLayout(self._layout)

    def _create_widgets(self):
        self._create_dummy_widgets()

        self._choose_language_layout = widgets.create_language_choose_widget(self)
        self._languages_layout = widgets.create_languages_buttons(self)
        self._choose_language_layout.addLayout(self._languages_layout)
        self._layout.addLayout(self._choose_language_layout, 1, 0)

        self._title = widgets.create_title_widget(self)
        self._layout.addWidget(self._title, 0, 1)

    def _refresh_menu(self):
        clear_layout(self._layout)
        clear_layout(self._choose_language_layout)
        clear_layout(self._languages_layout)
        self._create_widgets()

    def _create_dummy_widgets(self):
        self._dummy_widget1 = QWidget()
        self._dummy_widget1.setFixedSize(OptionMenuSizes.OPTION_MENU_LANGUAGE)
        self._layout.addWidget(self._dummy_widget1, 0, 0)

        self._dummy_widget2 = QWidget()
        self._dummy_widget2.setFixedSize(OptionMenuSizes.OPTION_MENU_LANGUAGE)
        self._layout.addWidget(self._dummy_widget2, 2, 2)

    def _event_set_en_language(self):
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.EN
        with open(Paths.PATH_TO_SETTINGS, 'w') as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)
        self._event_language_changed()

    def _event_set_ru_language(self):
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.RU
        with open(Paths.PATH_TO_SETTINGS, 'w') as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)
        self._event_language_changed()

    def _event_language_changed(self):
        clear_layout(self._languages_layout)
        clear_layout(self._choose_language_layout)
        clear_layout(self._layout)
        label = widgets.restart_request_label(self)
        button = widgets.exit_button(self)
        self._create_dummy_widgets()
        self._layout.addWidget(button, 2, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self._layout.addWidget(label, 1, 1)

    @staticmethod
    def _event_exit():
        exit()
