#The logic with this program is that I have a seperate module (the below code) with several different classes
#When I want somehting, I dont need to import everything
#Far more efficient, and doesn't add any complexity


from PyQt4.QtGui import *
import sqlite3



class StaffInput(QWidget):
    """Layout for when inputting Staff data"""
    def __init__(self):
        super().__init__()

        self.fNameLabel = QLabel("First Name")
        self.lNameLabel = QLabel("Last Name")
        self.fNameEdit = QLineEdit()
        self.lNameEdit = QLineEdit()
        self.leftVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.fNameLabel)
        self.leftVBox.addWidget(self.fNameEdit)
        self.rightVBox = QVBoxLayout()
        self.rightVBox.addWidget(self.lNameLabel)
        self.rightVBox.addWidget(self.lNameEdit)
        self.staffBox = QHBoxLayout()
        self.setLayout(self.staffBox)

class CategoryInput(QWidget):
    """Layout for when inputting Category data"""
    def __init__(self):
        super().__init__()

        self.categoryBox = QVBoxLayout()
        self.categoryLabel = QLabel("New Category")
        self.LineEdit1 = QLineEdit()
        self.categoryBox.addWidget(self.categoryLabel)
        self.categoryBox.addWidget(self.LineEdit1)
        self.categoryBox.addLayout(self.buttonBox)
        self.setLayout(categoryBox)
        

#class ItemInput(QWidget):
 #   """Layout for when inputting Item data"""
  #  def __init__(self):
  ##      super().__init__()
#
   #     self.descriptLabel = QLabel("Item Description")
    #    self.priceLabel = QLabel("Price (£)")
     #   self.categoryLabel = QLabel("Category")
      #  self.qualityLabel = QLabel("Quality Check")
       # self.statusLabel = QLabel("Current Status")
 #       self.descriptEdit = QLineEdit()
  #      self.priceEdit = QLineEdit()
   #     self.categorySpin = QSpinBox()
    #    self.qualityCheck = #This will be a check box
     #   self.statusSpin = QSpinBox()

        #FINISH THIS WHEN YOU HAVE INTERNET

class DonatorInput(QWidget):
    """Layout for when inputting Donator data"""
    def __init__(self):
        super().__init__()

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
        self.donatorBox = QHBoxLayout()
        self.donatorBox.addLayout(self.leftVBox)
        self.donatorBox.addLayout(self.rightVBox)
        self.setLayout(self.donatorBox)

        
    