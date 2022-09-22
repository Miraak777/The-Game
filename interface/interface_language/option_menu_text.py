from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "Options"
    LANGUAGE_CHANGE_LABEL: str = "Choose language"


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "Настройки"
    LANGUAGE_CHANGE_LABEL: str = "Выберите язык"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
