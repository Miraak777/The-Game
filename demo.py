from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QDir
from core import BACKGROUNDS, BUTTONS, WIDGET_TEXTURES, Paths

from interface import MainMenu

QDir.addSearchPath(BACKGROUNDS, Paths.PATH_TO_BACKGROUNDS)
QDir.addSearchPath(BUTTONS, Paths.PATH_TO_BUTTON_TEXTURES)
QDir.addSearchPath(WIDGET_TEXTURES, Paths.PATH_TO_WIDGET_TEXTURES)
app = QApplication([])

main_window = MainMenu()
main_window.show()

app.exec()
