import sys
from PyQt4 import QtGui


def main():
    
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QWidget()
    w.resize(250, 150)
    w.move(835, 465)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
