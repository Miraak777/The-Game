from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel, QVBoxLayout,  QWidget
from PyQt6.QtCore import Qt, QTimer
from functools import partial
from typing import Any, Dict
from interface.common import clear_layout
from .texts import Text
from interface.common import get_key_binds
from core.constants.key_bind_constants import KeyBindNames
from core.constants.actions_constants import ActionButtons
from .constants import GameWindowSizes
from .stylesheets import game_window_stylesheet, label_stylesheet
from . import widgets


class GameWindow(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(GameWindowSizes.GAME_WINDOW_SIZE)

        self.setStyleSheet(game_window_stylesheet)
        self._create_layout()
        self.hide()

    def _create_layout(self):
        self._layout = QGridLayout()
        self._scroll_area_layout = QVBoxLayout()
        self._scroll_area_layout.addStretch()
        self._scroll_area = widgets.create_scroll_area(self)
        widget = QWidget()
        widget.setLayout(self._scroll_area_layout)
        self._scroll_area.setWidget(widget)
        self._layout.addWidget(self._scroll_area, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)

        self.buttons_layout = QGridLayout()
        self._layout.addLayout(self.buttons_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)

        self.setLayout(self._layout)

    def add_log(self, text: str):
        label = QLabel(text=text)
        label.setStyleSheet(label_stylesheet)
        label.setFixedHeight(30)
        self._scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self.scroll_down()

    def scroll_down(self):
        scroll_bar = self._scroll_area.verticalScrollBar()
        scroll_bar.setValue(scroll_bar.maximum())

    def set_action_buttons(self, events: Dict[str, Any], texts: Dict[str, Any]) -> None:
        clear_layout(self.buttons_layout)
        button = widgets.create_action_button(events[ActionButtons.FIRST_ACTION], texts[ActionButtons.FIRST_ACTION])
        button.setShortcut(get_key_binds()[KeyBindNames.FIRST_ACTION])
        self.buttons_layout.addWidget(button, 0, 0)

        button = widgets.create_action_button(events[ActionButtons.SECOND_ACTION], texts[ActionButtons.SECOND_ACTION])
        button.setShortcut(get_key_binds()[KeyBindNames.SECOND_ACTION])
        self.buttons_layout.addWidget(button, 0, 1)

        button = widgets.create_action_button(events[ActionButtons.THIRD_ACTION], texts[ActionButtons.THIRD_ACTION])
        button.setShortcut(get_key_binds()[KeyBindNames.THIRD_ACTION])
        self.buttons_layout.addWidget(button, 1, 0)

        button = widgets.create_action_button(events[ActionButtons.FOURTH_ACTION], texts[ActionButtons.FOURTH_ACTION])
        button.setShortcut(get_key_binds()[KeyBindNames.FOURTH_ACTION])
        self.buttons_layout.addWidget(button, 1, 1)

