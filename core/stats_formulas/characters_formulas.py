def health_formula(health_mult: float, level: int, vitality: int) -> float:
    stamina = health_mult * ((level * 10) + (vitality * 10))
    return round(stamina, 2)


def stamina_formula(stamina_mult: float, level: int, endurance: int) -> float:
    health = stamina_mult * ((level * 5) + (endurance * 5))
    return round(health, 2)


def min_damage_formula(min_damage: int,
                       agility: int,
                       agility_damage_multiplier: float,
                       strength: int,
                       strength_damage_multiplier: float) -> float:
    min_damage = min_damage * (1 +
            (agility_damage_multiplier * (agility * 0.1))
            + (strength_damage_multiplier * (strength * 0.1))
    )
    return round(min_damage, 2)


def max_damage_formula(max_damage: int,
                       agility: int,
                       agility_damage_multiplier: float,
                       strength: int,
                       strength_damage_multiplier: float) -> float:
    max_damage = max_damage * (1 +
            (agility_damage_multiplier * (agility * 0.1))
            + (strength_damage_multiplier * (strength * 0.1))
    )
    return round(max_damage, 2)


def critical_strike_formula(base_critical_strike_chance: float,
                            agility: int,
                            critical_strike_chance_multiplier: float) -> float:
    critical_strike_chance = base_critical_strike_chance * (1 + critical_strike_chance_multiplier * agility * 0.05)
    if critical_strike_chance <= 0:
        critical_strike_chance = 0
    if critical_strike_chance >= 1:
        critical_strike_chance = 1
    return round(critical_strike_chance, 3)


def accuracy_formula(accuracy: float, agility: int, level: int) -> float:
    accuracy = accuracy * ((1 + agility * 0.3) / (0.9 + level*0.1))
    if accuracy <= 0:
        accuracy = 0
    if accuracy >= 1:
        accuracy = 1
    return round(accuracy, 3)
