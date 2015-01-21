from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3

class DonateDialog (QDialog):
    """Used to input data"""

    def __init__(self):
        super:().__init__()
        self.setWindowTitle("Donation")



        self.boxLayout = QVBoxLayout
        self.donateLayout = QGridLayout

        self.textBox = QLineEdit()
        self.textBox2 = QLineEdit()

        self.donateLayout.addWidget(self.textBox, 1, 0)
        self.donateLayout.addWidget(self.textBox2, 1, 1)

        
