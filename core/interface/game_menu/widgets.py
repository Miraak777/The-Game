from typing import Callable
from functools import partial

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QProgressBar, QPushButton, QScrollArea, QWidget, QHBoxLayout, QGridLayout

from .constants import GameMenuButtons, GameMenuSizes
from .stylesheets import enemy_bar_stylesheet, health_bar_stylesheet, scroll_area_stylesheet, stamina_bar_stylesheet


def create_scroll_area(self) -> QScrollArea:
    scroll_area = QScrollArea()
    scroll_area.setStyleSheet(scroll_area_stylesheet)
    scroll_area.setFixedSize(GameMenuSizes.SCROLL_AREA_SIZE)
    scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    scroll_area.setWidgetResizable(True)
    return scroll_area


def create_action_button(event: Callable, text: str, action_button_number: int) -> QPushButton:
    button = QPushButton(text=text)
    button.setFixedSize(GameMenuButtons.ACTION_BUTTON_SIZE)
    button.clicked.connect(partial(event, action_button_number))
    if text == "":
        button.setEnabled(False)
    return button


def create_health_bar() -> QProgressBar:
    progress_bar = QProgressBar()
    progress_bar.setFixedSize(GameMenuSizes.CHARACTER_BARS_SIZE)
    progress_bar.setStyleSheet(health_bar_stylesheet)
    progress_bar.setMaximum(1)
    progress_bar.setMinimum(0)
    progress_bar.setValue(1)
    progress_bar.setDisabled(True)
    progress_bar.setFormat(str(progress_bar.value()) + "/" + str(progress_bar.maximum()))
    return progress_bar


def create_stamina_bar() -> QProgressBar:
    progress_bar = QProgressBar()
    progress_bar.setFixedSize(GameMenuSizes.CHARACTER_BARS_SIZE)
    progress_bar.setStyleSheet(stamina_bar_stylesheet)
    progress_bar.setMaximum(1)
    progress_bar.setMinimum(0)
    progress_bar.setValue(1)
    progress_bar.setDisabled(True)
    progress_bar.setFormat(str(progress_bar.value()) + "/" + str(progress_bar.maximum()))
    return progress_bar


def create_enemy_health_bar() -> QProgressBar:
    progress_bar = QProgressBar()
    progress_bar.setFixedSize(GameMenuSizes.ENEMY_BAR_SIZE)
    progress_bar.setStyleSheet(enemy_bar_stylesheet)
    progress_bar.setMaximum(1)
    progress_bar.setMinimum(0)
    progress_bar.setValue(1)
    progress_bar.setDisabled(True)
    progress_bar.setFormat(str(progress_bar.value()) + "/" + str(progress_bar.maximum()))
    return progress_bar
