from typing import Dict

from PyQt6.QtCore import QDir
from yaml import safe_load

from core import BACKGROUNDS, BUTTONS, WIDGET_TEXTURES, Paths
from core.constants.key_bind_constants import KeyBindNames
from core.constants.server_constants import ServerConstants as sc
from core.main_character.character import MainCharacter


def get_key_binds() -> Dict:
    with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
        settings = safe_load(settings_file)
        return settings[KeyBindNames.KEY_BINDS]


def get_server_url() -> str:
    with open(Paths.PATH_TO_SETTINGS, "r") as settings_file:
        settings = safe_load(settings_file)
        url = settings[sc.SERVER][sc.HOST] + ":" + settings[sc.SERVER][sc.PORT]
        return url


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


def calculate_difficulty(main_menu, enemy) -> float:
    difficulty = 1
    main_character: MainCharacter = main_menu.main_character
    health_modifier = (main_character.health / (main_character.max_health * 2)) - 0.5
    average_character_damage = (main_character.max_damage + main_character.min_damage) / 2
    average_enemy_damage = (enemy.max_damage + enemy.min_damage) / 2
    if average_enemy_damage > average_character_damage:
        damage_modifier = (average_character_damage/(average_enemy_damage * 2)) * -1
    else:
        damage_modifier = average_character_damage/(average_enemy_damage * 3)
    return round(difficulty + health_modifier + damage_modifier, 2)
