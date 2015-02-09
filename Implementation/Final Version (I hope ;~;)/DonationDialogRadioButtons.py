from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """The radio buttons that appear in the donation dialog"""
    def __init__(self):
        super().__init__()

        self.radioBox = QGroupBox("Select an option")
        self.radioGroup = QButtonGroup()
        self.radioButtons = [QRadioButton("New Donator"),QRadioButton("Existing Donator")]
        self.radioLayout = QVBoxLayout()
        count = 1
        for button in radioButtons:
            self.radioLayout.addWidget(button)
            self.radioGroup.addButton(button)
            self.radioGroup.setId(button, count)
            count += 1
        self

        
