from dataclasses import dataclass


@dataclass(frozen=True)
class ServerConstants:
    SERVER: str = "server"
    HOST: str = "host"
    PORT: str = "port"


@dataclass(frozen=True)
class ResourcesConstants:
    WEAPONS: str = "weapons"
    ENEMIES: str = "enemies"
    CONSUMABLES: str = "consumables"
    SCENARIOS: str = "scenarios"


class ServerEndpoints:
    RESOURCES_LIST: str = "/resources_list"
