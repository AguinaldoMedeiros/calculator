from PySide6.QtWidgets import QLineEdit
from variables import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUM_WIGTH
from PySide6.QtCore import Qt


class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        # self.setMinimumHeight(2*BIG_FONT_SIZE)
        # self.setMinimumWidth(MINIMUM_WIGTH)
        self.setMinimumSize(MINIMUM_WIGTH, 2*BIG_FONT_SIZE)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        # self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])
        self.setTextMargins(TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN, TEXT_MARGIN)
