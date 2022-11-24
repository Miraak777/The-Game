from typing import Dict
from PyQt6.QtCore import QDir
from yaml import safe_load
from pathlib import Path

from core.constants.key_bind_constants import KeyBindNames
from core import BACKGROUNDS, BUTTONS, WIDGET_TEXTURES, Paths


def get_key_binds() -> Dict:
    with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
        settings = safe_load(settings_file)
        return settings[KeyBindNames.KEY_BINDS]


def clear_layout(layout) -> None:
    item_list = list(range(layout.count()))
    item_list.reverse()
    for i in item_list:
        item = layout.itemAt(i)
        layout.removeItem(item)
        if item.widget():
            item.widget().deleteLater()


def set_qdirs() -> None:
    QDir.addSearchPath(BACKGROUNDS, Paths.PATH_TO_BACKGROUNDS)
    QDir.addSearchPath(BUTTONS, Paths.PATH_TO_BUTTON_TEXTURES)
    QDir.addSearchPath(WIDGET_TEXTURES, Paths.PATH_TO_WIDGET_TEXTURES)








def get_enemy_stats(enemy_file_name):
    with open(str(Path(Paths.PATH_TO_ENEMIES, enemy_file_name)), "r") as enemy_file:
        stats = safe_load(enemy_file)
        return stats
