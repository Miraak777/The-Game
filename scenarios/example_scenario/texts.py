from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = ""
    SECOND_ACTION: str = ""
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = ""
    SECOND_ACTION: str = ""
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}