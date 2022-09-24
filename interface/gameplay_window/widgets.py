from PyQt6.QtWidgets import QScrollArea, QPushButton
from PyQt6.QtCore import Qt
from interface.common import get_key_binds
from core.constants.key_bind_constants import KeyBindNames
from .stylesheets import scroll_area_stylesheet
from .constants import GameWindowSizes, GameWindowButtons


def create_scroll_area(self) -> QScrollArea:
    scroll_area = QScrollArea()
    scroll_area.setStyleSheet(scroll_area_stylesheet)
    scroll_area.setFixedSize(GameWindowSizes.SCROLL_AREA_SIZE)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll_area.setWidgetResizable(True)
    return scroll_area


def create_debug_buttons(self) -> list:
    buttons = []
    button = QPushButton("Get 1000 Xp")
    button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
    button.clicked.connect(self._event_give_some_exp)
    button.setShortcut(get_key_binds()[KeyBindNames.FIRST_ACTION])
    buttons.append(button)

    button = QPushButton("Become Peasant")
    button.clicked.connect(self._event_set_class_peasant)
    button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
    button.setShortcut(get_key_binds()[KeyBindNames.SECOND_ACTION])
    buttons.append(button)

    button = QPushButton("Become Warrior")
    button.clicked.connect(self._event_set_class_warrior)
    button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
    button.setShortcut(get_key_binds()[KeyBindNames.THIRD_ACTION])
    buttons.append(button)

    button = QPushButton("Become Assassin")
    button.clicked.connect(self._event_set_class_assassin)
    button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
    button.setShortcut(get_key_binds()[KeyBindNames.FOURTH_ACTION])
    buttons.append(button)

    return buttons
