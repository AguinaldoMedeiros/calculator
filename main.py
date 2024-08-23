import sys

from buttons import ButtonsGrid
from main_window import MainWindow
from display import Display
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from styles import setupTheme
from variables import WINDOWS_ICON_PATH

if __name__ == "__main__":
    # Creating the application
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Define the icon
    icon = QIcon(str(WINDOWS_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('')
    window.addWidgetToVLayout(info)
    info.configStyle()

    # Display
    display = Display()
    display.setPlaceholderText('Typing something')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Run all
    window.adjustFixedSize()
    window.show()
    app.exec()
