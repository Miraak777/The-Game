from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QLabel, QVBoxLayout
from copy import copy

from core.constants.character_constants import AttributesNames as an
from core.common import clear_layout

from . import widgets
from . import buttons
from .constants import CharacterMenuSizes
from .stylesheets import character_menu_stylesheet
from .texts import Text


class CharacterMenu(QFrame):
    def __init__(self, main_menu) -> None:
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(CharacterMenuSizes.CHARACTER_MENU_SIZE)
        self.setStyleSheet(character_menu_stylesheet)
        self._main_character_copy = None
        self._layout = None

    def refresh_character_menu(self) -> None:
        clear_layout(self._layout)
        clear_layout(self._attributes_title_layout)
        clear_layout(self._strength_layout)
        clear_layout(self._agility_layout)
        clear_layout(self._vitality_layout)
        clear_layout(self._endurance_layout)
        clear_layout(self._attribute_points_layout)
        clear_layout(self._accept_button_layout)
        self._create_widgets()

    def create_layout(self) -> None:
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._main_character_copy = copy(self._main_menu.main_character)
        self._create_widgets()
        self.setLayout(self._layout)

    def _create_widgets(self) -> None:

        exit_button = buttons.create_exit_menu_button(self)
        self._layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignRight)

        for line in widgets.create_general_widget(self):
            self._layout.addWidget(line)

        for line in widgets.create_bars_lines(self):
            self._layout.addWidget(line)

        attribute_layouts = widgets.create_attributes_widget(self)
        self._attributes_title_layout = attribute_layouts[0]
        self._layout.addLayout(self._attributes_title_layout)
        self._attribute_points_layout = attribute_layouts[1]
        self._layout.addLayout(self._attribute_points_layout)
        self._strength_layout = attribute_layouts[2]
        self._layout.addLayout(self._strength_layout)
        self._agility_layout = attribute_layouts[3]
        self._layout.addLayout(self._agility_layout)
        self._vitality_layout = attribute_layouts[4]
        self._layout.addLayout(self._vitality_layout)
        self._endurance_layout = attribute_layouts[5]
        self._layout.addLayout(self._endurance_layout)
        self._accept_button_layout = attribute_layouts[6]
        self._layout.addLayout(self._accept_button_layout)
        label = QLabel()
        label.setFixedWidth(1)
        self._layout.addWidget(label)
        for line in widgets.create_stats_widget(self):
            self._layout.addWidget(line)

    def _event_add_strength(self) -> None:
        if self._main_character_copy.attribute_points >= 1:
            self._main_character_copy.strength += 1
            self._main_character_copy.attribute_points -= 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_add_agility(self) -> None:
        if self._main_character_copy.attribute_points >= 1:
            self._main_character_copy.agility += 1
            self._main_character_copy.attribute_points -= 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_add_vitality(self) -> None:
        if self._main_character_copy.attribute_points >= 1:
            self._main_character_copy.vitality += 1
            self._main_character_copy.attribute_points -= 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_add_endurance(self) -> None:
        if self._main_character_copy.attribute_points >= 1:
            self._main_character_copy.endurance += 1
            self._main_character_copy.attribute_points -= 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_remove_strength(self) -> None:
        if self._main_character_copy.attribute_points <= self._main_menu.main_character.attribute_points:
            if self._main_character_copy.strength != 0:
                self._main_character_copy.strength -= 1
                self._main_character_copy.attribute_points += 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_remove_agility(self) -> None:
        if self._main_character_copy.attribute_points <= self._main_menu.main_character.attribute_points:
            if self._main_character_copy.agility != 0:
                self._main_character_copy.agility -= 1
                self._main_character_copy.attribute_points += 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_remove_vitality(self) -> None:
        if self._main_character_copy.attribute_points <= self._main_menu.main_character.attribute_points:
            if self._main_character_copy.vitality != 0:
                self._main_character_copy.vitality -= 1
                self._main_character_copy.attribute_points += 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_remove_endurance(self) -> None:
        if self._main_character_copy.attribute_points <= self._main_menu.main_character.attribute_points:
            if self._main_character_copy.endurance != 0:
                self._main_character_copy.endurance -= 1
                self._main_character_copy.attribute_points += 1
        self._main_character_copy.refresh_stats()
        self.refresh_character_menu()

    def _event_accept(self) -> None:
        output_attributes = {
            an.STRENGTH: self._main_character_copy.strength,
            an.AGILITY: self._main_character_copy.agility,
            an.VITALITY: self._main_character_copy.vitality,
            an.ENDURANCE: self._main_character_copy.endurance,
            an.ATTRIBUTE_POINTS: self._main_character_copy.attribute_points,
        }
        self._main_menu.main_character.send_attributes(output_attributes)
        self._main_character_copy = copy(self._main_menu.main_character)
        self.refresh_character_menu()

    def _event_exit_menu(self) -> None:
        self.hide()
