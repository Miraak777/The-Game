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
    "}"
)

remove_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:remove_button_enabled.png);"
    "background-position: center;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:remove_button_disabled.png);"
    "}"
)

accept_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:accept_button_enabled.png);"
    "color: #edbd79;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:accept_button_disabled.png);"
    "font: bold 18px;"
    "}"
)

exit_menu_button_stylesheet = (
    "QPushButton {"
    f"background-image: url({BUTTONS}:exit_menu_button.png);"
    "border: 0px"
    "}"
    "QPushButton:hover {"
    f"background-image: url({BUTTONS}:selected_exit_menu_button.png);"
    "}"
)
