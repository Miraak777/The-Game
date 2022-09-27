from dataclasses import dataclass
from core.constants.language_constants import Language
from interface.common import get_key_binds
from core.constants.key_bind_constants import KeyBindNames


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Create Character!"
    CHARACTER_NAME_PLACEHOLDER: str = "Enter your character name"
    CHARACTER_MENU_BUTTON_TOOLTIP: str = f"Character Menu ({get_key_binds()[KeyBindNames.CHARACTER_MENU]})"
    OPTION_MENU_BUTTON_TOOLTIP: str = f"Option Menu ({get_key_binds()[KeyBindNames.OPTION_MENU]})"
    LEVEL_UP: str = "Level up!"
    GAINED_EXPERIENCE: str = "Gained Experience: "
    BECOME_PEASANT: str = "You're now Peasant!"
    BECOME_WARRIOR: str = "You're now Warrior"
    BECOME_ASSASSIN: str = "You're now Assassin"


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Создайте персонажа!"
    CHARACTER_NAME_PLACEHOLDER: str = "Введите имя вашего персонажа"
    CHARACTER_MENU_BUTTON_TOOLTIP: str = f"Меню персонажа ({get_key_binds()[KeyBindNames.CHARACTER_MENU]})"
    OPTION_MENU_BUTTON_TOOLTIP: str = f"Настройка ({get_key_binds()[KeyBindNames.OPTION_MENU]})"
    LEVEL_UP: str = "Повышение уровня!"
    GAINED_EXPERIENCE: str = "Получено опыта: "
    BECOME_PEASANT: str = "Теперь вы Крестьянин"
    BECOME_WARRIOR: str = "Теперь вы Воин"
    BECOME_ASSASSIN: str = "Теперь ты Убийца"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
