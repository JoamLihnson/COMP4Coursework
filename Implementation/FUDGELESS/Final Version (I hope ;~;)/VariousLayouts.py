from PyQt4.QtGui import *

class ButtonBoxWidget(QWidget):
    """A widget that has a basic OK and Cancel button combo"""
    def __init__(self):
        super().__init__()
        self.OKButton = QPushButton("OK")
        self.CancelButton = QPushButton("Cancel")
        self.buttonBoxLayout = QHBoxLayout()
        self.buttonBoxLayout.addWidget(self.OKButton)
        self.buttonBoxLayout.addWidget(self.CancelButton)
        self.setLayout(self.buttonBoxLayout)

class SQLConstruct():
    """Returns the required SQL strings and stuff for when you need to perform a search"""
    def __init__(self, selection):
        super().__()
        if selection == "Staff":
            Questioned, ListedFields = SelectStaff()
            return(Questioned, ListedFields)
        elif selection == "Donator":
            Questioned, ListedFields = SelectDonator()
            return(Questioned, ListedFields)
        elif selection == "Category":
            Questioned, ListedFields = SelectCategory()
            return(Questioned, ListedFields)
        elif selection == "Item":
            Questioned, ListedFields = SelectItem()
            return(Questioned, ListedFields)
        elif selection == "Donation":
            Questioned, ListedFields = SelectDonation()
            return(Questioned, ListedFields)
        
        def SelectStaff():
            Questioned = "(?,?,?)"
            ListedFields = ["Staff", "StaffID", "StaffFirstName", "StaffLastName"]
            return(Questioned, ListedFields)

        def SelectDonator():
            Questioned = "(?,?,?,?,?,?,?,?,?)"
            ListedFields = ["Donator", "DonatorID", "DonatorFirstName", "DonatorLastName", "DonatorAddress1", "DonatorAddress2", "DonatorCity", "DonatorCounty", "DonatorPostCode", "DonatorContact"]
            return(Questioned, ListedFields)

        def SelectCategory():
            Questioned = "(?,?)"
            ListedFields = ["Category", "ItemCategory", "ItemCategoryDescription"]
            return(Questioned, ListedFields)

        def SelectItem():
            Questioned = "(?,?,?,?,?,?,?)"
            ListedFields = ["Item", "ItemCode", "DonationCode", "ItemDescription", "ItemPrice", "ItemCategory", "ItemQualityCheck", "ItemStatus"]
            return(Questioned, ListedFields)

        def SelectDonation():
            Questioned = "(?,?,?,?)"
            ListedFields = ["Donation", "DonationCode", "DonatorID", "StaffID", "Date"]
            return(Questioned, ListedFields)
