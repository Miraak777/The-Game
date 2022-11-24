from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TAKEN: str = "took"
    DEAL: str = "dealt"
    DAMAGE: str = "damage"
    DIED: str = "died"
    RECEIVED: str = " received "
    RECEIVED_DAMAGE: str = " damage"


@dataclass(frozen=True)
class RussianText:
    TAKEN: str = "получил"
    DEAL: str = "нанёс"
    DAMAGE: str = "единиц урона"
    DIED: str = "умер"
    RECEIVED: str = " получил "
    RECEIVED_DAMAGE: str = " урона"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
