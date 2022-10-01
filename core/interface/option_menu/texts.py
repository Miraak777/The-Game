from dataclasses import dataclass

from core.constants.language_constants import Language


@dataclass(frozen=True)
class EnglishText:
    TITLE: str = "Options"
    LANGUAGE_CHANGE_LABEL: str = "Choose language"
    RESTART_REQUEST: str = "Please, restart the game, for changes to take effect"
    EXIT_BUTTON: str = "Ok"
    DEBUG_BUTTON: str = "Debug Mode"


@dataclass(frozen=True)
class RussianText:
    TITLE: str = "Настройки"
    LANGUAGE_CHANGE_LABEL: str = "Выберите язык"
    RESTART_REQUEST: str = "Пожалуйста, перезапустите игру, чтобы изменения вступили в силу"
    EXIT_BUTTON: str = "Ок"
    DEBUG_BUTTON: str = "Режим Дебага"


Text = {
    Language.EN: EnglishText,
    Language.RU: RussianText,
}
