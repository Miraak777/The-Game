from typing import Any, Dict

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget

from core.common import clear_layout, get_key_binds
from core.constants.actions_constants import ActionButtons
from core.constants.character_constants import BarsNames as bn
from core.constants.key_bind_constants import KeyBindNames
from core.enemies import Enemy

from . import widgets
from .constants import GameMenuSizes
from .stylesheets import game_window_stylesheet, label_stylesheet


class GameMenu(QFrame):
    def __init__(self, main_menu: QMainWindow) -> None:
        super().__init__()
        self._main_menu = main_menu
        self.setFixedSize(GameMenuSizes.GAME_WINDOW_SIZE)

        self.setStyleSheet(game_window_stylesheet)
        self._create_layout()

    def _create_layout(self) -> None:
        self._layout = QGridLayout()

        self._enemy_bar = widgets.create_enemy_health_bar()
        self._layout.addWidget(self._enemy_bar, 0, 0)

        self._scroll_area_layout = QVBoxLayout()
        self._scroll_area = widgets.create_scroll_area(self)
        self._scroll_area_widget = QWidget()
        self._scroll_area_widget.setLayout(self._scroll_area_layout)
        self._scroll_area.setWidget(self._scroll_area_widget)
        self._scroll_area_layout.addStretch()
        self._layout.addWidget(self._scroll_area, 1, 0)

        self._bars_layout = QHBoxLayout()
        self._health_bar = widgets.create_health_bar()
        self._stamina_bar = widgets.create_stamina_bar()
        self._bars_layout.addWidget(self._health_bar)
        self._bars_layout.addWidget(self._stamina_bar)
        self._layout.addLayout(self._bars_layout, 2, 0)

        self.buttons_layout = QGridLayout()
        self._layout.addLayout(self.buttons_layout, 3, 0)

        self.setLayout(self._layout)

    def add_log(self, text: str) -> None:
        label = QLabel(text=text)
        label.setStyleSheet(label_stylesheet)
        label.setWordWrap(True)
        self._scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self.scroll_down()

    def scroll_down(self) -> None:
        scroll_bar = self._scroll_area.verticalScrollBar()
        scroll_bar.rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))

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

    def refresh_character_bars(self) -> None:
        stats = self._main_menu.main_character.get_stats()
        self._health_bar.setMaximum(int(stats[bn.MAX_HEALTH]))
        self._health_bar.setValue(int(round(stats[bn.HEALTH])))
        self._health_bar.setFormat(str(stats[bn.HEALTH]) + "/" + str(stats[bn.MAX_HEALTH]))
        self._stamina_bar.setMaximum(int(stats[bn.MAX_STAMINA]))
        self._stamina_bar.setValue(int(round(stats[bn.STAMINA])))
        self._stamina_bar.setFormat(str(stats[bn.STAMINA]) + "/" + str(stats[bn.MAX_STAMINA]))

    def refresh_enemy_bar(self, enemy: Enemy) -> None:
        max_health = enemy.max_health
        health = enemy.health
        self._enemy_bar.setMaximum(int(max_health))
        self._enemy_bar.setValue(int(health))
        self._enemy_bar.setFormat(str(health) + "/" + str(max_health))
