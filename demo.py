from PyQt6.QtWidgets import QApplication

from interface import MainWindow

app = QApplication([])

main_window = MainWindow()
main_window.show()

app.exec()
