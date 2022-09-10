from dataclasses import dataclass
from core.constants.language_constants import Language
import PyQt6.QtCore
from PyQt6.QtCore import QSize


@dataclass
class WindowSizes:
    MAIN_WINDOW_SIZE: PyQt6.QtCore.QSize = QSize(1200, 700)
    CHARACTER_MENU_SIZE: PyQt6.QtCore.QSize = QSize(400, 500)
    OPTION_MENU_SIZE: PyQt6.QtCore.QSize = QSize(1000, 600)
#     TODO сделать настройку через конфиг



@dataclass
class WindowsFonts:
    FONT_SIZE: int = 15
#     TODO сделать настройку через конфиг


@dataclass
class WidgetSizes:
    CHARACTER_CREATE_NAME_LINE_EDIT: PyQt6.QtCore.QSize = QSize(150, 30)
#     TODO сделать настройку через конфиг


@dataclass(frozen=True)
class WidgetNames:
    CHARACTER_CREATE_NAME_LINE_EDIT: str = "character_create_name_line_edit"
    CHARACTER_CREATE_BUTTON: str = "character_create_button"


@dataclass
class AttributeLinesLengthEn:
    STRENGTH_LINE_SIZE: PyQt6.QtCore.QSize = QSize(123, 20)
    AGILITY_LINE_SIZE: PyQt6.QtCore.QSize = QSize(103, 20)
    VITALITY_LINE_SIZE: PyQt6.QtCore.QSize = QSize(107, 20)
    ENDURANCE_LINE_SIZE: PyQt6.QtCore.QSize = QSize(139, 20)


@dataclass
class AttributeLinesLengthRu:
    STRENGTH_LINE_SIZE: PyQt6.QtCore.QSize = QSize(93, 20)
    AGILITY_LINE_SIZE: PyQt6.QtCore.QSize = QSize(133, 20)
    VITALITY_LINE_SIZE: PyQt6.QtCore.QSize = QSize(147, 20)
    ENDURANCE_LINE_SIZE: PyQt6.QtCore.QSize = QSize(177, 20)


attribute_lines = {
    Language.EN: AttributeLinesLengthEn,
    Language.RU: AttributeLinesLengthRu
}
