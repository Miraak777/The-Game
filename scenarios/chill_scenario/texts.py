from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Next Battle"
    SECOND_ACTION: str = ""
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""
    CHILL: str = "You're chilling"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Следующий бой"
    SECOND_ACTION: str = ""
    THIRD_ACTION: str = ""
    FOURTH_ACTION: str = ""
    CHILL: str = "Вы отдыхаете"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}