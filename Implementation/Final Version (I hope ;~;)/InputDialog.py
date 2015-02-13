from PyQt4.QtGui import *

class InputDialog(QDialog):
    """A dialog for inserting data into the database"""
    def __init__(self,title,specify):
        super().__init__()
        self.setWindowTitle("Insert Entry")
