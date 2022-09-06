from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QIcon, QImage, QPalette
from PyQt6.QtWidgets import QVBoxLayout, QWidget
from core.constants.path_constants import Paths
from interface.interface_language.en_lang import CharacterMenuText
from core.constants.windows_constants import WindowSizes
from main_character import MainCharacter
import interface.character_menu.lines_creation as lines


class CharacterMenu(QWidget):
    def __init__(self, main_character: MainCharacter):
        super().__init__()
        self.setAutoFillBackground(True)
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)
        self._create_background()
        self._create_layout(main_character)

    def _create_background(self):
        background_image = QImage(Paths.CHARACTER_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.CHARACTER_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def refresh_character_menu(self, main_character: MainCharacter):
        item_list = list(range(self._layout.count()))
        item_list.reverse()
        for i in item_list:
            item = self._layout.itemAt(i)
            self._layout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()
        self._create_lines(main_character)

    def _create_lines(self, main_character: MainCharacter) -> None:
        self._main_character = main_character
        self._main_character_stats = self._main_character.get_stats()
        lines.create_general_lines(self)
        lines.create_bars_lines(self)
        lines.create_attributes_lines(self)
        lines.create_stats_lines(self)

    def _create_layout(self, main_character: MainCharacter):
        self._layout = QVBoxLayout()
        self._layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._create_lines(main_character)
        self.setLayout(self._layout)
