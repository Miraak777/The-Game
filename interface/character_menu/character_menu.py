from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QImage, QPalette
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from core.constants.path_constants import Paths
from core.constants.widget_constants import WindowSizes, attribute_lines
from interface.interface_language.character_menu_text import Text
import interface.character_menu.lines_creation as lines
from interface.common import clear_layout


class CharacterMenu(QWidget):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self._attribute_lines_length = attribute_lines[self._main_menu.language]
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)

        self._main_character_stats = main_menu.main_character.get_stats()

        self._create_background()
        self._create_layout()

    def _create_background(self) -> None:
        self.setAutoFillBackground(True)
        background_image = QImage(Paths.CHARACTER_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.CHARACTER_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def refresh_character_menu(self) -> None:
        self._main_character_stats = self._main_menu.main_character.get_stats()
        clear_layout(self._layout)
        clear_layout(self._attributes_title_layout)
        clear_layout(self._strength_layout)
        clear_layout(self._agility_layout)
        clear_layout(self._vitality_layout)
        clear_layout(self._endurance_layout)
        clear_layout(self._attribute_points_layout)
        self._create_lines()

    def _create_lines(self) -> None:

        for line in lines.create_general_lines(self):
            self._layout.addWidget(line)

        for line in lines.create_bars_lines(self):
            self._layout.addWidget(line)

        attribute_layouts = lines.create_attributes_lines(self)
        self._attributes_title_layout = attribute_layouts[0]
        self._layout.addLayout(self._attributes_title_layout)
        self._strength_layout = attribute_layouts[1]
        self._layout.addLayout(self._strength_layout)
        self._agility_layout = attribute_layouts[2]
        self._layout.addLayout(self._agility_layout)
        self._vitality_layout = attribute_layouts[3]
        self._layout.addLayout(self._vitality_layout)
        self._endurance_layout = attribute_layouts[4]
        self._layout.addLayout(self._endurance_layout)
        self._attribute_points_layout = attribute_layouts[5]
        self._layout.addLayout(self._attribute_points_layout)

        for line in lines.create_stats_lines(self):
            self._layout.addWidget(line)

    def _create_layout(self) -> None:
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._create_lines()
        self.setLayout(self._layout)

    def _event_add_strength(self):
        self._main_menu.main_character.add_strength()
        self.refresh_character_menu()

    def _event_add_agility(self):
        self._main_menu.main_character.add_agility()
        self.refresh_character_menu()

    def _event_add_vitality(self):
        self._main_menu.main_character.add_vitality()
        self.refresh_character_menu()

    def _event_add_endurance(self):
        self._main_menu.main_character.add_endurance()
        self.refresh_character_menu()
