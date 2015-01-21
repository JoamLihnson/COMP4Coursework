from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Charity Shop Database Management")

        self.MakeUI()

    def MakeUI(self):
        self.okButton = QPushButton("OK")
        self.cancelButton = QPushButton("Cancel")
        self.textBox = QLineEdit()
        self.vBox = QVBoxLayout()
        self.grid = QGridLayout()
        self.grid.addWidget(self.textBox, 0,0)
        self.vBox.addWidget(self.okButton)
        self.vBox.addWidget(self.cancelButton)
        self.grid.addLayout(self.vBox, 0,1)
        self.useButton = QPushButton("Useless")
        self.usesButton = QPushButton("Usessssless")

        self.grid.addWidget(self.useButton, 1, 1)
        self.grid.addWidget(self.usesButton, 1, 0)

        self.centrelWidget = QWidget()
        self.centrelWidget.setLayout(self.grid)

        self.setCentralWidget(self.centrelWidget)


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
