from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    GET_1000_XP = "Get 1000 Xp"
    BECOME_PEASANT = "Become Peasant"
    BECOME_WARRIOR = "Become Warrior"
    BECOME_ASSASSIN = "Become Assassin"


@dataclass(frozen=True)
class RussianText:
    GET_1000_XP = "Получить 1000 опыта"
    BECOME_PEASANT = "Стать Крестьянином"
    BECOME_WARRIOR = "Стать Воином"
    BECOME_ASSASSIN = "Стать Убийцей"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}