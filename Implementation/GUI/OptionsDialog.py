#Code for opening and using the Options dialog

from PyQt4.QtGui import *

class OptionsDialog(QWidget):
    """Opens the options dialog for option changing"""
    def __init__(self,windowTitle,fileTypes):
        super().__init__()

        self.titleLabel
