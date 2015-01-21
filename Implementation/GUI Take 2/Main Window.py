from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Charity Shop Database Management")
        okButton = QPushButton("Cancel")
        cancelButton = QPushButton("OK")
        self.hbox = QVBoxLayout()
        self.hbox.addStretch(1)
        self.hbox.addWidget(okButton)
        self.hbox.addWidget(cancelButton)
        self.setLayout(self.hbox)


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
