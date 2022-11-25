from core import BACKGROUNDS, BUTTONS

character_menu_stylesheet = (
    "CharacterMenu {"
    f"background-image: url({BACKGROUNDS}:character_menu_background.png);"
    "}"
    "QLabel {"
    "font: 18px;"
    "}"
)

add_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:add_button_enabled.png);"
    "background-position: center;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:add_button_disabled.png);"
    "border: 1px solid black"
    "}"
    "QPushButton:hover {border: 1px solid #edbd79;}"
)

remove_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:remove_button_enabled.png);"
    "background-position: center;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:remove_button_disabled.png);"
    "border: 1px solid black"
    "}"
    "QPushButton:hover {border: 1px solid #edbd79;}"
)

accept_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:accept_button_enabled.png);"
    "color: #edbd79;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:accept_button_disabled.png);"
    "font: bold 18px;"
    "border: 1px solid black"
    "}"
    "QPushButton:hover {border: 1px solid #edbd79;}"
)

exit_menu_button_stylesheet = (
    "QPushButton {"
    f"background-image: url({BUTTONS}:exit_menu_button.png);"
    "border: 0px"
    "}"
    "QPushButton:hover {"
    f"background-image: url({BUTTONS}:selected_exit_menu_button.png);"
    "border: 1px solid black"
    "}"
    "QPushButton:hover {border: 1px solid #edbd79;}"
)
