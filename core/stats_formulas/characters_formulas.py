def health_formula(health_mult, level, vitality):
    return health_mult * ((level * 5) + (vitality * 10))


def stamina_formula(stamina_mult, level, endurance):
    return stamina_mult * ((level * 2.5) + (endurance * 5))


def min_damage_formula(min_damage, agility, agility_damage_multiplier, strength, strength_damage_multiplier):
    return min_damage * (
            (agility_damage_multiplier * (1 + agility * 0.1)) +
            (strength_damage_multiplier * (1 + strength * 0.1))
    )


def max_damage_formula(max_damage, agility, agility_damage_multiplier, strength, strength_damage_multiplier):
    return max_damage * (
            (agility_damage_multiplier * (1 + agility * 0.1)) +
            (strength_damage_multiplier * (1 + strength * 0.1))
    )


def critical_strike_formula(base_critical_strike_chance, agility, critical_strike_chance_multiplier):
    return base_critical_strike_chance * (1 + critical_strike_chance_multiplier * agility * 0.05)


def accuracy_formula(accuracy, agility, level):
    return accuracy * (1 + (agility * 5 - level))
