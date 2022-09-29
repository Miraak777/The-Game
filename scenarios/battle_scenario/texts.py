from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Light Attack"
    SECOND_ACTION: str = "Medium Attack"
    THIRD_ACTION: str = "Heavy Attack"
    FOURTH_ACTION: str = "Retreat"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Лёгкая атака"
    SECOND_ACTION: str = "Средняя атака"
    THIRD_ACTION: str = "Тяжелая атака"
    FOURTH_ACTION: str = "Отступить"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}