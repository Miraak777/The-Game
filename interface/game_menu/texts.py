from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    awd = "awd"


@dataclass(frozen=True)
class RussianText:
    awd = "awd"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
