from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Create Character!"
    CHARACTER_NAME_PLACEHOLDER: str = "Enter your character name"


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "The Game"
    CHARACTER_CREATE_BUTTON: str = "Создайте персонажа!"
    CHARACTER_NAME_PLACEHOLDER: str = "Введите имя вашего персонажа"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
