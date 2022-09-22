from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from core.constants.widget_constants import WindowSizes
from core import Paths, BACKGROUNDS, BUTTONS
from interface.interface_language.option_menu_text import Text
import interface.option_menu.widget_creation as lines
from core.constants.language_constants import Language, LANGUAGE
from core.constants.widget_constants import WidgetSizes
from yaml import safe_load, safe_dump
from core import WIDGET_TEXTURES
from interface.common import clear_layout


class OptionMenu(QFrame):
    def __init__(self, language):
        super().__init__()
        self._language = language
        self._text = Text[language]()
        self.setFixedSize(WindowSizes.OPTION_MENU_SIZE)

        self._set_stylesheets()
        self._create_layout()

    def _set_stylesheets(self):
        self.setStyleSheet("OptionMenu {"
                           f"background-image: url({BACKGROUNDS}:option_menu_background.jpg);"
                           "}")
        self._title_stylesheet = ("QLabel {"
                                  f"background-image: url({WIDGET_TEXTURES}:option_menu_title.png);"
                                  "background-repeat: no-repeat;"
                                  "background-position:vertical-center;"
                                  "font: bold 20px;"
                                  "color:#edbd79;"
                                  "padding: 1px;}")
        self._language_choose_stylesheet = ("QLabel {"
                                            f"background-image: url({WIDGET_TEXTURES}:option_menu_title.png);"
                                            "font: bold 18px;"
                                            "background-repeat: no-repeat;"
                                            "color:#edbd79;"
                                            "padding: 1px;}")
        self._languages_buttons_stylesheet = ("QPushButton:enabled {"
                                              f"background-image: url({BUTTONS}:language_button_enabled.png);"
                                              "color:#edbd79;"
                                              "border: 0px;"
                                              "}"
                                              "QPushButton {"
                                              f"background-image: url({BUTTONS}:language_button_disabled.png);"
                                              "color: black;"
                                              "font: 18px;"
                                              "border: 0px;"
                                              "}")
        self._restart_request_stylesheet = ("QLabel {"
                                            "font: bold 18px;"
                                            "color: #edbd79;}")

    def _create_layout(self):
        self._layout = QGridLayout()
        self._create_widgets()
        self.setLayout(self._layout)

    def _create_widgets(self):
        self._create_dummy_widgets()

        self._choose_language_layout = lines.create_language_choose_widget(self)
        self._languages_layout = lines.create_languages_buttons(self)
        self._choose_language_layout.addLayout(self._languages_layout)
        self._layout.addLayout(self._choose_language_layout, 1, 0)

        self._title = lines.create_title_widget(self)
        self._layout.addWidget(self._title, 0, 1)

    def _refresh_menu(self):
        clear_layout(self._layout)
        clear_layout(self._choose_language_layout)
        clear_layout(self._languages_layout)
        self._create_widgets()

    def _create_dummy_widgets(self):
        self._dummy_widget1 = QWidget()
        self._dummy_widget1.setFixedSize(WidgetSizes.OPTION_MENU_LANGUAGE)
        self._layout.addWidget(self._dummy_widget1, 0, 0)

        self._dummy_widget2 = QWidget()
        self._dummy_widget2.setFixedSize(WidgetSizes.OPTION_MENU_LANGUAGE)
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
        label = lines.restart_request_label(self, self._text)
        self._create_dummy_widgets()
        self._layout.addWidget(label, 1, 1)
