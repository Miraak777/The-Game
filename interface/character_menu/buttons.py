from core.constants.button_size_constants import CharacterMenuButtons
from PyQt6.QtWidgets import QPushButton
from interface.common import set_button_and_icon_sizes
from core.constants import AttributesNames as an


def create_strength_button(self) -> QPushButton:
    strength_button = QPushButton()
    strength_button = set_button_and_icon_sizes(strength_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    strength_button.setCheckable(True)
    strength_button.clicked.connect(self._event_add_strength)
    if self._main_character_stats[an.ATTRIBUTE_POINTS] == 0:
        strength_button.setDisabled(True)
    else:
        strength_button.setDisabled(False)
    return strength_button


def create_agility_button(self) -> QPushButton:
    agility_button = QPushButton()
    agility_button = set_button_and_icon_sizes(agility_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    agility_button.setCheckable(True)
    agility_button.clicked.connect(self._event_add_agility)
    if self._main_character_stats[an.ATTRIBUTE_POINTS] == 0:
        agility_button.setDisabled(True)
    else:
        agility_button.setDisabled(False)
    return agility_button


def create_vitality_button(self) -> QPushButton:
    vitality_button = QPushButton()
    vitality_button = set_button_and_icon_sizes(vitality_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    vitality_button.setCheckable(True)
    vitality_button.clicked.connect(self._event_add_vitality)
    if self._main_character_stats[an.ATTRIBUTE_POINTS] == 0:
        vitality_button.setDisabled(True)
    else:
        vitality_button.setDisabled(False)
    return vitality_button


def create_endurance_button(self) -> QPushButton:
    endurance_button = QPushButton()
    endurance_button = set_button_and_icon_sizes(endurance_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    endurance_button.setCheckable(True)
    endurance_button.clicked.connect(self._event_add_endurance)
    if self._main_character_stats[an.ATTRIBUTE_POINTS] == 0:
        endurance_button.setDisabled(True)
    else:
        endurance_button.setDisabled(False)
    return endurance_button
