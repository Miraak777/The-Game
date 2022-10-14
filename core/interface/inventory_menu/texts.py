from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    INVENTORY_IS_FULL = "Inventory is full!"


@dataclass(frozen=True)
class RussianText:
    INVENTORY_IS_FULL = "Инвентарь полон!"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
