# The-Game.

## Warning: it's on develop

## Menus:

### Main Menu:

First, you should name your character, after you confirmed your character creation, there are two buttons in the bottom
right corner.

First button opens character menu

Second one opens option menu

### Character Menu

Here are all the stats of your character. You can distribute start attribute points as you wish.

You should confirm your distribution by accept button.

### Option Menu

Here, you can change game language, after choosing another language, you must restart the game, language changes will be
saved

## Dev's:

### Adding new Enemy

When you add new enemy in "enemies" you should add his names in texts, add him in enemy map (core/enemies/enemy_map.py) and add him in enemies
init (core/enemies/init.py).

### Adding new Weapon

When you add new weapon in "items" you should add it names in texts, add it in drop rate map with 0 drop rate (
core/enemies/drop_rates.py) and add it in weapons init (core/items/weapons/init.py).

### Adding new Scenario

Every scenario rules manages situations. Situation creates new buttons once. If you want to crate a new set of buttons,
you should create new situation. There is a battle situation, that can be used in your scenario, it takes main menu ref
and enemy ref

### About BaseSituation Using

BaseSituation have _texts map, which contains button labels

BaseSituation have button function named like "event__#_action" they are doing nothing, you should override them so
buttons use them.

BaseSituation have self._log() function, it takes string, which will be logged in game window

BaseSituation have self.refresh_buttons() func, you should use it, if you changed self._texts