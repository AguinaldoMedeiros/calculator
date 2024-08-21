from PySide6.QtWidgets import (QMainWindow, QLabel, QWidget, QVBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)

        self.setCentralWidget(self.cw)

        # Window Title
        self.setWindowTitle('Calculator')
        

    def adjustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        
    def addWidgetToVLayout(self, text, size):
        label = QLabel(text)
        label.setStyleSheet(f'font-size: {size}px;')
        
        
        self.vLayout.addWidget(label)