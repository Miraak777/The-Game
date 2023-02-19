from dataclasses import dataclass

from core.common import get_key_binds
from core.constants.key_bind_constants import KeyBindNames
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Create Character!"
    CHARACTER_NAME_PLACEHOLDER: str = "Enter your character name"
    CHARACTER_MENU_BUTTON_TOOLTIP: str = f"Character Menu ({get_key_binds()[KeyBindNames.CHARACTER_MENU]})"
    OPTION_MENU_BUTTON_TOOLTIP: str = f"Option Menu ({get_key_binds()[KeyBindNames.OPTION_MENU]})"
    ABOUT_MENU_TEXT: str = (
        "Author Name:\n"
        "Forite (Sergy Belev)\n"
        "University Information:\n"
        "PO-7 3-course\n"
        "Short Project Description:\n"
        "This is a Roguelike Text RPG."
    )
    FILE_VERIFY_FAILED: str = "Your files different from server files. Check them for loses."


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Создайте персонажа!"
    CHARACTER_NAME_PLACEHOLDER: str = "Введите имя вашего персонажа"
    CHARACTER_MENU_BUTTON_TOOLTIP: str = f"Меню персонажа ({get_key_binds()[KeyBindNames.CHARACTER_MENU]})"
    OPTION_MENU_BUTTON_TOOLTIP: str = f"Настройки ({get_key_binds()[KeyBindNames.OPTION_MENU]})"
    ABOUT_MENU_TEXT: str = (
        "Имя Автора:\n"
        "Форайт (Сергей Белев)\n"
        "Информация об Университете:\n"
        "ПО-7 3-курс\n"
        "Короткое описание проекта:\n"
        "Это Роглайк Текстовое РПГ."
    )
    FILE_VERIFY_FAILED: str = "Ваши файлы отличаются от серерных. Проверьте их на наличие потерь."


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
