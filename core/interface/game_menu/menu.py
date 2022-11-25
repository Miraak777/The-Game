from typing import Any, Dict

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QVBoxLayout, QWidget, QStackedLayout

from core.common import clear_layout, get_key_binds
from core.constants.actions_constants import ActionButtons
from core.constants.key_bind_constants import KeyBindNames
from core.constants.item_constants import ItemTypes
from core.enemies import Enemy

from . import widgets
from .texts import Text
from .constants import GameMenuSizes
from .stylesheets import game_window_stylesheet, label_stylesheet


class GameMenu(QFrame):
    def __init__(self, main_menu) -> None:
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(GameMenuSizes.GAME_WINDOW_SIZE)

        self.setStyleSheet(game_window_stylesheet)
        self._create_layout()

    def _create_layout(self) -> None:
        self._stacked_layout = QStackedLayout()
        self._layout = QGridLayout()
        self.setLayout(self._stacked_layout)
        widget = QWidget()
        widget.setFixedSize(GameMenuSizes.GAME_WINDOW_SIZE)
        widget.setLayout(self._layout)

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

        item_info_layout = QHBoxLayout()
        self.item_info_layout_widget = QWidget()
        self.item_info_layout_widget.setFixedSize(GameMenuSizes.ITEM_INFO_LAYOUT_SIZE)
        self.item_info_layout_widget.setLayout(item_info_layout)
        self.item_info_layout = QGridLayout()
        self.item_info_widget = QFrame()
        self.item_info_widget.setFixedSize(GameMenuSizes.ITEM_INFO_SIZE)
        self.item_info_widget.setLayout(self.item_info_layout)
        item_info_layout.addWidget(self.item_info_widget,
                                   alignment=Qt.AlignmentFlag.AlignRight)
        self._stacked_layout.addWidget(self.item_info_layout_widget)
        self.item_info_layout_widget.hide()
        self._stacked_layout.addWidget(widget)
        widget.show()

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

        self._health_bar.setMaximum(int(self._main_menu.main_character.max_health))
        self._health_bar.setValue(int(round(self._main_menu.main_character.health)))
        self._health_bar.setFormat(
            f"{self._main_menu.main_character.health}/{self._main_menu.main_character.max_health}")
        self._stamina_bar.setMaximum(int(self._main_menu.main_character.max_stamina))
        self._stamina_bar.setValue(int(round(self._main_menu.main_character.stamina)))
        self._stamina_bar.setFormat(f"{self._main_menu.main_character.stamina}/"
                                    f"{self._main_menu.main_character.max_stamina}")

    def refresh_enemy_bar(self, enemy: Enemy) -> None:
        max_health = enemy.max_health
        health = enemy.health
        self._enemy_bar.setMaximum(int(max_health))
        self._enemy_bar.setValue(int(health))
        self._enemy_bar.setFormat(f"{health}/{max_health}")

    def show_item_info(self, button):
        self.item_info_layout_widget.show()
        item = button.item
        color = button.rarity
        rarity = button.item.rarity
        rarity_map = {
            0: self._text.TRASH,
            1: self._text.COMMON,
            2: self._text.UNCOMMON,
            3: self._text.RARE,
            4: self._text.UNIQUE,
            5: self._text.LEGENDARY,
            6: self._text.RELIC,
            7: self._text.DIVINE,
        }
        self.item_info_widget.setStyleSheet(f"background-color: grey; border: 1px solid {color};")
        item_name_label = QLabel(item.name)
        item_name_label.setStyleSheet(
            f"color: {color}; background-color: rgba(0, 0, 0, 0); border: 0px; font: 16px;")
        self.item_info_layout.addWidget(item_name_label, 0, 0,
                                        alignment=(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft))

        rarity_label = QLabel(rarity_map[rarity])
        rarity_label.setStyleSheet(f"color: {color}; background-color: rgba(0, 0, 0, 0); border: 0px;")
        self.item_info_layout.addWidget(rarity_label, 0, 1,
                                        alignment=(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight))
        if item.item_type == ItemTypes.WEAPON:
            damage_label = QLabel(f"{self._text.DAMAGE}: {round(item.min_damage, 2)}-{round(item.max_damage, 2)}")
            damage_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 0px;")
            self.item_info_layout.addWidget(damage_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)

            stamina_consumption_label = QLabel(
                f"{self._text.STAMINA_CONSUMPTION}: {round(item.stamina_consumption, 2)}")
            self.item_info_layout.addWidget(stamina_consumption_label, 2, 0, alignment=Qt.AlignmentFlag.AlignLeft)

            stamina_consumption_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 0px;")
            level_label = QLabel(f"{self._text.LEVEL} {item.level}")
            level_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 0px;")
            self.item_info_layout.addWidget(level_label, 3, 1,
                                            alignment=(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight))

        elif item.item_type == ItemTypes.CONSUMABLE:
            if item.consumable_type == ItemTypes.FOOD:
                restore_label = QLabel(f"{self._text.RESTORES} {item.restore_value}% {self._text.HEALTH}")
                restore_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: 0px;")
                self.item_info_layout.addWidget(restore_label, 1, 0, alignment=Qt.AlignmentFlag.AlignLeft)

    def hide_item_info(self):
        clear_layout(self.item_info_layout)
        self.item_info_layout_widget.hide()

    def event_hover_item_show(self, hover):
        button = self.sender()
        if hover == "enterEvent":
            self.show_item_info(button)
        elif hover == "leaveEvent":
            self.hide_item_info()
