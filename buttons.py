from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrNot, isEmpty, isValidNum
from display import Display
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info

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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self.info =  info
        self.display = display
        self._equation = ''
        self._left = None
        self._rigth = None
        self._op = None
        self._makeGrid()

    @property
    def equation(self):
        return self._equation
    
    @equation.setter
    def equation(self, text):
        self.equation = text
        self.info.settext(text)

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)
                self._configSpecialButtonClicked(button)

                if not isNumOrNot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(self._addButtonTextToDisplay, button_text)
                button.clicked.connect(slot)

    # def _connectButtonClicked(self, button, slot):
    #     button.clicked.connect(slot)

    def _configSpecialButtonClicked(self, button: Button):
        text = button.text()
        if text == 'C':
            # slot = self._makeSlot(self.display.clear)
            button.clicked.connect(self._clear)
        
        if text in '-+*/':
            button.clicked.connect(self._makeSlot(self._displayInfoConifig, text))

        if text == '=':
            button.clicked.connect(self._calculate)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _addButtonTextToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNum(newDisplayValue):
            return

        self.display.insert(text)

    def _clear(self):
        self.info.setText('')
        self._left = None
        self._op = None
        self._rigth = None
        self.display.clear()

    def _displayInfoConifig(self, text):
        displayText = self.display.text()
        if displayText == '':
            return
        self._left = displayText
        self._op = text
        infoText = self._left + " " + self._op + " ??"
        self.info.setText(infoText)
        self.display.clear()

    def _calculate(self):
        displayText = self.display.text()
        if displayText == '':
            return
        self._rigth = displayText
        account = self._left + self._op + self._rigth +'='
        self.display.setText(eval(account))
        self.info.setText('')