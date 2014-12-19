from PyQt4.QtGui import *
from PyQt4.QtCore import *
from RadioButton import *
import sys
import sqlite3

class Database:
    """The database and it's abilities"""
    def __init__(self):
        super().__init__()

        self.Insert = "lel"

class Window (QMainWindow):
    """Charity Shop Program"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Charity Shop Database Management")

        self.resize(750,500)

        self.LoadDatabase = QAction("Load Database", self)
        self.Recreate = QAction("Recreate Database",self)
        self.EndProgram = QAction("Close Program", self)
        self.Insert = QAction("Insert", self)
        self.Update = QAction("Update", self)
        self.Delete = QAction("Delete", self)

        self.menuBar = QMenuBar()
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.EndProgram)
        self.databaseMenu = self.menuBar.addMenu("Database")
        self.databaseMenu.addAction(self.LoadDatabase)
        self.databaseMenu.addAction(self.Recreate)
        self.databaseMenu.addAction(self.Insert)
        self.databaseMenu.addAction(self.Update)
        self.databaseMenu.addAction(self.Delete)

        self.toolBar = QToolBar("ToolBar")
        self.toolBar.addAction(self.Insert)
        self.toolBar.addAction(self.Update)
        self.toolBar.addAction(self.Delete)

        self.addToolBar(self.toolBar)
        self.setMenuBar(self.menuBar)
        self.RadioButtons()

        self.LoadDatabase.triggered.connect(self.LoadDatabaseConnect)
        self.Recreate.triggered.connect(self.RecreateConnect)
        self.EndProgram.triggered.connect(self.EndProgramConnect)
        self.Insert.triggered.connect(self.InsertConnect)
        self.Update.triggered.connect(self.UpdateConnect)
        self.Delete.triggered.connect(self.DeleteConnect)

    def RadioButtons(self):
        self.radioButtonss = RadioButtonWidget("Choose somethin", "Yeah, do that", ("Insert","Update","Delete"))
        self.instantiateButton = QPushButton("Hella")
        self.initialLayout = QVBoxLayout()
        self.initialLayout.addWidget(self.radioButtonss)
        self.initialLayout.addWidget(self.instantiateButton)
        self.selectOption = QWidget()
        self.selectOption.setLayout(self.initialLayout)
        self.setCentralWidget(self.selectOption)
    def LoadDatabaseConnect(self):
        print("Database Loading...")

    def RecreateConnect(self):
        print("Recreating database...")

    def EndProgramConnect(self):
        print("Program gonna close")

    def InsertConnect(self):
        print("Choose data to Insert")

    def UpdateConnect(self):
        print("Choose data to Update")

    def DeleteConnect(self):
        print("Choose data to Delete")

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Database = Database()
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
        

        
        
