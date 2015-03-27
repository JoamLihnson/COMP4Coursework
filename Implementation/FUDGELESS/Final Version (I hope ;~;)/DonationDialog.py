from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3
import time
from InputSelect import DonatorInput
from InputSelect import ItemInput
from VariousLayouts import ButtonBoxWidget
import random

class DonationDialogClass(QDialog):
    """A dialog when an item is donated"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Donation Information")
        self.setFixedSize(600,500)
        
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
        self.donatorTest = QPushButton("Test Donator Adding")

        self.tableView = QTableWidget()
        self.tableView.setColumnCount(2)
        self.tableView.setRowCount(1)

        for count in range (2):
            self.tableView.setColumnWidth(count,166)
        header = QTableWidgetItem("Description")
        self.tableView.setHorizontalHeaderItem(0,header)
        header = QTableWidgetItem("Category")
        self.tableView.setHorizontalHeaderItem(1,header)
        self.buttonBox = ButtonBoxWidget()        
        self.leftVBox.addWidget(self.RadioButtons)
        self.leftVBox.addWidget(self.addItem)
        self.addItem.setFixedWidth(350)
        self.leftVBox.addWidget(self.donatorTest)
        self.leftVBox.addWidget(self.tableView)
        self.leftVBox.addWidget(self.buttonBox)
        
        self.donatorLayout = DonatorInput()
        self.existingDonator = QVBoxLayout()
        self.existSearch = QPushButton("Search")
        self.IDLabel = QLabel("Donator ID :")
        self.IDEdit = QLineEdit()
        self.IDEdit.setReadOnly(True)
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
        self.donatorTest.clicked.connect(self.AddDonatorTest)
        self.buttonBox.CancelButton.clicked.connect(self.close)
        self.existSearch.clicked.connect(self.SearchDonator)

    def AddDonatorTest(self):
        self.donatorInfo = []
        self.donatorInfo.append(self.donatorLayout.LineEdit1.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit2.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit3.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit4.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit5.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit6.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit7.text())
        self.donatorInfo.append(self.donatorLayout.LineEdit8.text())
        print(self.donatorInfo)
        self.donatorIDGen = "R"
        for count in range(2):
            self.donatorIDGen += ((self.donatorInfo[count])[:1])
        print(self.donatorIDGen)
        randCode = []
        for count in range(3):
            randCode.append(random.randint(0,9))
        randCode.append(str(randCode[0] + randCode[1] + randCode[2]))
        print(randCode)
        if len(randCode[3]) == 1:
            randCode[3] = "0" + randCode[3]
        randCode.append(str(randCode[0])+str(randCode[1])+str(randCode[2])+((randCode[3])[1:]))
        print(randCode)
        self.donatorIDGen += randCode[4]
        print(self.donatorIDGen)
        self.donatorInfo.insert(0,self.donatorIDGen)
        print(self.donatorInfo)
        sql = "insert into Donator(DonatorID,DonatorFirstName,DonatorLastName,DonatorAddress1,DonatorAddress2,DonatorCity,DonatorCounty,DonatorPostCode,DonatorContact) values (?,?,?,?,?,?,?,?,?)"
        self.donatorInfo = tuple(self.donatorInfo)
        with sqlite3.connect("charityShop.db") as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            cursor.execute(sql, self.donatorInfo)
            db.commit()
        
                        
        
        



    def RadioSwitchLayout(self):
        if self.currentLayout == 0:
            self.currentLayout += 1
            self.radioStack.setCurrentIndex(self.currentLayout)
        else:
            self.currentLayout -= 1
            self.radioStack.setCurrentIndex(self.currentLayout)
        

    def AddItem(self):
        self.addItemDialog = AddItemClass()
        self.addItemDialog.exec_()
        temInfo = self.addItemDialog.values()
        self.addItemDialog.close()
        if temInfo != "":
            self.tableView.insertRow(1)
            print(temInfo)

            tableItem = QTableWidgetItem()
            tableItem.setText(temInfo[2])
            print(temInfo[2])
            self.tableView.setItem(1,1,tableItem)
            with sqlite3.connect("charityShop.db") as db:
                sql = "select ItemCategoryDescription from Category where ItemCategory = {}".format(str(temInfo[4]))
                cursor = db.cursor()
                cursor.execute(sql)
                selected = cursor.fetchall()
            tableItem.setText(selected[0][0])
            self.tableView.setItem(0,2,tableItem)
        else:
            pass


    def SearchDonator(self):
        self.searchDonatorDialog = SearchDonatorClass()
        self.searchDonatorDialog.exec_()
        returnedID = self.searchDonatorDialog.values()
        if returnedID != "":
            self.IDEdit.setText(returnedID.text())
        else:
            self.IDEdit.setText(returnedID)



#############################################################
class SearchDonatorClass(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Donator Search")
            self.OKHit = False
            self.setFixedSize(1150,500)
            self.searchBarBox = QHBoxLayout()
            self.searchBar = QLineEdit()
            self.searchBar.setMaximumWidth(150)
            self.searchButton = QPushButton("Search")
            self.primKeyLabel = QLabel("Primary Key : ")
            self.primKeySelected = QLabel("")
            self.buttonBox = ButtonBoxWidget()   

            
            self.ListedFields = ["Donator", "DonatorID", "DonatorFirstName", "DonatorLastName", "DonatorAddress1", "DonatorAddress2", "DonatorCity", "DonatorCounty", "DonatorPostCode", "DonatorContact"]

            self.tableWidget = QTableWidget()

            self.tableWidget.setColumnCount(9)

            for count in range(len(self.ListedFields)-1):
                
                
                header = QTableWidgetItem((self.ListedFields[count+1])[7:])
                self.tableWidget.setHorizontalHeaderItem(count,header)
                self.tableWidget.setColumnWidth(count,120)
            self.tableWidget.setRowCount(4)
            self.tableWidget.setCornerButtonEnabled(False)

            self.searchBarBox.addWidget(self.searchBar)
            self.searchBarBox.addWidget(self.searchButton)
            self.searchBarBox.addWidget(self.primKeyLabel)
            self.searchBarBox.addWidget(self.primKeySelected)
            self.searchBarBox.addWidget(self.buttonBox)
            self.wholeDialog = QVBoxLayout()
            self.wholeDialog.addLayout(self.searchBarBox)
            self.wholeDialog.addWidget(self.tableWidget)
            self.setLayout(self.wholeDialog)

            self.tableWidget.cellClicked.connect(self.DisplayKey)          

            self.buttonBox.CancelButton.clicked.connect(self.close)
            self.buttonBox.OKButton.clicked.connect(self.OKCheck)
            self.searchButton.clicked.connect(self.GoSearch)


        def OKCheck(self):
            self.OKHit = True
            self.close()

        def DisplayKey(selfh, selectRow, selectColumn):
            primKeyItem = self.tableWidget.item(selectRow,0)
            primKeyItem = primKeyItem.text()
            self.primKeySelected.setText(primKeyItem)
            
            
            

        def GoSearch(self):
            self.tableWidget.setRowCount(0)
            results =[]
            for count in range(len(self.ListedFields)-1):
                sql = "select * from Donator where {}=?".format(self.ListedFields[count+1])
                selected = self.Query(sql,self.searchBar.text())
                for count in range(len(selected)):
                    results.append(selected[count])
            for count in range(len(results)):
                self.tableWidget.insertRow(count)
                currentEntry = results[count]
                for counting in range(9):
                    tableItem = QTableWidgetItem()
                    tableItem.setText(currentEntry[counting])
                    self.tableWidget.setItem(count,counting,tableItem)


        def values(self):
            if self.OKHit == True:
                return(self.primKeySelected)
            else:
                return("")
                    
                    
                
                    
                                                                
                                                                

        def Query (self,sql,data):
            with sqlite3.connect("charityShop.db") as db:
                cursor = db.cursor()
                cursor.execute("PRAGMA foreign_keys = ON")
                cursor.execute(sql, (data,))
                selected = cursor.fetchall()
                db.commit()
                return(selected)
            
#############################################################
class AddItemClass(QDialog):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Add Item")
            self.OKHit = False
            self.setFixedSize(250,220)
            self.addItemWidget = ItemInput()
            self.addItemWidget.priceLabel.setDisabled(True)
            self.addItemWidget.priceEdit.setDisabled(True)
            self.addItemWidget.qualityLabel.setDisabled(True)
            self.addItemWidget.statusLabel.setDisabled(True)
            self.addItemWidget.donationLabel.setDisabled(True)
            self.addItemWidget.qualityCheck.setDisabled(True)
            self.addItemWidget.statusCombo.setDisabled(True)
            self.addItemWidget.donationEdit.setDisabled(True)
                     
            self.addItemLayout = QVBoxLayout()
            self.buttonBox = ButtonBoxWidget()   
        
            self.addItemLayout.addWidget(self.addItemWidget)
            self.addItemLayout.addWidget(self.buttonBox)
        
            self.setLayout(self.addItemLayout)

            self.buttonBox.CancelButton.clicked.connect(self.close)
            self.buttonBox.OKButton.clicked.connect(self.Validate)

        def Validate(self):
            #there will be validation code
            self.EnterTable()
            pass
        
        def EnterTable(self): 
            randCode = []
            for count in range(5):
                randCode.append(random.randint(0,9))
            randCode.append(randCode[0] + randCode[1] + randCode[2] + randCode[3] + randCode[4])    
            if randCode[5] > 26:
                randCode[5] +=70
            else:
                randCode[5] += 96
            randCode.append(chr(randCode[5]))
            IDGen = "I" + str(randCode[0]) + str(randCode[1]) + str(randCode[2]) + str(randCode[3]) + str(randCode[4]) + randCode[6].upper()
            print(IDGen)
            print(self.addItemWidget.categoryCombo.currentIndex())
            self.ItemData = [IDGen, "Donation Code", self.addItemWidget.descriptEdit.text(), "0.00", self.addItemWidget.categoryCombo.currentIndex()+1, False, "Stored"]
            print(self.ItemData)
            self.OKHit = True
            self.close()
            

        def values(self):
            if self.OKHit == True:
                return(self.ItemData)
            else:
                return("")
            
        
