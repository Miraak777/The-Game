from PyQt6.QtWidgets import QApplication

from core.interface import MainMenu

app = QApplication([])

main_window = MainMenu()
main_window.show()

app.exec()
