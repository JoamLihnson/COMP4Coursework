from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Charity Shop Database Management")
        
