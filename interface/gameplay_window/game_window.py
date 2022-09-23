from PyQt6.QtWidgets import QFrame, QGridLayout, QLabel, QVBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from .texts import Text
from .constants import GameWindowSizes, GameWindowButtons
from .stylesheets import game_window_stylesheet
from . import widgets


class GameWindow(QFrame):
    def __init__(self, main_menu):
        super().__init__()
        self._main_menu = main_menu
        self._text = Text[self._main_menu.language]
        self.setFixedSize(GameWindowSizes.GAME_WINDOW_SIZE)

        self.setStyleSheet(game_window_stylesheet)
        self._create_layout()

    def _create_layout(self):
        self._layout = QGridLayout()
        self.scroll_area_layout = QVBoxLayout()
        self._scroll_area = widgets.create_scroll_area(self)
        self._scroll_area.setWidgetResizable(True)
        self._scroll_area.setLayout(self.scroll_area_layout)
        self.buttons_layout = QGridLayout()
        button = QPushButton("Get 1000 Xp")
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        button.clicked.connect(self._event_give_some_exp)
        self.buttons_layout.addWidget(button, 0, 0)
        button = QPushButton("Become Peasant")
        button.clicked.connect(self._event_set_class_peasant)
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 0, 1)
        button = QPushButton("Become Warrior")
        button.clicked.connect(self._event_set_class_warrior)
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 1, 0)
        button = QPushButton("Become Assassin")
        button.clicked.connect(self._event_set_class_assassin)
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 1, 1)
        self._layout.addLayout(self.buttons_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self._layout.addWidget(self._scroll_area, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self._layout)

    def _event_give_some_exp(self):
        self._main_menu.main_character.send_experience(1000)
        self._main_menu.character_menu.set_actual_character_stats()
        label = QLabel(text="Gained 1000 xp!")
        self.scroll_area_layout.addWidget(label)

    def _event_set_class_peasant(self):
        self._main_menu.main_character.set_class_peasant()
        self._main_menu.character_menu.set_actual_character_stats()
        label = QLabel(text="You're now Peasant!")
        self.scroll_area_layout.addWidget(label)

    def _event_set_class_warrior(self):
        self._main_menu.main_character.set_class_warrior()
        self._main_menu.character_menu.set_actual_character_stats()
        label = QLabel(text="You're now Warrior!")
        self.scroll_area_layout.addWidget(label)

    def _event_set_class_assassin(self):
        self._main_menu.main_character.set_class_assassin()
        self._main_menu.character_menu.set_actual_character_stats()
        label = QLabel(text="You're now Assassin!")
        self.scroll_area_layout.addWidget(label)
