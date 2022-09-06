from dataclasses import dataclass


@dataclass(frozen=True)
class Language:
    EN = "en"
    RU = "ru"


LANGUAGE = "language"
