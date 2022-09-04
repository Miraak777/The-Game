from interface import MainWindow
from PyQt6.QtWidgets import QApplication
from core.constants.path_constants import Paths

app = QApplication([])

main_window = MainWindow()
main_window.show()

app.exec()
