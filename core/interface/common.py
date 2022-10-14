from typing import Dict
from PyQt6.QtCore import QDir
from yaml import safe_load

from core.constants.key_bind_constants import KeyBindNames
from core import BACKGROUNDS, BUTTONS, WIDGET_TEXTURES, Paths


def get_key_binds() -> Dict:
    with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
        settings = safe_load(settings_file)
        return settings[KeyBindNames.KEY_BINDS]


def clear_layout(layout):
    item_list = list(range(layout.count()))
    item_list.reverse()
    for i in item_list:
        item = layout.itemAt(i)
        layout.removeItem(item)
        if item.widget():
            item.widget().deleteLater()


def set_qdirs():
    QDir.addSearchPath(BACKGROUNDS, Paths.PATH_TO_BACKGROUNDS)
    QDir.addSearchPath(BUTTONS, Paths.PATH_TO_BUTTON_TEXTURES)
    QDir.addSearchPath(WIDGET_TEXTURES, Paths.PATH_TO_WIDGET_TEXTURES)
