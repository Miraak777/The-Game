from PyQt6.QtWidgets import QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from core.constants.character_constants import (
    BarsNames as bn,
    CombatStatsNames as cs,
    MainStatsNames as msn,
    Classes
)
from .constants import CharacterMenuSizes
from . import buttons


def create_general_widget(self) -> list:
    lines = []
    class_map = {
        Classes.PEASANT: self._text.PEASANT,
        Classes.WARRIOR: self._text.WARRIOR,
        Classes.ASSASSIN: self._text.ASSASSIN
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
    label = QLabel(self._text.NAME + self._main_character_stats[msn.NAME])
    return label


def create_level_line(self) -> QLabel:
    label = QLabel(
        self._text.LEVEL + str(self._main_character_stats[msn.LEVEL])
    )
    return label


def create_class_line(self, class_map) -> QLabel:
    label = QLabel(self._text.CLASS + class_map[self._main_character_stats[msn.CLASS]])
    return label


def create_bars_lines(self) -> list:
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
        self._text.HEALTH
        + str(self._main_character_stats[bn.MAX_HEALTH])
        + "/"
        + str(self._main_character_stats[bn.HEALTH])
    )
    return label


def create_stamina_widget(self) -> QLabel:
    label = QLabel(
        self._text.STAMINA
        + str(self._main_character_stats[bn.MAX_STAMINA])
        + "/"
        + str(self._main_character_stats[bn.STAMINA])
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
    label = QLabel(
        self._text.STRENGTH + str(self._attributes.STRENGTH)
    )
    return label


def create_agility_widget(self) -> QLabel:
    label = QLabel(
        self._text.AGILITY + str(self._attributes.AGILITY)
    )
    return label


def create_vitality_widget(self) -> QLabel:
    label = QLabel(
        self._text.VITALITY + str(self._attributes.VITALITY)
    )
    return label


def create_endurance_widget(self) -> QLabel:
    label = QLabel(
        self._text.ENDURANCE + str(self._attributes.ENDURANCE)
    )
    return label


def create_attribute_points_widget(self) -> QLabel:
    label = QLabel(
        self._text.ATTRIBUTE_POINTS
        + str(self._attributes.ATTRIBUTE_POINTS)
    )
    return label


def create_stats_widget(self) -> list:
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
        self._text.DAMAGE
        + str(self._main_character_stats[cs.MIN_DAMAGE])
        + "-"
        + str(self._main_character_stats[cs.MAX_DAMAGE])
    )
    return label


def create_accuracy_widget(self) -> QLabel:
    label = QLabel(
        self._text.ACCURACY
        + str(self._main_character_stats[cs.ACCURACY] * 100)
        + "%"
    )
    return label


def create_critical_strike_chance_widget(self) -> QLabel:
    label = QLabel(
        self._text.CRITICAL_STRIKE_CHANCE
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_CHANCE] * 100)
        + "%"
    )
    return label


def create_critical_strike_multiplier_widget(self) -> QLabel:
    label = QLabel(
        self._text.CRITICAL_STRIKE_MULTIPLIER
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_MULTIPLIER])
    )
    return label
