from PyQt6.QtWidgets import QLabel
from interface.common import upper_font, bold_font
from core.constants import (
    AttributesNames as an,
    BarsNames as bn,
    CombatStatsNames as cs,
    MainStatsNames as msn
)


def create_general_lines(self) -> None:
    label = QLabel(self._text.GENERAL)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_name_line(self)
    create_level_line(self)
    create_class_line(self)


def create_name_line(self) -> None:
    label = QLabel(self._text.NAME + self._main_character_stats[msn.NAME])
    label = upper_font(label)
    self._layout.addWidget(label)


def create_level_line(self) -> None:
    label = QLabel(
        self._text.LEVEL + str(self._main_character_stats[msn.LEVEL])
    )
    label = upper_font(label)

    self._layout.addWidget(label)


def create_class_line(self) -> None:
    label = QLabel(self._text.CLASS + self._main_character_stats[msn.CLASS])
    label = upper_font(label)
    self._layout.addWidget(label)


def create_bars_lines(self) -> None:
    label = QLabel(self._text.BARS)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_health_line(self)
    create_stamina_line(self)


def create_health_line(self) -> None:
    label = QLabel(
        self._text.HEALTH
        + str(self._main_character_stats[bn.MAX_HEALTH])
        + "/"
        + str(self._main_character_stats[bn.HEALTH])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_stamina_line(self) -> None:
    label = QLabel(
        self._text.STAMINA
        + str(self._main_character_stats[bn.MAX_STAMINA])
        + "/"
        + str(self._main_character_stats[bn.STAMINA])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_attributes_lines(self) -> None:
    label = QLabel(self._text.ATTRIBUTES)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_strength_line(self)
    create_agility_line(self)
    create_vitality_line(self)
    create_endurance_line(self)


def create_strength_line(self) -> None:
    label = QLabel(
        self._text.STRENGTH + str(self._main_character_stats[an.STRENGTH])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_agility_line(self) -> None:
    label = QLabel(
        self._text.AGILITY + str(self._main_character_stats[an.AGILITY])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_vitality_line(self) -> None:
    label = QLabel(
        self._text.VITALITY + str(self._main_character_stats[an.VITALITY])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_endurance_line(self) -> None:
    label = QLabel(
        self._text.ENDURANCE + str(self._main_character_stats[an.ENDURANCE])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_attribute_points_line(self) -> None:
    label = QLabel(
        self._text.ATTRIBUTE_POINTS
        + str(self._main_character_stats[an.ATTRIBUTE_POINTS])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_stats_lines(self) -> None:
    label = QLabel(self._text.STATS)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_damage_line(self)
    create_accuracy_line(self)
    create_critical_strike_chance_line(self)
    create_critical_strike_multiplier_line(self)


def create_damage_line(self) -> None:
    label = QLabel(
        self._text.DAMAGE
        + str(self._main_character_stats[cs.MIN_DAMAGE])
        + "-"
        + str(self._main_character_stats[cs.MAX_DAMAGE])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_accuracy_line(self) -> None:
    label = QLabel(
        self._text.ACCURACY
        + str(self._main_character_stats[cs.ACCURACY] * 100)
        + "%"
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_critical_strike_chance_line(self) -> None:
    label = QLabel(
        self._text.CRITICAL_STRIKE_CHANCE
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_CHANCE] * 100)
        + "%"
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_critical_strike_multiplier_line(self) -> None:
    label = QLabel(
        self._text.CRITICAL_STRIKE_MULTIPLIER
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_MULTIPLIER])
    )
    label = upper_font(label)
    self._layout.addWidget(label)
