from dataclasses import dataclass


@dataclass(frozen=True)
class KeyBindNames:
    KEY_BINDS = "key_binds"
    CHARACTER_MENU = "character_menu"
    OPTION_MENU = "option_menu"
