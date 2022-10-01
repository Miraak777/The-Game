from core import BUTTONS

game_window_stylesheet = (
    "GameWindow {"
    "background-color: rgba(100, 100, 100, 0.5);"
    "}"
    "QPushButton {"
    f"background-image: url({BUTTONS}:action_button.png);"
    "color: #dea659;"
    "font: 20px;"
    "}"
)

scroll_area_stylesheet = "background-color: rgba(0, 0, 0, 0.08);" "border: 0px;"

label_stylesheet = "QLabel {" "background-color: rgba(0, 0, 0, 0);" "font: 18px;" "}"
