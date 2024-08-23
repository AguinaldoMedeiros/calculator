import math
from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrNot, isEmpty, isValidNum
from display import Display
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


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
    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['', '0', '.', '='],
        ]

        self._info = info
        self._display = display
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None
        self._window = window
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, text):
        self._equation = text
        self._info.setText(text)

    def _makeGrid(self):
        for row_number, row_data in enumerate(self._gridMask):
            for column_number, button_text in enumerate(row_data):
                button = Button(button_text)
                self._configSpecialButtonClicked(button)

                if not isNumOrNot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')

                self.addWidget(button, row_number, column_number)
                slot = self._makeSlot(
                    self._addButtonTextToDisplay, button_text)
                button.clicked.connect(slot)

    # def _connectButtonClicked(self, button, slot):
    #     button.clicked.connect(slot)

    def _configSpecialButtonClicked(self, button: Button):
        text = button.text()
        if text == 'C':
            # slot = self._makeSlot(self.display.clear)
            button.clicked.connect(self._clear)

        if text in '-+*/^':
            button.clicked.connect(self._makeSlot(
                self._displayInfoConfig, text))

        if text == '=':
            button.clicked.connect(self._calculate)

        if text == '◀':
            button.clicked.connect(self._backSpace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _addButtonTextToDisplay(self, text):
        newDisplayValue = self._display.text() + text

        if not isValidNum(newDisplayValue):
            return

        self._display.insert(text)

    def _clear(self):
        self._info.setText('')
        self._left = None
        self._op = None
        self._right = None
        # self.equation = ''
        self._display.clear()

    def _displayInfoConfig(self, text):
        displayText = self._display.text()
        if displayText == '':
            return
        self._left = float(displayText)
        self._op = text
        self.equation = f'{self._left} {self._op} ??'
        self._display.clear()

    def _calculate(self):
        displayText = self._display.text()
        if displayText == '':
            return
        if self._left is None:
            return
        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'

        try:
            if '^' in self.equation and isinstance(self._left, float):
                try:
                    result = math.pow(self._left, self._right)
                    self._display.setText(str(result))
                except:
                    self._clear()
                    self._showERROR('Burst')
                    return
            else:
                result = eval(self.equation)
                self._display.setText(str(result))

        except ZeroDivisionError:
            self._showERROR("Can't divide by zero", 'Zero division ERROR')
            self._clear()
            return

        self._info.setText(f'{self.equation} =')

    def _backSpace(self):
        self._display.backspace()

    def _showERROR(self, text, title_error='ERROR'):
        msgBox = self._window.makeMsgBox()
        msgBox.setWindowTitle(title_error)
        msgBox.setText(text)
        # msgBox.setInformativeText('BLA BLA BLA BLA BLA')
        # msgBox.setIcon(msgBox.Icon.Critical)

        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok  # |
            # msgBox.StandardButton.Cancel |
            # msgBox.StandardButton.NoAll
        )
        # msgBox.button(msgBox.StandardButton.Cancel).setText('Cancelar')

        msgBox.exec()
        # result = msgBox.exec()

        # if result == msgBox.StandardButton.Ok:
        #     print('Ok')
        # if result == msgBox.StandardButton.Cancel:
        #     print('Cancel')
        # if result == msgBox.StandardButton.NoAll:
        #     print('NoAll')
