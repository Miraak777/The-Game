from core import BACKGROUNDS, BUTTONS, WIDGET_TEXTURES

character_create_button_stylesheet = (
    f"background-image: url({WIDGET_TEXTURES}:character_creation_line_edit.jpg);"
    "font: bold 20px;"
    "border: 1px solid black"
)

main_menu_stylesheet = (
    "MainMenu {"
    f"background-image: url({BACKGROUNDS}:main_menu_background.jpg);"
    "}"
    "QPushButton:hover {border: 1px solid #edbd79;"
    "}"
    "QPushButton {"
    "border: 1px solid black;"
    "}"
    "QWidget {"
    "font-family: Comic Sans MS, Comic Sans, cursive"
    "}"
)

character_creation_button_stylesheet = (
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:"
    "character_creation_button_enabled.png);"
    "color: #edbd79;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:"
    "character_creation_button_disabled.png);"
    "font: bold 18px;"
    "color: #000000;"
    "}"
)

character_menu_button_stylesheet = (
    "QPushButton:enabled {"
    f"image: url({BUTTONS}:character_menu_button_enabled.png);"
    "}"
    "QPushButton {"
    f"image: url({BUTTONS}:character_menu_button_disabled.png);"
    "}"
)
option_menu_button_stylesheet = (
    "QPushButton:enabled {"
    f"image: url({BUTTONS}:option_menu_button_enabled.png);"
    "}"
    "QPushButton {"
    f"image: url({BUTTONS}:option_menu_button_disabled.png);"
    "}"
)

about_menu_stylesheet = (
    "QFrame {" f"background-image: url({BACKGROUNDS}:main_menu_background);" "border: 2px solid;" "}"
)
about_menu_label_stylesheet = (
    "QLabel {" "background-image: url(no_back_ground);" "border: 0px solid;" "font: 20px;" "color: #edbd79;" "}"
)

exit_about_menu_button_stylesheet = (
    "QPushButton {" "border: 2px solid;" "border-radius: 2px;" "background-color: rgb(150, 0, 0)" "}"
)
