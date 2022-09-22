from PyQt6.QtWidgets import QLabel, QPushButton
from PyQt6.QtCore import QSize
from core.constants.widget_constants import WindowsFonts


def upper_font(label: QLabel) -> QLabel:
    font = label.font()
    font.setPointSize(WindowsFonts.FONT_SIZE)
    label.setFont(font)
    return label


def bold_font(label: QLabel) -> QLabel:
    font = label.font()
    font.setBold(True)
    label.setFont(font)
    return label


def clear_layout(layout):
    item_list = list(range(layout.count()))
    item_list.reverse()
    for i in item_list:
        item = layout.itemAt(i)
        layout.removeItem(item)
        if item.widget():
            item.widget().deleteLater()


def set_button_and_icon_sizes(button: QPushButton, size: QSize) -> QPushButton:
    button.setIconSize(size)
    button.setFixedSize(size)
    return button