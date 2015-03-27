from PyQt.4Gui import *

class TableWidget(QWidget):
    """Creates a table, given different values"""
    def __init__(self, rows, columns):
        super().__init__()

        self.tableWidget = new QTableWidget(12, 3, this);
        
