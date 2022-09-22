from PyQt6.QtWidgets import QWidget, QGridLayout, QFrame
from core.constants.widget_constants import WindowSizes
from core.constants.path_constants import Paths, BACKGROUNDS
from interface.interface_language.option_menu_text import Text
import interface.option_menu.lines_creation as lines
from core.constants.language_constants import Language, LANGUAGE
from yaml import safe_load, safe_dump


class OptionMenu(QFrame):
    def __init__(self, language):
        super().__init__()
        self._text = Text[language]()
        self.setFixedSize(WindowSizes.OPTION_MENU_SIZE)

        self._create_background()
        self._create_layout()

    def _create_background(self):
        self.setStyleSheet("OptionMenu {"
                           f"background-image: url({BACKGROUNDS}:option_menu_background.jpg);"
                           "}")

    def _create_layout(self):
        self._layout = QGridLayout()

        self._dummy_widget1 = QWidget()
        self._layout.addWidget(self._dummy_widget1, 0, 0)

        self._dummy_widget2 = QWidget()
        self._layout.addWidget(self._dummy_widget2, 2, 2)

        self._title = lines.create_title_line(self)
        self._layout.addWidget(self._title, 0, 1)

        self.setLayout(self._layout)

    @staticmethod
    def _event_set_en_language():
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.EN
        with open(Paths.PATH_TO_SETTINGS, 'w') as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)

    @staticmethod
    def _event_set_ru_language():
        with open(Paths.PATH_TO_SETTINGS, 'r') as settings_file:
            settings = safe_load(settings_file)
        settings[LANGUAGE] = Language.RU
        with open(Paths.PATH_TO_SETTINGS, 'w') as settings_file:
            safe_dump(settings, settings_file, default_flow_style=False)
