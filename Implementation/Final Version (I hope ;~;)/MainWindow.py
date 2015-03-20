#1.     Imports the required modules
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3
from DonationDialog import *

#2.     Initilization of the mindow class
class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Charity Shop Database Management")

        self.setFixedSize(565,600)

        self.MakeUI()

    def MakeUI(self):
#3.     Defines the "Actions" that are performed when perfoming an act such as pressing a button
        self.Insert = QAction("Insert", self)
        self.Update = QAction("Update", self)
        self.Delete = QAction("Delete", self)
        self.View = QAction("View", self)
        self.Sale = QAction("Sale", self)
        self.Donation = QAction("Donation", self)
        self.Exit = QAction("Exit", self)
#4.     Creates the menu bar
        self.menuBar = QMenuBar()   
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.Exit)
        self.databaseMenu = self.menuBar.addMenu("Database")
        self.databaseMenu.addAction(self.Insert)
        self.databaseMenu.addAction(self.Update)
        self.databaseMenu.addAction(self.Delete)
        self.databaseMenu.addAction(self.View)
        self.donationMenu = self.menuBar.addMenu("Bussiness")
        self.donationMenu.addAction(self.Sale)
        self.donationMenu.addAction(self.Donation)
        self.setMenuBar(self.menuBar)
#5.     Creates the contents of the top-left "Database" box
        self.databaseLabel = QLabel("Database")
        self.insertButton = QPushButton("Insert")
        self.updateButton = QPushButton("Update")
        self.deleteButton = QPushButton("Delete")
        self.viewButton = QPushButton("View")
        self.leftVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.databaseLabel)
        self.leftVBox.addWidget(self.insertButton)
        self.leftVBox.addWidget(self.updateButton)
        self.leftVBox.addWidget(self.deleteButton)
        self.leftVBox.addWidget(self.viewButton)
#6.     Creates the contents of the top-right "Bussiness" box
        self.bussinessLabel = QLabel("Bussiness")
        self.saleButton = QPushButton("Sale")
        self.saleButton.setFixedHeight(55)
        self.donationButton = QPushButton("Donation")
        self.donationButton.setFixedHeight(55)
        self.rightVBox = QVBoxLayout()
        self.rightVBox.addWidget(self.bussinessLabel)
        self.rightVBox.addWidget(self.saleButton)
        self.rightVBox.addWidget(self.donationButton)
#7.     Creates the divider seen between the two top boxes
        self.vertDivide = QFrame()
        self.vertDivide.setFrameStyle(QFrame.VLine)
#8.     Creates the contents of the middle "Search" box
        self.middleHBox = QHBoxLayout()
        self.searchBar = QLineEdit()
        self.searchButton = QPushButton("Search")
        self.middleHBox.addWidget(self.searchBar)
        self.middleHBox.addWidget(self.searchButton)
#9.     This is all code for the tables. I don't know shit about tables ¯\_(ツ)_/¯
        self.tableWidget = QTableWidget()
#10.    Creates the status bar the appears at the very bottom of the window
        self.statusBar = QStatusBar()
        self.statusBar.setSizeGripEnabled(0)
#11.    Combines the two top VBoxes into one HBox
        self.topHBox = QHBoxLayout()
        self.topHBox.addLayout(self.leftVBox)
        self.topHBox.addWidget(self.vertDivide)
        self.topHBox.addLayout(self.rightVBox)
#12.    Creates a final VBox to place everything else in and set as the central widget
        self.bigVBox = QVBoxLayout()
        self.bigVBox.addLayout(self.topHBox)
        self.bigVBox.addLayout(self.middleHBox)
        self.bigVBox.addWidget(self.tableWidget)
        self.bigVBox.addWidget(self.statusBar)
        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.bigVBox)
        self.setCentralWidget(self.centralWidget)

#13.    Sets the function connections that get accessed by the button and menu options

        self.donationButton.clicked.connect(self.DonationDialog)

    def DonationDialog(self):
        statusNote = QLabel("Donation Button Clicked!")
        self.statusBar.addWidget(statusNote)
        self.dialog = DonationDialogClass()
        self.dialog.exec_()
        self.statusBar.removeWidget



if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
