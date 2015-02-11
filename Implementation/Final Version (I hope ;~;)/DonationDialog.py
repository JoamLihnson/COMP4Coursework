from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3
import time
from InputSelect import DonatorInput

class DonationDialogClass(QDialog):
    """A dialog when an item is donated"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Donation Information")

        self.ConstructLayouts()



    def ConstructLayouts(self):
        self.leftVBox = QVBoxLayout()

        self.radioBox = QGroupBox("Select an option")
        self.radioGroup = QButtonGroup()
        self.radioButtons = [QRadioButton("New Donator"),QRadioButton("Existing Donator")]
        self.radioButtons[0].setChecked(True)
        self.currentLayout = 0
        self.radioLayout = QVBoxLayout()
        count = 1
        for button in self.radioButtons:
            self.radioLayout.addWidget(button)
            self.radioGroup.addButton(button)
            self.radioGroup.setId(button, count)
            count += 1
        self.radioBox.setLayout(self.radioLayout)
        self.selectLayout = QHBoxLayout()
        self.selectLayout.addWidget(self.radioBox)


        
        self.RadioButtons = QWidget()
        self.RadioButtons.setLayout(self.selectLayout)


        
        self.tableView = QTableWidget()
        self.tableView.setColumnCount(3)
        self.tableView.setRowCount(4)

        
        self.leftVBox.addWidget(self.RadioButtons)
        self.leftVBox.addWidget(self.tableView)
        
        self.donatorLayout = DonatorInput()
        self.existingDonator = QVBoxLayout()
        self.existSearch = QPushButton("Search")
        self.IDLabel = QLabel("Donator ID :")
        self.IDEdit = QLineEdit()
        self.IDEnter = QHBoxLayout()
        self.IDEnter.addWidget(self.IDLabel)
        self.IDEnter.addWidget(self.IDEdit)


        self.existingDonator.addWidget(self.existSearch)
        self.existingDonator.addLayout(self.IDEnter)

        self.existingWidget = QWidget()
        self.existingWidget.setLayout(self.existingDonator)

        self.radioStack = QStackedLayout()
        self.radioStack.addWidget(self.donatorLayout)
        self.radioStack.addWidget(self.existingWidget)

        
        self.testBox = QHBoxLayout()
        self.testBox.addLayout(self.leftVBox)
        self.testBox.addLayout(self.radioStack)
        self.setLayout(self.testBox)

        self.radioButtons[0].toggled.connect(self.RadioSwitchLayout)


    def RadioSwitchLayout(self):
        if self.currentLayout == 0:
            self.currentLayout += 1
            self.radioStack.setCurrentIndex(self.currentLayout)
        else:
            self.currentLayout -= 1
            self.radioStack.setCurrentIndex(self.currentLayout)
        
        
        
