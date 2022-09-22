from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QDir
from core import BACKGROUNDS, ICONS, BUTTONS, WIDGET_TEXTURES, Paths

from interface import MainWindow

QDir.addSearchPath(BACKGROUNDS, Paths.PATH_TO_BACKGROUNDS)
QDir.addSearchPath(ICONS, Paths.PATH_TO_ICONS)
QDir.addSearchPath(BUTTONS, Paths.PATH_TO_BUTTON_TEXTURES)
QDir.addSearchPath(WIDGET_TEXTURES, Paths.PATH_TO_WIDGET_TEXTURES)
app = QApplication([])

main_window = MainWindow()
main_window.show()

app.exec()
