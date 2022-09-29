from dataclasses import dataclass


@dataclass(frozen=True)
class KeyBindNames:
    KEY_BINDS: str = "key_binds"
    CHARACTER_MENU: str = "character_menu"
    OPTION_MENU: str = "option_menu"
    FIRST_ACTION: str = "first_action"
    SECOND_ACTION: str = "second_action"
    THIRD_ACTION: str = "third_action"
    FOURTH_ACTION: str = "fourth_action"
