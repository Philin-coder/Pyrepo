import sys
from PyQt5.QtCore import *
import form
from PyQt5 import QtWidgets


class disap(QtWidgets.QWidget, form.Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.test)

    def test(self):
        self.lineEdit.setVisible(False)


def mn():
    app = QtWidgets.QApplication(sys.argv)
    wnd = disap()

    wnd.show()
    app.exec_()


if __name__ == '__main__':
    mn()
