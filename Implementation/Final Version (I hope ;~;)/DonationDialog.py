from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3
import time
from InputSelect import DonatorInput
from InputSelect import ItemInput
from VariousLayouts import ButtonBox

class DonationDialogClass(QDialog):
    """A dialog when an item is donated"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Donation Information")
        self.setFixedSize(700,500)
        
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

        self.addItem = QPushButton("Add Item")

        self.tableView = QTableWidget()
        self.tableView.setColumnCount(2)
        self.tableView.setRowCount(4)
        self.header = QTableWidgetItem("")
        self.tableView.setHorizontalHeaderItem(1,self.header)
        self.buttonBox = ButtonBox()        
        self.leftVBox.addWidget(self.RadioButtons)
        self.leftVBox.addWidget(self.addItem)
        self.leftVBox.addWidget(self.tableView)
        self.leftVBox.addWidget(self.buttonBox)
        self.leftVBox.setSpacing(20)
        
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
        self.addItem.clicked.connect(self.AddItem)


    def RadioSwitchLayout(self):
        if self.currentLayout == 0:
            self.currentLayout += 1
            self.radioStack.setCurrentIndex(self.currentLayout)
        else:
            self.currentLayout -= 1
            self.radioStack.setCurrentIndex(self.currentLayout)


    def AddItem(self):
        self.addItemDialog = QDialog()
        self.addItemDialog.setWindowTitle("Add Item")
        self.addItemWidget = ItemInput()
        self.addItemLayout = QVBoxLayout()
        
        self.addItemLayout.addWidget(self.addItemWidget)
        self.addItemLayout.addWidget(self.buttonBox)
        
        self.addItemDialog.setLayout(self.addItemLayout)
        self.addItemDialog.exec_()
        
        
        
