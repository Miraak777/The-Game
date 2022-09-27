from PyQt6.QtWidgets import QScrollArea, QPushButton
from PyQt6.QtCore import Qt
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


def create_action_button(event, text: str) -> QPushButton:
    button = QPushButton(text=text)
    button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
    button.clicked.connect(event)
    return button
