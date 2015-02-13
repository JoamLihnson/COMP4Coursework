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

