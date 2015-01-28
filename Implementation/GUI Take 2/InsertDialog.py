from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

class InsertDialogClass(QDialog):
    """A dialog for inserting data into the database"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Entry")

        self.EntrySelect()

        self.stackedLayout = QStackedLayout()
        self.stackedLayout.addWidget(self.entrySelectWidget)

        self.setLayout(self.stackedLayout)


    def EntrySelect(self):

        self.dialogGrid = QGridLayout()
        self.categoryButton = QPushButton("Category")
        self.donatorButton = QPushButton("Donator")
        self.donationButton = QPushButton("Donation")
        self.itemButton = QPushButton("Item")

        self.dialogGrid.addWidget(self.categoryButton,0,0)
        self.dialogGrid.addWidget(self.donatorButton,1,0)
        self.dialogGrid.addWidget(self.donationButton,0,1)
        self.dialogGrid.addWidget(self.itemButton,1,1)

        self.entrySelectWidget = QWidget()
        self.entrySelectWidget.setLayout(self.dialogGrid)

        self.categoryButton.clicked.connect(self.CategoryInput)


    def CategoryInput(self):
        self.setWindowTitle("Category Insert")
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        self.numberLabel  = QLabel("Category Number")
        self.categoryLabel = QLabel("Category")
        self.numberEdit = QLineEdit()
        self.categoryEdit = QLineEdit()
        self.leftVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.numberLabel)
        self.leftVBox.addWidget(self.numberEdit)
        self.rightVBox = QVBoxLayout()
        self.rightVBox.addWidget(self.categoryLabel)
        self.rightVBox.addWidget(self.categoryEdit)
        self.middleHBox = QHBoxLayout()
        self.middleHBox.addLayout(self.leftVBox)
        self.middleHBox.addLayout(self.rightVBox)
        self.middleVBox = QVBoxLayout()
        self.middleVBox.addLayout(self.middleHBox)
        self.middleVBox.addWidget(self.buttonBox)

        self.categoryEntryWidget = QWidget()
        self.categoryEntryWidget.setLayout(self.middleVBox)
        self.stackedLayout.addWidget(self.categoryEntryWidget)
        self.stackedLayout.setCurrentIndex(1)
