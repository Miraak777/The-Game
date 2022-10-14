from PyQt6.QtCore import QDir
from PyQt6.QtWidgets import QApplication

from core import BACKGROUNDS, BUTTONS, WEAPON_ICONS, WIDGET_TEXTURES, Paths
from core.interface import MainMenu

QDir.addSearchPath(BACKGROUNDS, Paths.PATH_TO_BACKGROUNDS)
QDir.addSearchPath(BUTTONS, Paths.PATH_TO_BUTTON_TEXTURES)
QDir.addSearchPath(WIDGET_TEXTURES, Paths.PATH_TO_WIDGET_TEXTURES)
QDir.addSearchPath(WEAPON_ICONS, Paths.PATH_TO_WEAPON_ICONS)
app = QApplication([])

main_window = MainMenu()
main_window.show()

app.exec()
