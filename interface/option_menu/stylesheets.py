from core import WIDGET_TEXTURES, BUTTONS, BACKGROUNDS

title_stylesheet = ("QLabel {"
                    f"background-image: url({WIDGET_TEXTURES}:option_menu_title.png);"
                    "background-repeat: no-repeat;"
                    "background-position:vertical-center;"
                    "font: bold 20px;"
                    "color:#edbd79;"
                    "padding: 1px;}")

language_choose_stylesheet = ("QLabel {"
                              f"background-image: url({WIDGET_TEXTURES}:option_menu_title.png);"
                              "font: bold 18px;"
                              "background-repeat: no-repeat;"
                              "color:#edbd79;"
                              "padding: 1px;}")

languages_buttons_stylesheet = ("QPushButton:enabled {"
                                f"background-image: url({BUTTONS}:language_button_enabled.png);"
                                "color:#edbd79;"
                                "border: 0px;"
                                "}"
                                "QPushButton {"
                                f"background-image: url({BUTTONS}:language_button_disabled.png);"
                                "color: black;"
                                "font: 18px;"
                                "border: 0px;"
                                "}")

restart_request_stylesheet = ("QLabel {"
                              "font: bold 18px;"
                              "color: #edbd79;}")

option_menu_stylesheet = ("OptionMenu {"
                          f"background-image: url({BACKGROUNDS}:option_menu_background.jpg);"
                          "}")
