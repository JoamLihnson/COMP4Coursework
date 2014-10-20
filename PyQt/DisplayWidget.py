from PyQt4.QGui import *
from PyQt4.QCore import *

class DisplayWidget (QWidget):
    """Main Widget"""
    def __init__(self):
        self.stacked_layout = QStackedLayout()
        self.model = None
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()
        self.results_widget = QWidget()
        self.display_results_layout()

    def display_results_layout(self):

    def show_results(self):

    def show_table(self):
        
