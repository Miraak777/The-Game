from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel, QVBoxLayout,  QWidget
from PyQt6.QtCore import Qt
from .texts import Text
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
        self.scroll_area_layout = QVBoxLayout()
        self._scroll_area = widgets.create_scroll_area(self)
        widget = QWidget()
        widget.setLayout(self.scroll_area_layout)
        self._scroll_area.setWidget(widget)
        self.buttons_layout = QGridLayout()

        buttons = widgets.create_debug_buttons(self)
        self.buttons_layout.addWidget(buttons[0], 0, 0)
        self.buttons_layout.addWidget(buttons[1], 0, 1)
        self.buttons_layout.addWidget(buttons[2], 1, 0)
        self.buttons_layout.addWidget(buttons[3], 1, 1)

        self._layout.addLayout(self.buttons_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self._layout.addWidget(self._scroll_area, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.scroll_area_layout.addStretch()
        self.setLayout(self._layout)

    def _event_give_some_exp(self):
        label = QLabel(text="Gained 1000 xp!")
        label.setStyleSheet(label_stylesheet)
        label.setFixedHeight(30)
        self.scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self._main_menu.main_character.send_experience(1000, self._main_menu)
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_peasant(self):
        label = QLabel(text="You're now Peasant!")
        label.setStyleSheet(label_stylesheet)
        label.setFixedHeight(30)
        self.scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self._main_menu.main_character.set_class_peasant()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_warrior(self):
        label = QLabel(text="You're now Warrior!")
        label.setStyleSheet(label_stylesheet)
        label.setFixedHeight(30)
        self.scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()

    def _event_set_class_assassin(self):
        label = QLabel(text="You're now Assassin!")
        label.setStyleSheet(label_stylesheet)
        label.setFixedHeight(30)
        self.scroll_area_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignBottom)
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()
