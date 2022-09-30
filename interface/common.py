from typing import Dict

from yaml import safe_load

from core import Paths
from core.constants.key_bind_constants import KeyBindNames


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
