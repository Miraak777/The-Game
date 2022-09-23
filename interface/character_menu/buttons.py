from PyQt6.QtWidgets import QPushButton
from core.constants.character_constants import AttributesNames as an
from .stylesheets import add_button_stylesheet, remove_button_stylesheet, accept_button_stylesheet
from .constants import CharacterMenuButtons


def create_strength_adding_button(self) -> QPushButton:
    strength_adding_button = QPushButton()
    strength_adding_button.setStyleSheet(add_button_stylesheet)
    strength_adding_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    strength_adding_button.setCheckable(True)
    strength_adding_button.clicked.connect(self._event_add_strength)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        strength_adding_button.setDisabled(True)
    else:
        strength_adding_button.setDisabled(False)
    return strength_adding_button


def create_agility_adding_button(self) -> QPushButton:
    agility_adding_button = QPushButton()
    agility_adding_button.setStyleSheet(add_button_stylesheet)
    agility_adding_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    agility_adding_button.setCheckable(True)
    agility_adding_button.clicked.connect(self._event_add_agility)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        agility_adding_button.setDisabled(True)
    else:
        agility_adding_button.setDisabled(False)
    return agility_adding_button


def create_vitality_adding_button(self) -> QPushButton:
    vitality_adding_button = QPushButton()
    vitality_adding_button.setStyleSheet(add_button_stylesheet)
    vitality_adding_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    vitality_adding_button.setCheckable(True)
    vitality_adding_button.clicked.connect(self._event_add_vitality)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        vitality_adding_button.setDisabled(True)
    else:
        vitality_adding_button.setDisabled(False)
    return vitality_adding_button


def create_endurance_adding_button(self) -> QPushButton:
    endurance_adding_button = QPushButton()
    endurance_adding_button.setStyleSheet(add_button_stylesheet)
    endurance_adding_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    endurance_adding_button.setCheckable(True)
    endurance_adding_button.clicked.connect(self._event_add_endurance)
    if self._attributes.ATTRIBUTE_POINTS == 0:
        endurance_adding_button.setDisabled(True)
    else:
        endurance_adding_button.setDisabled(False)
    return endurance_adding_button


def create_strength_removing_button(self) -> QPushButton:
    strength_removing_button = QPushButton()
    strength_removing_button.setStyleSheet(remove_button_stylesheet)
    strength_removing_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    strength_removing_button.setCheckable(True)
    strength_removing_button.clicked.connect(self._event_remove_strength)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS] \
            or self._attributes.STRENGTH == 0:
        strength_removing_button.setDisabled(True)
    else:
        strength_removing_button.setDisabled(False)
    return strength_removing_button


def create_agility_removing_button(self) -> QPushButton:
    agility_removing_button = QPushButton()
    agility_removing_button.setStyleSheet(remove_button_stylesheet)
    agility_removing_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    agility_removing_button.setCheckable(True)
    agility_removing_button.clicked.connect(self._event_remove_agility)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS] \
            or self._attributes.AGILITY == 0:
        agility_removing_button.setDisabled(True)
    else:
        agility_removing_button.setDisabled(False)
    return agility_removing_button


def create_vitality_removing_button(self) -> QPushButton:
    vitality_removing_button = QPushButton()
    vitality_removing_button.setStyleSheet(remove_button_stylesheet)
    vitality_removing_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    vitality_removing_button.setCheckable(True)
    vitality_removing_button.clicked.connect(self._event_remove_vitality)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS] \
            or self._attributes.VITALITY == 0:
        vitality_removing_button.setDisabled(True)
    else:
        vitality_removing_button.setDisabled(False)
    return vitality_removing_button


def create_endurance_removing_button(self) -> QPushButton:
    endurance_removing_button = QPushButton()
    endurance_removing_button.setStyleSheet(remove_button_stylesheet)
    endurance_removing_button.setFixedSize(CharacterMenuButtons.ATTRIBUTE_BUTTON)
    endurance_removing_button.setCheckable(True)
    endurance_removing_button.clicked.connect(self._event_remove_endurance)
    if self._attributes.ATTRIBUTE_POINTS == self._main_character_stats[an.ATTRIBUTE_POINTS] \
            or self._attributes.ENDURANCE == 0:
        endurance_removing_button.setDisabled(True)
    else:
        endurance_removing_button.setDisabled(False)
    return endurance_removing_button


def create_accept_button(self) -> QPushButton:
    accept_button = QPushButton(text=self._text.ACCEPT)
    accept_button.setStyleSheet(accept_button_stylesheet)
    accept_button.setFixedSize(CharacterMenuButtons.ACCEPT_BUTTON)
    accept_button.setCheckable(True)
    accept_button.clicked.connect(self._event_accept)
    if is_attributes_changed(self) and self._main_character_stats[an.ATTRIBUTE_POINTS] != 0:
        accept_button.setEnabled(True)
    else:
        accept_button.setEnabled(False)
    return accept_button


def is_attributes_changed(self) -> bool:
    rules = (
        self._attributes.STRENGTH != self._main_character_stats[an.STRENGTH],
        self._attributes.AGILITY != self._main_character_stats[an.AGILITY],
        self._attributes.VITALITY != self._main_character_stats[an.VITALITY],
        self._attributes.ENDURANCE != self._main_character_stats[an.ENDURANCE],
    )
    if True in rules:
        return True
    else:
        return False

