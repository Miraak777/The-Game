from core import BUTTONS

game_window_stylesheet = (
    "GameMenu {"
    "background-color: rgba(0, 0, 0, 0.08);"
    "}"
    "QPushButton:enabled {"
    f"background-image: url({BUTTONS}:action_button_enabled.png);"
    "color: #dea659;"
    "font: 20px;"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:action_button_disabled.png);"
    "}"
)

scroll_area_stylesheet = "background-color: rgba(0, 0, 0, 0.08);" "border: 0px;"

label_stylesheet = "QLabel {" "background-color: rgba(0, 0, 0, 0);" "font: 18px;" "}"
