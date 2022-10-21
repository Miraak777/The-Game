from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Continue"
    SECOND_ACTION: str = "Get all weapons"
    THIRD_ACTION: str = "Become Warrior"
    FOURTH_ACTION: str = "Become Assassin"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Продолжить"
    SECOND_ACTION: str = "Получить все оружия"
    THIRD_ACTION: str = "Стать Воином"
    FOURTH_ACTION: str = "Стать Убийцей"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
