from core import WIDGET_TEXTURES, BACKGROUNDS, BUTTONS

character_create_button_stylesheet = (f"background-image: url({WIDGET_TEXTURES}:character_creation_line_edit.jpg);"
                                      "font: bold 20px;"
                                      "border: 1px solid black")

main_window_stylesheet = ("MainWindow {"
                          f"background-image: url({BACKGROUNDS}:main_menu_background.jpg);"
                          "}"
                          "QPushButton:hover {border: 5px;"
                          "border-radius: 10px;}"
                          "QWidget {"
                          "font-family: Comic Sans MS, Comic Sans, cursive"
                          "}")

character_creation_button_stylesheet = ("QPushButton:enabled {"
                                        f"background-image: url({BUTTONS}:"
                                        "character_creation_button_enabled.png);"
                                        "color: #edbd79;"
                                        "border: 0px"
                                        "}"
                                        "QPushButton {"
                                        f"background-image: url({BUTTONS}:"
                                        "character_creation_button_disabled.png);"
                                        "font: bold 18px;"
                                        "color: #000000;"
                                        "border: 0px;"
                                        "}")

character_menu_button_stylesheet = ("QPushButton:enabled {"
                                    f"image: url({BUTTONS}:character_menu_button_enabled.png);"
                                    "border: 0px;"
                                    "}"
                                    "QPushButton {"
                                    f"image: url({BUTTONS}:character_menu_button_disabled.png);"
                                    "border: 0px;"
                                    "}")
option_menu_button_stylesheet = ("QPushButton:enabled {"
                                 f"image: url({BUTTONS}:option_menu_button_enabled.png);"
                                 "border: 0px;"
                                 "}"
                                 "QPushButton {"
                                 f"image: url({BUTTONS}:option_menu_button_disabled.png);"
                                 "border: 0px;"
                                 "}")
