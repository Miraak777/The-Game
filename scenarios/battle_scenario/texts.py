from dataclasses import dataclass
from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    FIRST_ACTION: str = "Light Attack"
    SECOND_ACTION: str = "Medium Attack"
    THIRD_ACTION: str = "Heavy Attack"
    FOURTH_ACTION: str = "Retreat"
    DAMAGE: str = "Damage: "
    STAMINA_CONSUMPTION: str = "Stamina consumption: "
    BATTLE_START: str = "You've been attacked by"
    HEALTH: str = "Health: "
    LEVEL: str = "Lvl"


@dataclass(frozen=True)
class RussianText:
    FIRST_ACTION: str = "Лёгкая атака"
    SECOND_ACTION: str = "Средняя атака"
    THIRD_ACTION: str = "Тяжелая атака"
    FOURTH_ACTION: str = "Отступить"
    DAMAGE: str = "Урон: "
    STAMINA_CONSUMPTION: str = "Затраты запаса сил: "
    BATTLE_START: str = "На вас напал"
    HEALTH: str = "Здоровье: "
    LEVEL: str = "Ур."


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}