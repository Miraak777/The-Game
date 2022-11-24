from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QHBoxLayout, QLabel, QPushButton, QVBoxLayout

from core.constants.language_constants import Language

from .constants import OptionMenuButtons, OptionMenuSizes
from .stylesheets import (
    debug_button_stylesheet,
    about_button_stylesheet,
    exit_button_stylesheet,
    language_choose_stylesheet,
    languages_buttons_stylesheet,
    restart_request_stylesheet,
    title_stylesheet,
    exit_menu_button_stylesheet,
)


def create_title_widget(self) -> QLabel:
    title = QLabel(self._text.TITLE)
    title.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
    title.setFixedSize(OptionMenuSizes.OPTION_MENU_TITLE)
    title.setStyleSheet(title_stylesheet)
    return title


def create_language_choose_title(self) -> QVBoxLayout:
    language_choose_layout = QVBoxLayout()
    label = QLabel(text=self._text.LANGUAGE_CHANGE_LABEL)
    label.setFixedSize(OptionMenuSizes.OPTION_MENU_LANGUAGE)
    label.setStyleSheet(language_choose_stylesheet)
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
    russian_language_button.setStyleSheet(languages_buttons_stylesheet)
    russian_language_button.setFixedSize(OptionMenuButtons.LANGUAGE_BUTTON)
    russian_language_button.setCheckable(True)
    russian_language_button.clicked.connect(self._event_set_ru_language)
    russian_language_button.setEnabled(True)
    if self._language == Language.RU:
        russian_language_button.setEnabled(False)
    return russian_language_button


def create_english_language_button(self) -> QPushButton:
    english_language_button = QPushButton(text=Language.ENGLISH)
    english_language_button.setStyleSheet(languages_buttons_stylesheet)
    english_language_button.setFixedSize(OptionMenuButtons.LANGUAGE_BUTTON)
    english_language_button.setCheckable(True)
    english_language_button.clicked.connect(self._event_set_en_language)
    english_language_button.setEnabled(True)
    if self._language == Language.EN:
        english_language_button.setEnabled(False)
    return english_language_button


def restart_request_label(self) -> QLabel:
    label = QLabel(text=self._text.RESTART_REQUEST)
    label.setStyleSheet(restart_request_stylesheet)
    return label


def exit_button(self) -> QPushButton:
    button = QPushButton(text=self._text.EXIT_BUTTON)
    button.setStyleSheet(exit_button_stylesheet)
    button.setFixedSize(OptionMenuButtons.EXIT_BUTTON)
    button.setCheckable(True)
    button.clicked.connect(self._event_exit)
    return button


def debug_mode_button(self) -> QPushButton:
    button = QPushButton(text=self._text.DEBUG_BUTTON)
    button.setStyleSheet(debug_button_stylesheet)
    button.setFixedSize(OptionMenuButtons.DEBUG_BUTTON)
    button.setCheckable(True)
    button.clicked.connect(self._event_debug_mode)
    return button


def about_menu_button(self) -> QPushButton:
    button = QPushButton(text=self._text.ABOUT_BUTTON)
    button.setStyleSheet(about_button_stylesheet)
    button.setFixedSize(OptionMenuButtons.ABOUT_BUTTON)
    button.setCheckable(True)
    button.clicked.connect(self.event_open_about_menu)
    return button


def create_exit_menu_button(self) -> QPushButton:
    button = QPushButton()
    button.setFixedSize(OptionMenuButtons.EXIT_MENU_BUTTON)
    button.setStyleSheet(exit_menu_button_stylesheet)
    button.clicked.connect(self._event_exit_menu)
    return button
