from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    APPLE: str = "Apple"
    STEAK: str = "Steak"
    PIE: str = "Pie"


@dataclass(frozen=True)
class RussianText:
    APPLE: str = "Яблоко"
    STEAK: str = "Стейк"
    PIE: str = "Пирог"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}