from collections import Counter
import sys
import ParseForm
from PyQt5 import QtWidgets


class mparse(QtWidgets.QMainWindow, ParseForm.Ui_Parseform):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.test)

    def test(self):
        self.lineEdit.setText("gutt")
        myhtml = self.lineEdit.text()


def mn():
    app = QtWidgets.QApplication(sys.argv)
    wnd = mparse()
    wnd.show()
    app.exec_()


if __name__ == '__main__':
    mn()
