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
        self.tableView = QWidget()
        self.leftVBox.addWidget(self.RadioButtons)
        self.leftVBox.addWidget(self.tableView)
        
        self.donatorLayout = DonatorInput()
        self.testBox = QHBoxLayout()
        self.testBox.addLayout(self.leftVBox)
        self.testBox.addWidget(self.donatorLayout)
        self.setLayout(self.testBox)
        
