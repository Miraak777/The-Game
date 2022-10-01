from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Continue traveling"
    SECOND_ACTION: str = "Rest"
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""
    CHILL: str = "You made a halt"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Продолжить путешествие"
    SECOND_ACTION: str = "Отдохнуть"
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""
    CHILL: str = "Вы устроили привал"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
