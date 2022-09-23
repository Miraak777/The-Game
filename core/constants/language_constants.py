from dataclasses import dataclass


@dataclass(frozen=True)
class Language:
    EN = "en"
    RU = "ru"
    ENGLISH = "English"
    RUSSIAN = "Русский"


LANGUAGE = "language"
