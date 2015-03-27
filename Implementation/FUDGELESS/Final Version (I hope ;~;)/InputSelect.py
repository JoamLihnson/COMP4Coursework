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
        

class ItemInput(QWidget):
    """Layout for when inputting Item data"""
    def __init__(self):
        super().__init__()

        self.descriptLabel = QLabel("Item Description")
        self.priceLabel = QLabel("Price (£)")
        self.categoryLabel = QLabel("Category")
        self.qualityLabel = QLabel("Quality Check")
        self.statusLabel = QLabel("Current Status")
        self.donationLabel  = QLabel("Donation Code")
        self.descriptEdit = QLineEdit()
        self.priceEdit = QLineEdit()
        self.categoryCombo = QComboBox()
        self.qualityCheck = QCheckBox()
        self.statusCombo = QComboBox()
        self.donationEdit = QLineEdit()

        self.statusCombo.addItem("Stored")
        self.statusCombo.addItem("Shop Front")
        self.statusCombo.addItem("Sold")

        with sqlite3.connect("charityShop.db") as db:
            sql = "select * from Category"
            cursor = db.cursor()
            cursor.execute(sql)
            selected = cursor.fetchall()
            db.commit()
            for count in range(len(selected)):
                primKey, textCate = selected[count]
                self.categoryCombo.addItem(textCate)

        self.leftVBox = QVBoxLayout()
        self.rightVBox = QVBoxLayout()
        self.leftVBox.addWidget(self.descriptLabel)
        self.leftVBox.addWidget(self.priceLabel)
        self.leftVBox.addWidget(self.categoryLabel)
        self.leftVBox.addWidget(self.qualityLabel)
        self.leftVBox.addWidget(self.statusLabel)
        self.leftVBox.addWidget(self.donationLabel)
        self.rightVBox.addWidget(self.descriptEdit)
        self.rightVBox.addWidget(self.priceEdit)
        self.rightVBox.addWidget(self.categoryCombo)
        self.rightVBox.addWidget(self.qualityCheck)
        self.rightVBox.addWidget(self.statusCombo)
        self.rightVBox.addWidget(self.donationEdit)
        self.itemBox = QHBoxLayout()
        self.itemBox.addLayout(self.leftVBox)
        self.itemBox.addLayout(self.rightVBox)
        self.setLayout(self.itemBox)


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

        
    
