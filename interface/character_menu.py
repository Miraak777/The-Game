from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon, QImage, QPalette, QBrush
from PyQt6.QtCore import Qt
from core.constants.windows_constants import WindowTitles
from core.constants.path_constants import Paths
from core.constants.character_constants import (
    BarsNames as bn,
    AttributesNames as an,
    CombatStats as cs,
    MainStatsNames as msn,
    Classes,
)
from interface.windows_parameters import WindowSizes, WindowsFonts


class CharacterMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(Paths.CHARACTER_MENU_ICON))
        self.setWindowTitle(WindowTitles.CHARACTER_MENU)
        self.setFixedSize(WindowSizes.CHARACTER_MENU_SIZE)

        self._create_background()

        self._global_layout = QVBoxLayout()

        self._create_lines()

        self._widget = QWidget()
        self._global_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self._widget.setLayout(self._global_layout)
        self.setCentralWidget(self._widget)

    def _create_background(self):
        background_image = QImage(Paths.CHARACTER_MENU_BACKGROUND)
        background_image.scaled(WindowSizes.CHARACTER_MENU_SIZE)
        palette = QPalette()
        palette.setBrush(QPalette.ColorRole.Window, QBrush(background_image))
        self.setPalette(palette)

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

    def _create_name_line(self):
        layout = QHBoxLayout()

        label = QLabel(msn.NAME + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_level_line(self):
        layout = QHBoxLayout()

        label = QLabel(msn.LEVEL + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_class_line(self):
        layout = QHBoxLayout()

        label = QLabel(msn.CLASS + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_bars_line(self):
        layout = QHBoxLayout()

        label = QLabel(bn.BARS + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_health_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + bn.HEALTH + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_stamina_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + bn.STAMINA + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_attributes_line(self):
        layout = QHBoxLayout()

        label = QLabel(an.ATTRIBUTES + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_strength_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + an.STRENGTH + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_agility_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + an.AGILITY + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_vitality_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + an.VITALITY + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_endurance_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + an.ENDURANCE + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_stats_line(self):
        layout = QHBoxLayout()

        label = QLabel(cs.STATS + ":")
        label = self._upper_font(label)
        label = self._bold_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_damage_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + cs.DAMAGE + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_accuracy_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + cs.ACCURACY + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_critical_strike_chance_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + cs.CRITICAL_STRIKE_CHANCE + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_critical_strike_multiplier_line(self):
        layout = QHBoxLayout()

        label = QLabel(" " + cs.CRITICAL_STRIKE_MULTIPLIER + ":")
        label = self._upper_font(label)
        layout.addWidget(label)

        self._global_layout.addLayout(layout)

    def _create_lines(self) -> None:
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
        self._create_stats_line()
        self._create_damage_line()
        self._create_accuracy_line()
        self._create_critical_strike_chance_line()
        self._create_critical_strike_multiplier_line()
