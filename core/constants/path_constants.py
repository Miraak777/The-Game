from dataclasses import dataclass
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent)


@dataclass(frozen=True)
class Paths:
    PATH_TO_SETTINGS: str = str(Path(BASE_DIR, "core", "settings.yml"))
    PATH_TO_BACKGROUNDS: str = str(Path(BASE_DIR, "resources", "textures", "background_textures"))
    PATH_TO_BUTTON_TEXTURES: str = str(Path(BASE_DIR, "resources", "textures", "button_textures"))
    PATH_TO_WIDGET_TEXTURES: str = str(Path(BASE_DIR, "resources", "textures", "widget_textures"))


BACKGROUNDS = "backgrounds"
BUTTONS = "buttons"
WIDGET_TEXTURES = "widget_textures"
