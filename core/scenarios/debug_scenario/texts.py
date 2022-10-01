from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Get 1000 Xp"
    SECOND_ACTION: str = "Become Peasant"
    THIRD_ACTION: str = "Become Warrior"
    FOURTH_ACTION: str = "Become Assassin"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Получить 1000 опыта"
    SECOND_ACTION: str = "Стать Крестьянином"
    THIRD_ACTION: str = "Стать Воином"
    FOURTH_ACTION: str = "Стать Убийцей"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
