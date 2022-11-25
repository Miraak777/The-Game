from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel

from core.constants.character_constants import BarsNames as bn
from core.constants.character_constants import Classes
from core.constants.character_constants import CombatStatsNames as cs
from core.constants.character_constants import MainStatsNames as msn

from . import buttons
from .constants import CharacterMenuSizes


def create_general_widget(self) -> list:
    lines = []
    class_map = {
        Classes.PEASANT: self._text.PEASANT,
        Classes.WARRIOR: self._text.WARRIOR,
        Classes.ASSASSIN: self._text.ASSASSIN,
    }
    label = QLabel(self._text.GENERAL)
    label.setStyleSheet("font: bold;")
    lines.append(label)

    label = create_name_widget(self)
    lines.append(label)

    label = create_level_line(self)
    lines.append(label)

    label = create_class_line(self, class_map)
    lines.append(label)

    return lines


def create_name_widget(self) -> QLabel:
    label = QLabel(f" {self._text.NAME} {self._main_character_copy.name}")
    return label


def create_level_line(self) -> QLabel:
    label = QLabel(
        f" {self._text.LEVEL} {self._main_character_copy.level}, "
        f"{self._main_character_copy.experience}/{self._main_character_copy.max_experience}"
    )
    return label


def create_class_line(self, class_map) -> QLabel:
    label = QLabel(f" {self._text.CLASS} {class_map[self._main_character_copy.character_class]}")
    return label


def create_bars_lines(self) -> list[QLabel]:
    lines = []
    label = QLabel(self._text.BARS)
    label.setStyleSheet("font: bold;")
    lines.append(label)

    label = create_health_widget(self)
    lines.append(label)

    label = create_stamina_widget(self)
    lines.append(label)
    return lines


def create_health_widget(self) -> QLabel:
    label = QLabel(
        f" {self._text.HEALTH} " f"{self._main_character_copy.health}/{self._main_character_copy.max_health}"
    )
    return label


def create_stamina_widget(self) -> QLabel:
    label = QLabel(
        f" {self._text.STAMINA} " f"{self._main_character_copy.stamina}/{self._main_character_copy.max_stamina}"
    )
    return label


def create_attributes_widget(self) -> list[QHBoxLayout]:
    layouts = []

    title_layout = QHBoxLayout()
    label = QLabel(self._text.ATTRIBUTES)
    label.setStyleSheet("font: bold;")
    title_layout.addWidget(label)
    layouts.append(title_layout)

    attribute_points_layout = QHBoxLayout()
    label = create_attribute_points_widget(self)
    attribute_points_layout.addWidget(label)
    layouts.append(attribute_points_layout)

    strength_layout = QHBoxLayout()
    label = create_strength_widget(self)
    label.setFixedSize(CharacterMenuSizes.ATTRIBUTE_LINE)
    strength_layout.addWidget(label)
    button = buttons.create_strength_adding_button(self)
    strength_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
    button = buttons.create_strength_removing_button(self)
    strength_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
    layouts.append(strength_layout)

    agility_layout = QHBoxLayout()
    label = create_agility_widget(self)
    label.setFixedSize(CharacterMenuSizes.ATTRIBUTE_LINE)
    agility_layout.addWidget(label)
    button = buttons.create_agility_adding_button(self)
    agility_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
    button = buttons.create_agility_removing_button(self)
    agility_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
    layouts.append(agility_layout)

    vitality_layout = QHBoxLayout()
    label = create_vitality_widget(self)
    label.setFixedSize(CharacterMenuSizes.ATTRIBUTE_LINE)
    vitality_layout.addWidget(label)
    button = buttons.create_vitality_adding_button(self)
    vitality_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
    button = buttons.create_vitality_removing_button(self)
    vitality_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
    layouts.append(vitality_layout)

    endurance_layout = QHBoxLayout()
    label = create_endurance_widget(self)
    label.setFixedSize(CharacterMenuSizes.ATTRIBUTE_LINE)
    endurance_layout.addWidget(label)
    button = buttons.create_endurance_adding_button(self)
    endurance_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignRight)
    button = buttons.create_endurance_removing_button(self)
    endurance_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
    layouts.append(endurance_layout)

    accept_button_layout = QHBoxLayout()
    button = buttons.create_accept_button(self)
    accept_button_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignLeft)
    layouts.append(accept_button_layout)

    return layouts


def create_strength_widget(self) -> QLabel:
    label = QLabel(f" {self._text.STRENGTH} {self._main_character_copy.strength}")
    return label


def create_agility_widget(self) -> QLabel:
    label = QLabel(f" {self._text.AGILITY} {self._main_character_copy.agility}")
    return label


def create_vitality_widget(self) -> QLabel:
    label = QLabel(f" {self._text.VITALITY} {self._main_character_copy.vitality}")
    return label


def create_endurance_widget(self) -> QLabel:
    label = QLabel(f" {self._text.ENDURANCE} {self._main_character_copy.endurance}")
    return label


def create_attribute_points_widget(self) -> QLabel:
    label = QLabel(f"{ self._text.ATTRIBUTE_POINTS} {self._main_character_copy.attribute_points}")
    return label


def create_stats_widget(self) -> list[QLabel]:
    lines = []
    label = QLabel(self._text.STATS)
    label.setStyleSheet("font: bold;")
    lines.append(label)

    label = create_damage_widget(self)
    lines.append(label)

    label = create_accuracy_widget(self)
    lines.append(label)

    label = create_critical_strike_chance_widget(self)
    lines.append(label)

    label = create_critical_strike_multiplier_widget(self)
    lines.append(label)

    return lines


def create_damage_widget(self) -> QLabel:
    label = QLabel(
        f" {self._text.DAMAGE} " f"{self._main_character_copy.min_damage}-{self._main_character_copy.max_damage}"
    )
    return label


def create_accuracy_widget(self) -> QLabel:
    label = QLabel(f" {self._text.ACCURACY} {self._main_character_copy.accuracy * 100}%")
    return label


def create_critical_strike_chance_widget(self) -> QLabel:
    label = QLabel(
        f" {self._text.CRITICAL_STRIKE_CHANCE} " f"{self._main_character_copy.critical_strike_chance * 100}%"
    )
    return label


def create_critical_strike_multiplier_widget(self) -> QLabel:
    label = QLabel(
        f" {self._text.CRITICAL_STRIKE_MULTIPLIER} " f"{self._main_character_copy.critical_strike_multiplier}"
    )
    return label
