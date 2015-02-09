from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """Uses a list to make radio buttons, yo"""
    def __init__(self, title, instruction, buttonList):
        super().__init__()

        self.titleLabel = QLabel(title)
        self.radioGroupBox = QGroupBox(instruction)
        self.radioButtonGroup = QButtonGroup()

        self.radioButtonList = []
        for each in buttonList:
            self.radioButtonList.append(QRadioButton(each))

        self.radioButtonLayout = QVBoxLayout()

        counter = 1
        for each in self.radioButtonList:
            print(each)
            self.radioButtonLayout.addWidget(each)
            self.radioButtonGroup.addButton(each)
            self.radioButtonGroup.setId(each, counter)
            counter += 1
        self.radioGroupBox.setLayout(self.radioButtonLayout)
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.radioGroupBox)

        self.setLayout(self.mainLayout)

    def selectedButton(self):
        return self.radioButtonGroup.checkId()
