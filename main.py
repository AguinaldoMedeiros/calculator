import sys

from PySide6.QtGui import QIcon
from main_window import MainWindow
from PySide6.QtWidgets import (QApplication, QLabel)

from variables import WINDOWS_ICON_PATH

def main():
    print('teste')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    
    window.adjustFixedSize()
    
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()