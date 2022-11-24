from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    INTRODUCTION: str = "You awake"
    FIRST_ACTION: str = "Travel to North"
    SECOND_ACTION: str = "Travel to East"
    THIRD_ACTION: str = "Travel to South"
    FOURTH_ACTION: str = "Travel to West"


@dataclass(frozen=True)
class RussianText:
    INTRODUCTION: str = (
        "Вы просыпаетесь посреди леса. Вас окружают деревья, и вы не знаете куда пойти. "
        "Вы умеете ориентироваться на местности, так что легко находите стороны света, в "
        "какую сторону света вы хотите пойти?"
    )
    FIRST_ACTION: str = "Пойти на Север"
    SECOND_ACTION: str = "Пойти на Восток"
    THIRD_ACTION: str = "Пойти на Юг"
    FOURTH_ACTION: str = "Пойти на Запад"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
