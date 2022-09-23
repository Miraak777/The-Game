def health_formula(health_mult: float, level: int, vitality: int) -> float:
    return health_mult * ((level * 10) + (vitality * 10))


def stamina_formula(stamina_mult: float, level: int, endurance: int) -> float:
    return stamina_mult * ((level * 5) + (endurance * 5))


def min_damage_formula(min_damage: int,
                       agility: int,
                       agility_damage_multiplier: float,
                       strength: int,
                       strength_damage_multiplier: float) -> float:
    return min_damage * (
            (agility_damage_multiplier * (1 + agility * 0.1))
            + (strength_damage_multiplier * (1 + strength * 0.1))
    )


def max_damage_formula(max_damage: int,
                       agility: int,
                       agility_damage_multiplier: float,
                       strength: int,
                       strength_damage_multiplier: float) -> float:
    return max_damage * (
            (agility_damage_multiplier * (1 + agility * 0.1))
            + (strength_damage_multiplier * (1 + strength * 0.1))
    )


def critical_strike_formula(base_critical_strike_chance: float,
                            agility: int,
                            critical_strike_chance_multiplier: float) -> float:
    critical_strike_chance = base_critical_strike_chance * (1 + critical_strike_chance_multiplier * agility * 0.05)
    if critical_strike_chance <= 0:
        critical_strike_chance = 0
    if critical_strike_chance >= 1:
        critical_strike_chance = 1
    critical_strike_chance = round(critical_strike_chance, 2)
    return critical_strike_chance


def accuracy_formula(accuracy: float, agility: int, level: int) -> float:
    accuracy = accuracy * ((1 + agility * 0.3) / (0.9 + level*0.1))
    if accuracy <= 0:
        accuracy = 0
    if accuracy >= 1:
        accuracy = 1
    return round(accuracy, 2)
