from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class Window (QMainWindow):
    """Best Window iirc"""
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("A title aggaa")
        
        self.open_database = QAction("Open Database",self)
        self.close_database = QAction("Close Database", self)
        self.file_dialog = QAction("File Dialog", self)
        self.find_products = QAction("Find Prodcuts", self)
        self.show_products = QAction("Show Prodcuts", self)
        
        self.menu_bar = QMenuBar()
        self.file_menu = self.menu_bar.addMenu("Database")
        self.file_menu.addAction(self.open_database)
        self.file_menu.addAction(self.close_database)
        self.file_menu.addAction(self.file_dialog)
        self.products_menu = self.menu_bar.addMenu("Products")
        self.products_menu.addAction(self.find_products)
        self.products_menu.addAction(self.show_products)
        
        self.tool_bar = QToolBar("Toolbar")
        self.tool_bar.addAction(self.open_database)
        self.tool_bar.addAction(self.close_database)
        self.tool_bar.addAction(self.file_dialog)
        
        self.addToolBar(self.tool_bar)
        self.setMenuBar(self.menu_bar)

        self.open_database.triggered.connect(self.open_database_connection)
        self.close_database.triggered.connect(self.close_database_connection)
        self.file_dialog.triggered.connect(self.file_dialog_connection)

    def open_database_connection(self):
        print("HAHA BET YOU THOUGHT THIS WOULD OPEN A DATABASE HAHHAHAHA")

    def close_database_connection(self):
        print("ech")

    def file_dialog_connection(self):
        print("OPEN")

if __name__ == "__main__":
    Application = QApplication(sys.argv)
    Window = Window()
    Window.show()
    Window.raise_()
    Application.exec_()
