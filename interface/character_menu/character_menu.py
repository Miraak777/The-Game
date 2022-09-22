from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame
from core.constants.path_constants import BACKGROUNDS, BUTTONS
from core.constants.widget_constants import WindowSizes
from core.constants.character_constants import StatsNames as sn, AttributesNames as an
from interface.interface_language.character_menu_text import Text
import interface.character_menu.lines_creation as lines
from main_character.start_parameters import Attributes
from interface.common import clear_layout


class CharacterMenu(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)

        self._main_character_stats = self._main_menu.main_character.get_stats()
        self._attributes = Attributes()
        self._actual_attribute_points = 0

        self._set_stylesheet()
        self._create_layout()

    def _set_stylesheet(self) -> None:
        self.setStyleSheet("CharacterMenu {"
                           f"background-image: url({BACKGROUNDS}:character_menu_background.png);"
                           "}")
        self._add_button_stylesheet = ("QPushButton:enabled {" +
                                       f"background-image: url({BUTTONS}:add_button_enabled.png);" +
                                       "border: 0px;" +
                                       "background-position: center;" +
                                       "}"
                                       "QPushButton {"
                                       f"background-image: url({BUTTONS}:add_button_disabled.png);"
                                       "}")
        self._remove_button_stylesheet = ("QPushButton:enabled {" +
                                          f"background-image: url({BUTTONS}:remove_button_enabled.png);" +
                                          "border: 0px;" +
                                          "background-position: center;" +
                                          "}"
                                          "QPushButton {"
                                          f"background-image: url({BUTTONS}:remove_button_disabled.png);"
                                          "}")
        self._accept_button_stylesheet = ("QPushButton:enabled {" +
                                          f"background-image: url({BUTTONS}:accept_button_enabled.png);" +
                                          "font: bold 17px;" +
                                          "color: #edbd79;" +
                                          "border: 0px;" +
                                          "}"
                                          "QPushButton {"
                                          f"background-image: url({BUTTONS}:accept_button_disabled.png);"
                                          "}")

    def set_actual_character_stats(self):
        self._main_character_stats = self._main_menu.main_character.get_stats()
        self._actual_attribute_points = self._main_character_stats[an.ATTRIBUTE_POINTS]
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
        self._create_lines()

    def _create_lines(self) -> None:

        for line in lines.create_general_lines(self):
            self._layout.addWidget(line)

        for line in lines.create_bars_lines(self):
            self._layout.addWidget(line)

        attribute_layouts = lines.create_attributes_lines(self)
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
        for line in lines.create_stats_lines(self):
            self._layout.addWidget(line)

    def _create_layout(self) -> None:
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._create_lines()
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
