from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QLabel, QFrame
from core.constants.character_constants import (
    StatsNames as sn,
    AttributesNames as an
)
from main_character.start_parameters import Attributes
from interface.common import clear_layout
from .constants import CharacterMenuSizes
from .stylesheets import character_menu_stylesheet
from .texts import Text
from . import widgets


class CharacterMenu(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(CharacterMenuSizes.CHARACTER_MENU_SIZE)

        self._main_character_stats = self._main_menu.main_character.get_stats()
        self._attributes = Attributes()

        self._set_stylesheet()
        self._create_layout()

    def _set_stylesheet(self) -> None:
        self.setStyleSheet(character_menu_stylesheet)

    def set_actual_character_stats(self):
        self._main_character_stats = self._main_menu.main_character.get_stats()
        self._attributes.STRENGTH = self._main_character_stats[an.STRENGTH]
        self._attributes.AGILITY = self._main_character_stats[an.AGILITY]
        self._attributes.VITALITY = self._main_character_stats[an.VITALITY]
        self._attributes.ENDURANCE = self._main_character_stats[an.ENDURANCE]
        self._attributes.ATTRIBUTE_POINTS = self._main_character_stats[an.ATTRIBUTE_POINTS]
        self._calculate_character_stats()
        self.refresh_character_menu()

    def _calculate_character_stats(self) -> None:
        stats_for_calculation = self._main_menu.main_character.get_stats_for_calculation()
        new_stats = self._main_menu.main_character.calculate_character_stats(
            attributes=self._attributes,
            main_stats=stats_for_calculation[sn.MAIN_STATS],
            class_multipliers=stats_for_calculation[sn.CLASS_MULTIPLIERS],
            equipped_weapon=stats_for_calculation[sn.EQUIPPED_WEAPON]
        )
        for stat in new_stats:
            self._main_character_stats[stat] = new_stats[stat]

    def refresh_character_menu(self) -> None:
        self._calculate_character_stats()
        clear_layout(self._layout)
        clear_layout(self._attributes_title_layout)
        clear_layout(self._strength_layout)
        clear_layout(self._agility_layout)
        clear_layout(self._vitality_layout)
        clear_layout(self._endurance_layout)
        clear_layout(self._attribute_points_layout)
        clear_layout(self._accept_button_layout)
        self._create_widgets()

    def _create_widgets(self) -> None:

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
        self._layout.addWidget(QLabel())
        for line in widgets.create_stats_widget(self):
            self._layout.addWidget(line)

    def _create_layout(self) -> None:
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._create_widgets()
        self.setLayout(self._layout)

    def _event_add_strength(self):
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.STRENGTH += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
        self.refresh_character_menu()

    def _event_add_agility(self):
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.AGILITY += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
        self.refresh_character_menu()

    def _event_add_vitality(self):
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.VITALITY += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
        self.refresh_character_menu()

    def _event_add_endurance(self):
        if self._attributes.ATTRIBUTE_POINTS >= 1:
            self._attributes.ENDURANCE += 1
            self._attributes.ATTRIBUTE_POINTS -= 1
        self.refresh_character_menu()

    def _event_remove_strength(self):
        if self._attributes.ATTRIBUTE_POINTS <= self._main_character_stats[an.ATTRIBUTE_POINTS]:
            if self._attributes.STRENGTH != 0:
                self._attributes.STRENGTH -= 1
                self._attributes.ATTRIBUTE_POINTS += 1
        self.refresh_character_menu()

    def _event_remove_agility(self):
        if self._attributes.ATTRIBUTE_POINTS <= self._main_character_stats[an.ATTRIBUTE_POINTS]:
            if self._attributes.AGILITY != 0:
                self._attributes.AGILITY -= 1
                self._attributes.ATTRIBUTE_POINTS += 1
        self.refresh_character_menu()

    def _event_remove_vitality(self):
        if self._attributes.ATTRIBUTE_POINTS <= self._main_character_stats[an.ATTRIBUTE_POINTS]:
            if self._attributes.VITALITY != 0:
                self._attributes.VITALITY -= 1
                self._attributes.ATTRIBUTE_POINTS += 1
        self.refresh_character_menu()

    def _event_remove_endurance(self):
        if self._attributes.ATTRIBUTE_POINTS <= self._main_character_stats[an.ATTRIBUTE_POINTS]:
            if self._attributes.ENDURANCE != 0:
                self._attributes.ENDURANCE -= 1
                self._attributes.ATTRIBUTE_POINTS += 1
        self.refresh_character_menu()

    def _event_accept(self):
        output_attributes = {
            an.STRENGTH: self._attributes.STRENGTH,
            an.AGILITY: self._attributes.AGILITY,
            an.VITALITY: self._attributes.VITALITY,
            an.ENDURANCE: self._attributes.ENDURANCE,
            an.ATTRIBUTE_POINTS: self._attributes.ATTRIBUTE_POINTS
        }
        self._main_menu.main_character.send_attributes(output_attributes)
        self.set_actual_character_stats()
