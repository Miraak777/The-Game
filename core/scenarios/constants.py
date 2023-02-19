from dataclasses import dataclass


@dataclass
class ScenarioStats:
    REQUIRED_LEVEL: str = "required_level"
    START: str = "start"
    TEXTS: str = "texts"
    ACTIONS: str = "actions"
    ACTION_1: str = "action_1"
    ACTION_2: str = "action_2"
    ACTION_3: str = "action_3"
    ACTION_4: str = "action_4"
    ACTION_NAMES: str = "action_names"
    NEXT_EVENT: str = "next_event"
    ACTION_TYPE: str = "action_type"
    DIALOG: str = "dialog"
    LEAVE: str = "leave"
    BATTLE: str = "battle"
    REWARD: str = "reward"
    ENEMY_INFO: str = "enemy_info"
    NAMES: str = "names"
    ENEMY_TYPE: str = "enemy_type"
    LEVEL: str = "level"
    CHARACTER_LEVEL: str = "character_level"
    ADDED_LEVEL: str = "added_level"
    WEAPON: str = "weapon"
    RANDOM: str = "random"
