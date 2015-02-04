#Thoughts about code#
#A lot of it is copy pasted and could have fancy functions that make it more efficient,
#but it's not worth the trouble, as, at the end of the day, the data inputted will require different
#handling methods, no matter what, and doing fancy input-dependant functions would just take too long and could
#easily lead to errors that take too much trouble to correct

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

        self.buttonBox = QHBoxLayout()
        self.OKButton = QPushButton("OK")
        self.CancelButton = QPushButton("Cancel")
        self.buttonBox.addWidget(self.OKButton)
        self.buttonBox.addWidget(self.CancelButton)

        self.entrySelectWidget = QWidget()
        self.entrySelectWidget.setLayout(self.dialogGrid)

        self.categoryButton.clicked.connect(self.CategoryInput)
        self.donatorButton.clicked.connect(self.DonatorInput)
        self.donationButton.clicked.connect(self.DonationInput)
        self.itemButton.clicked.connect(self.ItemInput)


    def CategoryInput(self):
        self.categoryBox = QVBoxLayout()
        self.categoryLabel = QLabel("New Category")
        self.LineEdit1 = QLineEdit()
        self.categoryBox.addWidget(self.categoryLabel)
        self.categoryBox.addWidget(self.LineEdit1)
        self.categoryBox.addLayout(self.buttonBox)
        self.categoryEntryWidget = QWidget()
        self.categoryEntryWidget.setLayout(self.categoryBox)
        self.stackedLayout.addWidget(self.categoryEntryWidget)
        self.stackedLayout.setCurrentIndex(1)

        self.entryAmount = 1

        self.CancelButton.clicked.connect(self.close)
        self.OKButton.clicked.connect(self.InsertDataFinal)

    def DonatorInput(self):
        self.doantorBox = QVBoxLayout()
        self.setWindowTitle("Donator Insert")
        
        self.firstName = QLabel("First Name")
        self.LineEdit1 = QLineEdit()
        self.lastName = QLabel("Last Name")
        self.LineEdit2 = QLineEdit()
        self.address1 = QLabel("Address Line 1")
        self.LineEdit3 = QLineEdit()
        self.address2 = QLabel("Address Line 2")
        self.LineEdit4 = QLineEdit()
        self.city = QLabel("City")
        self.LineEdit5 = QLineEdit()
        self.county = QLabel("County")
        self.LineEdit6 = QLineEdit()
        self.postCode = QLabel("PostCode")
        self.LineEdit7 = QLineEdit()
        self.contact = QLabel("Contact")
        self.LineEdit8 = QLineEdit()
        
        self.leftVBox = QVBoxLayout()
        self.rightVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.firstName)
        self.leftVBox.addWidget(self.LineEdit1)
        self.leftVBox.addWidget(self.lastName)
        self.leftVBox.addWidget(self.LineEdit2)
        self.leftVBox.addWidget(self.address1)
        self.leftVBox.addWidget(self.LineEdit3)
        self.leftVBox.addWidget(self.address2)
        self.leftVBox.addWidget(self.LineEdit4)
        self.rightVBox.addWidget(self.city)
        self.rightVBox.addWidget(self.LineEdit5)
        self.rightVBox.addWidget(self.county)
        self.rightVBox.addWidget(self.LineEdit6)
        self.rightVBox.addWidget(self.postCode)
        self.rightVBox.addWidget(self.LineEdit7)
        self.rightVBox.addWidget(self.contact)
        self.rightVBox.addWidget(self.LineEdit8)
        self.middleHBox = QHBoxLayout()
        self.middleVBox = QVBoxLayout()
        self.middleHBox.addLayout(self.leftVBox)
        self.middleHBox.addLayout(self.rightVBox)
        self.middleVBox.addLayout(self.middleHBox)
        self.middleVBox.addLayout(self.buttonBox)

        self.donatorEntryWidget = QWidget()
        self.donatorEntryWidget.setLayout(self.middleVBox)
        self.stackedLayout.addWidget(self.donatorEntryWidget)
        self.stackedLayout.setCurrentIndex(1)
        

        self.entryAmount = 8

        self.CancelButton.clicked.connect(self.close)
        self.OKButton.clicked.connect(self.InsertDataFinal)


#since I decided to be wacky and random in that ALL the code for inputting data will be in the dialog, shits tough
#this is very painful as im going to just return the values to the main program to have them be inputted in the database,
#despite the fact Im making database connections in this code. I might as well ship them to the db from here
#oh well...

#here is my main issue. Since different entries use differently named variables (because I am that brilliant)
#I can't use the same method I did in my CLI where it could figure out what you wanted, and thus didn't need
#a new function for each entry
#wait i got a idea

#If I include a "global" variable (~~not actually global silly~~) that gets changed depending on what thing you choose
#then I will only need 1 function, as that variable will tell the function what to do
#its gonna be a bigass function though. Practically all my other potential functions just combined into 1
#yay

#for loops or long lists? one looks neater, by if I cock it up it will be a super rookie mistake and super stupid
#for glory, fun, and diddy kong

#well shit, no theres not point in having similar variable execept saving a few bytes and confusing code

#thinking about it, dont bother returning it back to the main window. too complex and uneccessary

        




    def DonationInput(self):
        self.setWindowTitle("Donation Insert")

        pass

    def ItemInput(self):
        self.setWindowTitle("Item Insert")

    def InsertDataFinal(self):
        if self.entryAmount == 1:
            #make ItemCategory the next number in the db list
            #make a list with number first, category second
            #tuple and ditch it baby
            
            
        elif self.entryAmount == 8:
            #generate the ID
            #list it all
            #tuple and ditch
            pass
        else:
            pass
