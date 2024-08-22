from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrNot, isEmpty, isValidNum
from display import Display


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)

                if not isNumOrNot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, row_number, column_number)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._addButtonTextToDisplay, button_text
                )
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _addButtonTextToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNum(newDisplayValue):
            return

        self.display.insert(text)
