from . import (
    ArmedTroll,
    Goblin,
    GoblinWithDagger,
    Human,
    HumanWithDagger,
    HumanWithSword,
    HumanWithTwoHandedSword,
    Troll,
)

enemies_level_maps = [
    [1, [Goblin, GoblinWithDagger]],
    [3, [GoblinWithDagger, Human, HumanWithDagger, ]],
    [5, [GoblinWithDagger, Human, HumanWithDagger, HumanWithSword]],
    [10, [HumanWithDagger, HumanWithSword, HumanWithTwoHandedSword, Troll]],
    [20, [HumanWithSword, HumanWithTwoHandedSword, Troll, ArmedTroll]],
]
