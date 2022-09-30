from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    LEVEL_UP: str = "Level up!"
    GAINED_EXPERIENCE: str = "Gained Experience: "
    BECOME_PEASANT: str = "You're now Peasant!"
    BECOME_WARRIOR: str = "You're now Warrior"
    BECOME_ASSASSIN: str = "You're now Assassin"
    NOT_ENOUGH_STAMINA: str = "You do not have enough stamina for this attack"
    CRITICAL_STRIKE: str = "Critical Strike!"
    MISS: str = "Miss!"
    DEATH: str = "You died, your adventure ends here"
    REST: str = "You rested"
    CANNOT_REST: str = "You feel full of energy and don't want ro rest"


@dataclass(frozen=True)
class RussianText:
    LEVEL_UP: str = "Повышение уровня!"
    GAINED_EXPERIENCE: str = "Получено опыта: "
    BECOME_PEASANT: str = "Теперь вы Крестьянин"
    BECOME_WARRIOR: str = "Теперь вы Воин"
    BECOME_ASSASSIN: str = "Теперь ты Убийца"
    NOT_ENOUGH_STAMINA: str = "Вам не хватает запаса сил на эту атаку"
    CRITICAL_STRIKE: str = "Критический Удар!"
    MISS: str = "Промах!"
    DEATH: str = "Вы погибли, ваше приключение заканчивается здесь"
    REST: str = "Вы отдохнули"
    CANNOT_REST: str = "Вы чувствуете, что полны сил, и не хотите отдыхать"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
