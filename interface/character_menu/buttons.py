from core.constants.button_size_constants import CharacterMenuButtons
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from interface.common import set_button_and_icon_sizes
from core.constants.character_constants import AttributesNames as an
from core.constants.path_constants import Paths


def create_strength_adding_button(self) -> QPushButton:
    strength_adding_button = QPushButton(icon=QIcon(Paths.ADDING_ICON))
    strength_adding_button = set_button_and_icon_sizes(strength_adding_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    strength_adding_button.setCheckable(True)
    strength_adding_button.clicked.connect(self._event_add_strength)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        strength_adding_button.setDisabled(True)
    else:
        strength_adding_button.setDisabled(False)
    return strength_adding_button


def create_agility_adding_button(self) -> QPushButton:
    agility_adding_button = QPushButton(icon=QIcon(Paths.ADDING_ICON))
    agility_adding_button = set_button_and_icon_sizes(agility_adding_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    agility_adding_button.setCheckable(True)
    agility_adding_button.clicked.connect(self._event_add_agility)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        agility_adding_button.setDisabled(True)
    else:
        agility_adding_button.setDisabled(False)
    return agility_adding_button


def create_vitality_adding_button(self) -> QPushButton:
    vitality_adding_button = QPushButton(icon=QIcon(Paths.ADDING_ICON))
    vitality_adding_button = set_button_and_icon_sizes(vitality_adding_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    vitality_adding_button.setCheckable(True)
    vitality_adding_button.clicked.connect(self._event_add_vitality)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        vitality_adding_button.setDisabled(True)
    else:
        vitality_adding_button.setDisabled(False)
    return vitality_adding_button


def create_endurance_adding_button(self) -> QPushButton:
    endurance_adding_button = QPushButton(icon=QIcon(Paths.ADDING_ICON))
    endurance_adding_button = set_button_and_icon_sizes(endurance_adding_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    endurance_adding_button.setCheckable(True)
    endurance_adding_button.clicked.connect(self._event_add_endurance)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        endurance_adding_button.setDisabled(True)
    else:
        endurance_adding_button.setDisabled(False)
    return endurance_adding_button


def create_strength_removing_button(self) -> QPushButton:
    strength_removing_button = QPushButton(icon=QIcon(Paths.REMOVING_ICON))
    strength_removing_button = set_button_and_icon_sizes(strength_removing_button,
                                                         CharacterMenuButtons.ATTRIBUTE_BUTTON)
    strength_removing_button.setCheckable(True)
    strength_removing_button.clicked.connect(self._event_remove_strength)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS] \
            or self._attributes.STRENGTH == 0:
        strength_removing_button.setDisabled(True)
    else:
        strength_removing_button.setDisabled(False)
    return strength_removing_button


def create_agility_removing_button(self) -> QPushButton:
    agility_removing_button = QPushButton(icon=QIcon(Paths.REMOVING_ICON))
    agility_removing_button = set_button_and_icon_sizes(agility_removing_button, CharacterMenuButtons.ATTRIBUTE_BUTTON)
    agility_removing_button.setCheckable(True)
    agility_removing_button.clicked.connect(self._event_remove_agility)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS]\
            or self._attributes.AGILITY == 0:
        agility_removing_button.setDisabled(True)
    else:
        agility_removing_button.setDisabled(False)
    return agility_removing_button


def create_vitality_removing_button(self) -> QPushButton:
    vitality_removing_button = QPushButton(icon=QIcon(Paths.REMOVING_ICON))
    vitality_removing_button = set_button_and_icon_sizes(vitality_removing_button,
                                                         CharacterMenuButtons.ATTRIBUTE_BUTTON)
    vitality_removing_button.setCheckable(True)
    vitality_removing_button.clicked.connect(self._event_remove_vitality)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS]\
            or self._attributes.VITALITY == 0:
        vitality_removing_button.setDisabled(True)
    else:
        vitality_removing_button.setDisabled(False)
    return vitality_removing_button


def create_endurance_removing_button(self) -> QPushButton:
    endurance_removing_button = QPushButton(icon=QIcon(Paths.REMOVING_ICON))
    endurance_removing_button = set_button_and_icon_sizes(endurance_removing_button,
                                                          CharacterMenuButtons.ATTRIBUTE_BUTTON)
    endurance_removing_button.setCheckable(True)
    endurance_removing_button.clicked.connect(self._event_remove_endurance)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS]\
            or self._attributes.ENDURANCE == 0:
        endurance_removing_button.setDisabled(True)
    else:
        endurance_removing_button.setDisabled(False)
    return endurance_removing_button


def create_accept_button(self) -> QPushButton:
    accept_button = QPushButton(text=self._text.ACCEPT)
    accept_button = set_button_and_icon_sizes(accept_button, CharacterMenuButtons.ACCEPT_BUTTON)
    accept_button.setCheckable(True)
    accept_button.clicked.connect(self._event_accept)
    if self._attributes.ATTRIBUTE_POINTS != 0 or self._actual_attribute_points == 0:
        accept_button.setDisabled(True)
    else:
        accept_button.setDisabled(False)
    return accept_button
