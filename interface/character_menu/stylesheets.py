from core import BACKGROUNDS, BUTTONS

character_menu_stylesheet = ("CharacterMenu {"
                             f"background-image: url({BACKGROUNDS}:character_menu_background.png);"
                             "}"
                             "QLabel {"
                             "font: 18px;"
                             "}")

add_button_stylesheet = ("QPushButton:enabled {"
                         f"background-image: url({BUTTONS}:add_button_enabled.png);"
                         "border: 0px;"
                         "background-position: center;"
                         "}"
                         "QPushButton {"
                         f"background-image: url({BUTTONS}:add_button_disabled.png);"
                         "border: 0px;"
                         "}")

remove_button_stylesheet = ("QPushButton:enabled {"
                            f"background-image: url({BUTTONS}:remove_button_enabled.png);"
                            "border: 0px;"
                            "background-position: center;"
                            "}"
                            "QPushButton {"
                            f"background-image: url({BUTTONS}:remove_button_disabled.png);"
                            "border: 0px;"
                            "}")

accept_button_stylesheet = ("QPushButton:enabled {"
                            f"background-image: url({BUTTONS}:accept_button_enabled.png);"
                            "color: #edbd79;"
                            "border: 0px;"
                            "}"
                            "QPushButton {"
                            f"background-image: url({BUTTONS}:accept_button_disabled.png);"
                            "font: bold 18px;"
                            "border: 0px;"
                            "}")
