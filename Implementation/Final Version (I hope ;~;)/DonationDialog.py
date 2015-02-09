from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import sqlite3
import time

class DonationDialogClass(QDialog):
    """A dialog when an item is donated"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Donation Information")
