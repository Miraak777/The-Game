from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    LEVEL_UP: str = "Level up!"
    GAINED_EXPERIENCE: str = "Gained Experience: "
    CHANGE_CLASS: str = "You're now "
    NOT_ENOUGH_STAMINA: str = "You do not have enough stamina for this attack"
    CRITICAL_STRIKE: str = "Critical Strike!"
    MISS: str = "Miss!"
    DEATH: str = "You died, your adventure ends here"
    REST: str = "You rested"
    CANNOT_REST: str = "You feel full of energy and don't want ro rest"
    EQUIPPED_WEAPON: str = "You equipped "


@dataclass(frozen=True)
class RussianText:
    LEVEL_UP: str = "Повышение уровня!"
    GAINED_EXPERIENCE: str = "Получено опыта: "
    CHANGE_CLASS: str = "Теперь вы "
    NOT_ENOUGH_STAMINA: str = "Вам не хватает запаса сил на эту атаку"
    CRITICAL_STRIKE: str = "Критический Удар!"
    MISS: str = "Промах!"
    DEATH: str = "Вы погибли, ваше приключение заканчивается здесь"
    REST: str = "Вы отдохнули"
    CANNOT_REST: str = "Вы чувствуете, что полны сил, и не хотите отдыхать"
    EQUIPPED_WEAPON: str = "Вы экипировали "


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
