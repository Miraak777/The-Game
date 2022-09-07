from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QImage, QPalette
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from core.constants.path_constants import Paths
from core.constants.windows_constants import WindowSizes
from main_character import MainCharacter
from interface.interface_language.character_menu_text import Text
import interface.character_menu.lines_creation as lines
from interface.common import clear_layout


class CharacterMenu(QWidget):
    def __init__(self, main_character: MainCharacter, language: str):
        super().__init__()
        self._text = Text[language]
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)
        self._create_background()
        self._create_layout(main_character)

    def _create_background(self) -> None:
        self.setAutoFillBackground(True)
        background_image = QImage(Paths.CHARACTER_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.CHARACTER_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def refresh_character_menu(self, main_character: MainCharacter) -> None:
        clear_layout(self._layout)
        self._create_lines(main_character)

    def _create_lines(self, main_character: MainCharacter) -> None:
        self._main_character = main_character
        self._main_character_stats = self._main_character.get_stats()
        lines.create_general_lines(self)
        lines.create_bars_lines(self)
        lines.create_attributes_lines(self)
        lines.create_stats_lines(self)

    def _create_layout(self, main_character: MainCharacter) -> None:
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._create_lines(main_character)
        self.setLayout(self._layout)
