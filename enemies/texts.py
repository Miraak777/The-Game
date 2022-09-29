from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    GOBLIN: str = "Goblin"
    TROLL: str = "Troll"
    ARMED_TROLL: str = "Armed Troll"
    TAKEN: str = "took"
    DEAL: str = "dealt"
    DAMAGE: str = "damage"
    DIED: str = "died"


@dataclass(frozen=True)
class RussianText:
    GOBLIN: str = "Гоблин"
    TROLL: str = "Тролль"
    ARMED_TROLL: str = "Вооруженный Тролль"
    TAKEN: str = "получил"
    DEAL: str = "нанёс"
    DAMAGE: str = "единиц урона"
    DIED: str = "умер"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}