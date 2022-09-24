from dataclasses import dataclass


@dataclass(frozen=True)
class KeyBindNames:
    KEY_BINDS = "key_binds"
    CHARACTER_MENU = "character_menu"
    OPTION_MENU = "option_menu"
    FIRST_ACTION = "first_action"
    SECOND_ACTION = "second_action"
    THIRD_ACTION = "third_action"
    FOURTH_ACTION = "fourth_action"
