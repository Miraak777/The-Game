from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    APPLE: str = "Apple"
    STEAK: str = "Steak"
    RATION: str = "Ration"


@dataclass(frozen=True)
class RussianText:
    APPLE: str = "Яблоко"
    STEAK: str = "Стейк"
    RATION: str = "Паек"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}