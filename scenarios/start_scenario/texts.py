from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    dw = ""


@dataclass(frozen=True)
class RussianText:
    adw = ""


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
