from PyQt6.QtWidgets import QHBoxLayout, QLabel
from interface.interface_language.en_lang import CharacterMenuText
from core.constants.windows_constants import WindowsFonts
from core.constants import (
    AttributesNames as an,
    BarsNames as bn,
    CombatStatsNames as cs,
    MainStatsNames as msn
)


def upper_font(label: QLabel) -> QLabel:
    font = label.font()
    font.setPointSize(WindowsFonts.FONT_SIZE)
    label.setFont(font)
    return label


def bold_font(label: QLabel) -> QLabel:
    font = label.font()
    font.setBold(True)
    label.setFont(font)
    return label


def create_general_lines(self) -> None:
    label = QLabel(CharacterMenuText.GENERAL)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_name_line(self)
    create_level_line(self)
    create_class_line(self)


def create_name_line(self):
    label = QLabel(CharacterMenuText.NAME + self._main_character_stats[msn.NAME])
    label = upper_font(label)
    self._layout.addWidget(label)


def create_level_line(self):
    label = QLabel(
        CharacterMenuText.LEVEL + str(self._main_character_stats[msn.LEVEL])
    )
    label = upper_font(label)

    self._layout.addWidget(label)


def create_class_line(self):
    label = QLabel(CharacterMenuText.CLASS + self._main_character_stats[msn.CLASS])
    label = upper_font(label)
    self._layout.addWidget(label)


def create_bars_lines(self):
    label = QLabel(CharacterMenuText.BARS)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_health_line(self)

    create_stamina_line(self)


def create_health_line(self):
    label = QLabel(
        CharacterMenuText.HEALTH
        + str(self._main_character_stats[bn.MAX_HEALTH])
        + "/"
        + str(self._main_character_stats[bn.HEALTH])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_stamina_line(self):
    label = QLabel(
        CharacterMenuText.STAMINA
        + str(self._main_character_stats[bn.MAX_STAMINA])
        + "/"
        + str(self._main_character_stats[bn.STAMINA])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_attributes_lines(self):
    label = QLabel(CharacterMenuText.ATTRIBUTES)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_strength_line(self)
    create_agility_line(self)
    create_vitality_line(self)
    create_endurance_line(self)


def create_strength_line(self):
    label = QLabel(
        CharacterMenuText.STRENGTH + str(self._main_character_stats[an.STRENGTH])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_agility_line(self):
    label = QLabel(
        CharacterMenuText.AGILITY + str(self._main_character_stats[an.AGILITY])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_vitality_line(self):
    label = QLabel(
        CharacterMenuText.VITALITY + str(self._main_character_stats[an.VITALITY])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_endurance_line(self):
    label = QLabel(
        CharacterMenuText.ENDURANCE + str(self._main_character_stats[an.ENDURANCE])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_attribute_points_line(self):
    label = QLabel(
        CharacterMenuText.ATTRIBUTE_POINTS
        + str(self._main_character_stats[an.ATTRIBUTE_POINTS])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_stats_lines(self):
    label = QLabel(CharacterMenuText.STATS)
    label = upper_font(label)
    label = bold_font(label)
    self._layout.addWidget(label)

    create_damage_line(self)
    create_accuracy_line(self)
    create_critical_strike_chance_line(self)
    create_critical_strike_multiplier_line(self)


def create_damage_line(self):
    label = QLabel(
        CharacterMenuText.DAMAGE
        + str(self._main_character_stats[cs.MIN_DAMAGE])
        + "-"
        + str(self._main_character_stats[cs.MAX_DAMAGE])
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_accuracy_line(self):
    label = QLabel(
        CharacterMenuText.ACCURACY
        + str(self._main_character_stats[cs.ACCURACY] * 100)
        + "%"
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_critical_strike_chance_line(self):
    label = QLabel(
        CharacterMenuText.CRITICAL_STRIKE_CHANCE
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_CHANCE] * 100)
        + "%"
    )
    label = upper_font(label)
    self._layout.addWidget(label)


def create_critical_strike_multiplier_line(self):
    label = QLabel(
        CharacterMenuText.CRITICAL_STRIKE_MULTIPLIER
        + str(self._main_character_stats[cs.CRITICAL_STRIKE_MULTIPLIER])
    )
    label = upper_font(label)
    self._layout.addWidget(label)
