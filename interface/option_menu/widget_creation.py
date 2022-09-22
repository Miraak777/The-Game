from PyQt6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from core.constants.language_constants import Language
from core.constants.widget_constants import WidgetSizes
from core.constants.button_size_constants import OptionMenuButtons


def create_title_widget(self) -> QLabel:
    title = QLabel(self._text.TITLE)
    title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    title.setFixedSize(WidgetSizes.OPTION_MENU_TITLE)
    title.setStyleSheet(self._title_stylesheet)
    return title


def create_language_choose_widget(self) -> QVBoxLayout:
    language_choose_layout = QVBoxLayout()
    label = QLabel(text=self._text.LANGUAGE_CHANGE_LABEL)
    label.setFixedSize(WidgetSizes.OPTION_MENU_LANGUAGE)
    label.setStyleSheet(self._language_choose_stylesheet)
    language_choose_layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
    return language_choose_layout


def create_languages_buttons(self) -> QHBoxLayout:
    layout = QHBoxLayout()
    russian_button = create_russian_language_button(self)
    layout.addWidget(russian_button, alignment=Qt.AlignmentFlag.AlignTop)
    english_button = create_english_language_button(self)
    layout.addWidget(english_button, alignment=Qt.AlignmentFlag.AlignTop)
    return layout


def create_russian_language_button(self) -> QPushButton:
    russian_language_button = QPushButton(text=Language.RUSSIAN)
    russian_language_button.setStyleSheet(self._languages_buttons_stylesheet)
    russian_language_button.setFixedSize(OptionMenuButtons.LANGUAGE_BUTTON)
    russian_language_button.setCheckable(True)
    russian_language_button.clicked.connect(self._event_set_ru_language)
    russian_language_button.setEnabled(True)
    if self._language == Language.RU:
        russian_language_button.setEnabled(False)
    return russian_language_button


def create_english_language_button(self) -> QPushButton:
    english_language_button = QPushButton(text=Language.ENGLISH)
    english_language_button.setStyleSheet(self._languages_buttons_stylesheet)
    english_language_button.setFixedSize(OptionMenuButtons.LANGUAGE_BUTTON)
    english_language_button.setCheckable(True)
    english_language_button.clicked.connect(self._event_set_en_language)
    english_language_button.setEnabled(True)
    if self._language == Language.EN:
        english_language_button.setEnabled(False)
    return english_language_button


def restart_request_label(self, text) -> QLabel:
    label = QLabel(text=text.RESTART_REQUEST)
    label.setStyleSheet(self._restart_request_stylesheet)
    return label
