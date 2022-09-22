from PyQt6.QtWidgets import QLabel, QHBoxLayout
from interface.common import upper_font, bold_font
from PyQt6.QtCore import Qt
from interface.character_menu import buttons
from core.constants.size_constants import CharacterMenuSizes
from core.constants.character_constants import (
    BarsNames as bn,
    CombatStatsNames as cs,
    MainStatsNames as msn,
    Classes
)


def create_general_widget(self) -> list:
    lines = []
    class_map = {
        Classes.PEASANT: self._text.PEASANT,
        Classes.WARRIOR: self._text.WARRIOR,
        Classes.ASSASSIN: self._text.ASSASSIN
    }
    label = QLabel(self._text.GENERAL)
    label = upper_font(label)
    label = bold_font(label)
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
    label = upper_font(label)
    return label


def create_level_line(self) -> QLabel:
    label = QLabel(
        self._text.LEVEL + str(self._main_character_stats[msn.LEVEL])
    )
    label = upper_font(label)
    return label


def create_class_line(self, class_map) -> QLabel:
    label = QLabel(self._text.CLASS + class_map[self._main_character_stats[msn.CLASS]])
    label = upper_font(label)
    return label


def create_bars_lines(self) -> list:
    lines = []
    label = QLabel(self._text.BARS)
    label = upper_font(label)
    label = bold_font(label)
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
    label = upper_font(label)
    return label


def create_stamina_widget(self) -> QLabel:
    label = QLabel(
        self._text.STAMINA
        + str(self._main_character_stats[bn.MAX_STAMINA])
        + "/"
        + str(self._main_character_stats[bn.STAMINA])
    )
    label = upper_font(label)
    return label


def create_attributes_widget(self) -> list[QHBoxLayout]:
    layouts = []

    title_layout = QHBoxLayout()
    label = QLabel(self._text.ATTRIBUTES)
    label = upper_font(label)
    label = bold_font(label)
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
    label = upper_font(label)
    return label


def create_agility_widget(self) -> QLabel:
    label = QLabel(
        self._text.AGILITY + str(self._attributes.AGILITY)
    )
    label = upper_font(label)
    return label


def create_vitality_widget(self) -> QLabel:
    label = QLabel(
        self._text.VITALITY + str(self._attributes.VITALITY)
    )
    label = upper_font(label)
    return label


def create_endurance_widget(self) -> QLabel:
    label = QLabel(
        self._text.ENDURANCE + str(self._attributes.ENDURANCE)
    )
    label = upper_font(label)
    return label


def create_attribute_points_widget(self) -> QLabel:
    label = QLabel(
        self._text.ATTRIBUTE_POINTS
        + str(self._attributes.ATTRIBUTE_POINTS)
    )
    label = upper_font(label)
    return label


def create_stats_widget(self) -> list:
    lines = []
    label = QLabel(self._text.STATS)
    label = upper_font(label)
    label = bold_font(label)
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
    label = upper_font(label)
    return label


def create_accuracy_widget(self) -> QLabel:
    label = QLabel(
        self._text.ACCURACY
        + str(self._main_character_stats[cs.ACCURACY] * 100)
        + "%"
    )
    label = upper_font(label)
    return label


def create_critical_strike_chance_widget(self) -> QLabel:
    label = QLabel(
        self._text.CRITICAL_STRIKE_CHANCE
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_CHANCE] * 100)
        + "%"
    )
    label = upper_font(label)
    return label


def create_critical_strike_multiplier_widget(self) -> QLabel:
    label = QLabel(
        self._text.CRITICAL_STRIKE_MULTIPLIER
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_MULTIPLIER])
    )
    label = upper_font(label)
    return label
