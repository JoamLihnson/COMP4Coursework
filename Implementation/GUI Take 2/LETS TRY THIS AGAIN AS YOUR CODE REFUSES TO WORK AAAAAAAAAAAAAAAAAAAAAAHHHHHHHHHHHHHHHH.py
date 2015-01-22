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
        self.Insert = QAction("Insert", self)
        self.Delete = QAction("Delete", self)
        self.Update = QAction("Update", self)
        self.Donate = QAction("Donate", self)
        self.Search = QAction("Search", self)
        


        self.menuBar = QMenuBar()
        self.fileMenu = self.menuBar.addMenu("File")
        self.databaseMenu = self.menuBar.addMenu("Database")
        self.databaseMenu.addAction(self.Insert)
        self.databaseMenu.addAction(self.Update)
        self.databaseMenu.addAction(self.Delete)
        self.donationMenu = self.menuBar.addMenu("Dontation")
        self.donationMenu.addAction(self.Donate)
        self.donationMenu.addAction(self.Search)
        
        self.setMenuBar(self.menuBar)

        self.insertButton = QPushButton("Insert")
        self.updateButton = QPushButton("Update")
        self.deleteButton = QPushButton("Delete")
        self.leftVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.insertButton)
        self.leftVBox.addWidget(self.updateButton)
        self.leftVBox.addWidget(self.deleteButton)

        self.donateButton = QPushButton("Donate")
        self.searchBar = QLineEdit()
        self.searchGo = QPushButton("Search")
        self.searchBox  = QHBoxLayout()
        self.searchBox.addWidget(self.searchBar)
        self.searchBox.addWidget(self.searchGo)
        self.rightVBox = QVBoxLayout()
        self.rightVBox.addWidget(self.donateButton)
        self.rightVBox.addLayout(self.searchBox)

        self.statusBar = QStatusBar()
        self.statusBar.setSizeGripEnabled(0)


        self.upperHBox = QHBoxLayout()
        self.upperHBox.addLayout(self.leftVBox)
        self.upperHBox.addLayout(self.rightVBox)

        self.totalVBox = QVBoxLayout()
        self.totalVBox.addLayout(self.upperHBox)
        self.totalVBox.addWidget(self.statusBar)

        self.centrelWidget = QWidget()
        self.centrelWidget.setLayout(self.totalVBox)

        self.setCentralWidget(self.centrelWidget)

    def InsertDialog(self):
        


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
