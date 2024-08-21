from pathlib import Path
from PySide6.QtGui import QIcon

ROOT_DIR = Path(__file__).parent
FILE_DIR = ROOT_DIR / 'images'
WINDOWS_ICON_PATH = FILE_DIR / 'calculator.png'

# Sizing
BIG_FONT_SIZE = 40
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 18
TEXT_MARGIN = 15
MINIMUM_WIGTH = 500