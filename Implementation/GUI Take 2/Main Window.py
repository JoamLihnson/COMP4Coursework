from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Charity Shop Database Management")

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.button1 = QPushButton("Button 1", self)
        self.button2 = QPushButton("Button You", self)
        self.grid.addWidget(self.button1, 0,0,0,0)
        self.grid.addWidget(self.button2, 1,1,1,1)

        self.menuBar = QMenuBar()
        self.fileMenu = self.menuBar.addMenu("File")















if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
