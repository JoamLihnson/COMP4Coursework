from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class MakeMeAWindowWithTooMuchDefinitionText (QMainWindow):
    """Best Window iirc"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A title aggaa")

if __name__ == "__main__":
    dizApplication = QApplication(sys.argv)
    wandow = MakeMeAWindowWithTooMuchDefinitionText()
    wandow.show()
    wandow.raise_()
    dizApplication.exec_()
