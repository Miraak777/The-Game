from dataclasses import dataclass
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent)


@dataclass(frozen=True)
class Paths:
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
            BASE_DIR, "textures", "background_textures", "option_menu_background.png"
        )
    )
    CHARACTER_MENU_ICON: str = str(Path(BASE_DIR, "icons", "character_menu_icon.png"))
    OPTION_MENU_ICON: str = str(Path(BASE_DIR, "icons", "option_menu_icon.png"))
