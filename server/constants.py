from pathlib import Path
from dataclasses import dataclass

BASE_DIR = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Paths:
    PATH_TO_RESOURCES = str(Path(BASE_DIR, "resources"))
    PATH_TO_CONSUMABLES = Path(BASE_DIR, "resources", "consumables")
    PATH_TO_ENEMIES = Path(BASE_DIR, "resources", "enemies")
    PATH_TO_SCENARIOS = Path(BASE_DIR, "resources", "scenarios")
    PATH_TO_WEAPONS = Path(BASE_DIR, "resources", "weapons")
    PATH_TO_CONFIG = str(Path(BASE_DIR, "config.yml"))


@dataclass(frozen=True)
class ServerConstants:
    HOST: str = "host"
    PORT: str = "port"
    POST: str = "post"
    GET: str = "get"


@dataclass(frozen=True)
class ResourcesConstants:
    WEAPONS: str = "weapons"
    ENEMIES: str = "enemies"
    CONSUMABLES: str = "consumables"
    SCENARIOS: str = "scenarios"
