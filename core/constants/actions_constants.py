from dataclasses import dataclass


@dataclass(frozen=True)
class ActionButtons:
    FIRST_ACTION: str = "first_action"
    SECOND_ACTION: str = "second_action"
    THIRD_ACTION: str = "third_action"
    FOURTH_ACTION: str = "fourth_action"
