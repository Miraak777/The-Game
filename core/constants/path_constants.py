from dataclasses import dataclass
from pathlib import Path
from core.constants.item_constants import ItemTypes

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)


@dataclass(frozen=True)
class Paths:
    PATH_TO_MAIN_MENU_ICON: str = str(Path(BASE_DIR, "resources", "textures", "widget_textures", "main_menu_icon.png"))
    PATH_TO_SETTINGS: str = str(Path(BASE_DIR, "core", "settings.yml"))
    PATH_TO_BACKGROUNDS: str = str(Path(BASE_DIR, "resources", "textures", "background_textures"))
    PATH_TO_BUTTON_TEXTURES: str = str(Path(BASE_DIR, "resources", "textures", "button_textures"))
    PATH_TO_WIDGET_TEXTURES: str = str(Path(BASE_DIR, "resources", "textures", "widget_textures"))
    PATH_TO_WEAPON_ICONS: str = str(Path(BASE_DIR, "resources", "items", "weapons"))
    PATH_TO_CONSUMABLES_ICONS: str = str(Path(BASE_DIR, "resources", "items", "consumables"))


path_to_item_icons_map = {
    ItemTypes.WEAPON: Paths.PATH_TO_WEAPON_ICONS,
    ItemTypes.CONSUMABLE: Paths.PATH_TO_CONSUMABLES_ICONS,
}

BACKGROUNDS = "backgrounds"
BUTTONS = "buttons"
WIDGET_TEXTURES = "widget_textures"
WEAPON_ICONS = "weapon_icons"
