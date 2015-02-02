#imports the much needed PyQt modules
from PyQt4.QtGui import *
from PyQt4.QtCore import *

#imports all my own modules that I've made
from InsertDialog import *

#imports some other stuff :v
import sys
import sqlite3

#here we gooooo!!!!!
class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Charity Shop Database Management")

        self.MakeUI()

    def MakeUI(self):

        #creates the menu bar choices
        self.Insert = QAction("Insert", self)
        self.Delete = QAction("Delete", self)
        self.Update = QAction("Update", self)
        self.Donate = QAction("Donate", self)
        self.Search = QAction("Search", self)
        

        #creates the menu bar...
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
        
        #creates the left side of the menu. The 'Database' side
        self.databaseLabel = QLabel("Database")
        self.insertButton = QPushButton("Insert")
        self.updateButton = QPushButton("Update")
        self.deleteButton = QPushButton("Delete")
        self.leftVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.databaseLabel)
        self.leftVBox.addWidget(self.insertButton)
        self.leftVBox.addWidget(self.updateButton)
        self.leftVBox.addWidget(self.deleteButton)
        
        #muh d-divider!!!
        self.vertDivide = QFrame()
        self.vertDivide.setFrameStyle(QFrame.VLine)
        


        self.donationLabel = QLabel("Donation")
        self.donateButton = QPushButton("Donate")
        self.searchBar = QLineEdit()
        self.searchGo = QPushButton("Search")
        self.searchBox  = QHBoxLayout()
        self.searchBox.addWidget(self.searchBar)
        self.searchBox.addWidget(self.searchGo)
        self.rightVBox = QVBoxLayout()
        self.rightVBox.addWidget(self.donationLabel)
        self.rightVBox.addWidget(self.donateButton)
        self.rightVBox.addLayout(self.searchBox)

        self.statusBar = QStatusBar()
        self.statusBar.setSizeGripEnabled(0)


        self.upperHBox = QHBoxLayout()
        self.upperHBox.addLayout(self.leftVBox)
        self.upperHBox.addWidget(self.vertDivide)
        self.upperHBox.addLayout(self.rightVBox)

        self.totalVBox = QVBoxLayout()
        self.totalVBox.addLayout(self.upperHBox)
        self.totalVBox.addWidget(self.statusBar)

        self.centrelWidget = QWidget()
        self.centrelWidget.setLayout(self.totalVBox)

        self.setCentralWidget(self.centrelWidget)

        self.insertButton.clicked.connect(self.InsertDialog)
        self.updateButton.clicked.connect(self.UpdateDialog)
        self.deleteButton.clicked.connect(self.DeleteDialog)

    def InsertDialog(self):
        statusNote = QLabel("Choose data to insert")
        self.statusBar.addWidget(statusNote)
        self.dialog = InsertDialogClass()
        self.dialog.exec_()
        self.statusBar.removeWidget(statusNote)

    def UpdateDialog(self):
        pass

    def DeleteDialog(self):
        pass

    def DonateDialog(self):
        pass

    def SearchFunc(self):
        pass


if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
