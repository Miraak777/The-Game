from PyQt6.QtWidgets import QFrame, QGridLayout, QWidget, QVBoxLayout, QPushButton
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
        button = QPushButton("First action")
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 0, 0)
        button = QPushButton("Second action")
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 0, 1)
        button = QPushButton("Third action")
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 1, 0)
        button = QPushButton("Fourth action")
        button.setFixedSize(GameWindowButtons.ACTION_BUTTON_SIZE)
        self.buttons_layout.addWidget(button, 1, 1)
        self._layout.addLayout(self.buttons_layout, 1, 0, alignment=Qt.AlignmentFlag.AlignBottom)
        self._layout.addWidget(self._scroll_area, 0, 0, alignment=Qt.AlignmentFlag.AlignLeft)
        self.setLayout(self._layout)

