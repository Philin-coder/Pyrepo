import datetime
import sys
import hashlib
import base64
import gui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class mpass(QtWidgets.QWidget, gui.Ui_passphrase):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.parseprint)

    def parseprint(self):
        w = datetime.datetime.now()  #
        # w = w.month
        w = w.minute
        w = str(w)
        w = sys.platform + w
        a = hashlib.md5(w.encode('utf-8')).hexdigest()
        w = a
        w = w + sys.platform
        a = w
        a = base64.b64encode(w.encode())
        w = a
        w = str(w)
        a = hashlib.md5(w.encode('utf-8')).hexdigest()
        w = a
        # print(w)
        self.lineEdit.setText(str(w))
        return w


def main():
    app = QtWidgets.QApplication(sys.argv)
    wnd = mpass()
    wnd.show()
    app.exec_()


if __name__ == '__main__':
    main()
