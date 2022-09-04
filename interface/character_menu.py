from PyQt6.QtCore import Qt
from PyQt6.QtGui import QBrush, QIcon, QImage, QPalette
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QWidget

from core.constants.character_constants import AttributesNames as an
from core.constants.character_constants import BarsNames as bn
from core.constants.character_constants import CombatStats as cs
from core.constants.character_constants import MainStatsNames as msn
from core.constants.path_constants import Paths
from interface.interface_language.en_lang import CharacterMenuText
from interface.windows_parameters import WindowsFonts, WindowSizes
from main_character import MainCharacter


class CharacterMenu(QMainWindow):
    def __init__(self, main_character: MainCharacter):
        super().__init__()
        self._main_character = main_character
        self._main_character_stats = self._main_character.get_stats()

        self._character_menu_init()

        self._global_layout = QVBoxLayout()
        self._global_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self._create_lines()

        self._widget = QWidget()
        self._widget.setLayout(self._global_layout)
        self.setCentralWidget(self._widget)

    def _create_background(self):
        background_image = QImage(Paths.CHARACTER_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.CHARACTER_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

    def _character_menu_init(self):
        self.setWindowIcon(QIcon(Paths.CHARACTER_MENU_ICON))
        self.setWindowTitle(CharacterMenuText.TITLE)
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)
        self._create_background()

    @staticmethod
    def _upper_font(label: QLabel) -> QLabel:
        font = label.font()
        font.setPointSize(WindowsFonts.FONT_SIZE)
        label.setFont(font)
        return label

    @staticmethod
    def _bold_font(label: QLabel) -> QLabel:
        font = label.font()
        font.setBold(True)
        label.setFont(font)
        return label

    def _create_general_line(self):
        label = QLabel(CharacterMenuText.GENERAL)
        label = self._upper_font(label)
        label = self._bold_font(label)
        self._global_layout.addWidget(label)

    def _create_name_line(self):
        label = QLabel(CharacterMenuText.NAME + self._main_character_stats[msn.NAME])
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_level_line(self):
        label = QLabel(
            CharacterMenuText.LEVEL + str(self._main_character_stats[msn.LEVEL])
        )
        label = self._upper_font(label)

        self._global_layout.addWidget(label)

    def _create_class_line(self):
        label = QLabel(CharacterMenuText.CLASS + self._main_character_stats[msn.CLASS])
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_bars_line(self):
        label = QLabel(CharacterMenuText.BARS)
        label = self._upper_font(label)
        label = self._bold_font(label)
        self._global_layout.addWidget(label)

    def _create_health_line(self):
        label = QLabel(
            CharacterMenuText.HEALTH
            + str(self._main_character_stats[bn.HEALTH][0])
            + "/"
            + str(self._main_character_stats[bn.HEALTH][1])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_stamina_line(self):
        label = QLabel(
            CharacterMenuText.STAMINA
            + str(self._main_character_stats[bn.STAMINA][0])
            + "/"
            + str(self._main_character_stats[bn.STAMINA][1])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_attributes_line(self):
        label = QLabel(CharacterMenuText.ATTRIBUTES)
        label = self._upper_font(label)
        label = self._bold_font(label)
        self._global_layout.addWidget(label)

    def _create_strength_line(self):
        label = QLabel(
            CharacterMenuText.STRENGTH + str(self._main_character_stats[an.STRENGTH])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_agility_line(self):
        label = QLabel(
            CharacterMenuText.AGILITY + str(self._main_character_stats[an.AGILITY])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_vitality_line(self):
        label = QLabel(
            CharacterMenuText.VITALITY + str(self._main_character_stats[an.VITALITY])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_endurance_line(self):
        label = QLabel(
            CharacterMenuText.ENDURANCE + str(self._main_character_stats[an.ENDURANCE])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_attribute_points_line(self):
        label = QLabel(
            CharacterMenuText.ATTRIBUTE_POINTS
            + str(self._main_character_stats[an.ATTRIBUTE_POINTS])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_stats_line(self):
        label = QLabel(CharacterMenuText.STATS)
        label = self._upper_font(label)
        label = self._bold_font(label)
        self._global_layout.addWidget(label)

    def _create_damage_line(self):
        label = QLabel(
            CharacterMenuText.DAMAGE
            + str(self._main_character_stats[cs.MIN_DAMAGE])
            + "-"
            + str(self._main_character_stats[cs.MAX_DAMAGE])
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_accuracy_line(self):
        label = QLabel(
            CharacterMenuText.ACCURACY
            + str(self._main_character_stats[cs.ACCURACY] * 100)
            + "%"
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_critical_strike_chance_line(self):
        label = QLabel(
            CharacterMenuText.CRITICAL_STRIKE_CHANCE
            + str(self._main_character_stats[cs.CRITICAL_STRIKE_CHANCE] * 100)
            + "%"
        )
        label = self._upper_font(label)
        self._global_layout.addWidget(label)

    def _create_critical_strike_multiplier_line(self):
        layout = QHBoxLayout()

        label = QLabel(
            CharacterMenuText.CRITICAL_STRIKE_MULTIPLIER
            + str(self._main_character_stats[cs.CRITICAL_STRIKE_MULTIPLIER])
        )
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_lines(self) -> None:
        self._create_general_line()
        self._create_name_line()
        self._create_level_line()
        self._create_class_line()
        self._create_bars_line()
        self._create_health_line()
        self._create_stamina_line()
        self._create_attributes_line()
        self._create_strength_line()
        self._create_agility_line()
        self._create_vitality_line()
        self._create_endurance_line()
        self._create_attribute_points_line()
        self._create_stats_line()
        self._create_damage_line()
        self._create_accuracy_line()
        self._create_critical_strike_chance_line()
        self._create_critical_strike_multiplier_line()
