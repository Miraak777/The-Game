from dataclasses import dataclass
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)


@dataclass(frozen=True)
class Paths:
    PATH_TO_SETTINGS: str = str(
        Path(BASE_DIR, "settings.yml")
    )
    MAIN_MENU_BACKGROUND: str = str(
        Path(BASE_DIR, "textures", "background_textures", "main_menu_background.jpg")
    )
    CHARACTER_MENU_BACKGROUND: str = str(
        Path(
            BASE_DIR, "textures", "background_textures", "character_menu_background.png"
        )
    )
    OPTION_MENU_BACKGROUND: str = str(
        Path(
            BASE_DIR, "textures", "background_textures", "option_menu_background.jpg"
        )
    )
    CHARACTER_MENU_ICON: str = str(Path(BASE_DIR, "icons", "character_menu_icon.png"))
    OPTION_MENU_ICON: str = str(Path(BASE_DIR, "icons", "option_menu_icon.png"))
    ADDING_ICON: str = str(Path(BASE_DIR, "textures", "button_textures", "add_button.png"))
    REMOVING_ICON: str = str(Path(BASE_DIR, "textures", "button_textures", "remove_button.png"))
    BUTTON_150x40: str = str(Path(BASE_DIR, "textures", "button_textures", "150x40_button.png"))
