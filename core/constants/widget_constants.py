from dataclasses import dataclass


@dataclass
class WindowsFonts:
    FONT_SIZE: int = 15


@dataclass(frozen=True)
class WidgetNames:
    CHARACTER_CREATE_NAME_LINE_EDIT: str = "character_create_name_line_edit"
    CHARACTER_CREATE_BUTTON: str = "character_create_button"

