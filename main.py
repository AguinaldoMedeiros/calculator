import sys

from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variables import WINDOWS_ICON_PATH


def main():
    print('teste')


if __name__ == "__main__":
    # Creating the application
    app = QApplication(sys.argv)
    window = MainWindow()

    # Define the icon
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('25.53 ^ 5')
    window.addToVLayout(info)
    info.configStyle()

    # Display
    display = Display()
    display.setPlaceholderText('Typing something')
    window.addToVLayout(display)

    # Run all
    window.adjustFixedSize()
    window.show()
    app.exec()
