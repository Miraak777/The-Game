from PyQt6.QtWidgets import QLabel

from core.constants.windows_constants import WindowsFonts


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
    return layout
