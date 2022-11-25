from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TRASH: str = "Trash"
    COMMON: str = "Common"
    UNCOMMON: str = "Uncommon"
    RARE: str = "Rare"
    UNIQUE: str = "Unique"
    LEGENDARY: str = "Legendary"
    RELIC: str = "Relic"
    DIVINE: str = "Divine"
    DAMAGE: str = "Damage"
    STAMINA_CONSUMPTION: str = "Stamina consumption"
    LEVEL: str = "Lvl"
    RESTORES: str = "Restores"
    HEALTH: str = "health"


@dataclass(frozen=True)
class RussianText:
    TRASH: str = "Мусор"
    COMMON: str = "Обычное"
    UNCOMMON: str = "Необычное"
    RARE: str = "Редкое"
    UNIQUE: str = "Уникальное"
    LEGENDARY: str = "Легендарное"
    RELIC: str = "Реликвия"
    DIVINE: str = "Божественное"
    DAMAGE: str = "Урон"
    STAMINA_CONSUMPTION: str = "Затраты запаса сил"
    LEVEL: str = "Ур."
    RESTORES: str = "Восстанавливает"
    HEALTH: str = "здоровья"


Text = {Language.EN: EnglishText, Language.RU: RussianText}
