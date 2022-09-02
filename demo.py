from main_character.character import MainCharacter

Character = MainCharacter()
# Character.set_class_assassin()
# Character.set_class_warrior()
Character.add_strength()
Character.add_agility()
Character.add_vitality()
# Character.add_endurance()
Character.set_max_health()
Character.set_max_stamina()
print(
    Character.get_main_stats(), "\n",
    Character.get_bars(), "\n",
    Character.get_attributes(), "\n",
    Character.get_combat_stats(), "\n",
)
