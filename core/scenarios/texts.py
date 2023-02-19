from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    LIGHT_ATTACK: str = "Light Attack"
    MEDIUM_ATTACK: str = "Medium Attack"
    HEAVY_ATTACK: str = "Heavy Attack"
    ESCAPE: str = "Retreat"
    DAMAGE: str = "Damage"
    STAMINA_CONSUMPTION: str = "Stamina consumption"
    BATTLE_START: str = "You've been attacked by"
    LEVEL: str = "Lvl"
    YOU_FOUNDED: str = "You founded"


@dataclass(frozen=True)
class RussianText:
    LIGHT_ATTACK: str = "Лёгкая атака"
    MEDIUM_ATTACK: str = "Обычная атака"
    HEAVY_ATTACK: str = "Тяжелая атака"
    ESCAPE: str = "Отступить"
    DAMAGE: str = "Урон"
    STAMINA_CONSUMPTION: str = "Затраты запаса сил"
    BATTLE_START: str = "На вас напал"
    LEVEL: str = "Ур"
    YOU_FOUNDED: str = "Вы нашли"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}