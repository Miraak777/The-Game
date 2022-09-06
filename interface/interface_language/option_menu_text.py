from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "Options"


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "Настройки"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
