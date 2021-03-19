import iface
import sys
import os
from PyQt5 import QtWidgets


class ld(QtWidgets.QWidget, iface.Ui_lwo):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit.setFocus()
        self.pushButton.clicked.connect(self.test)
        self.listWidget.itemDoubleClicked.connect(self.shifr)

    def test(self):
        self.listWidget.clear()
        mdr = QtWidgets.QFileDialog.getExistingDirectory(self, "что открыть?")
        global put
        put = os.path.abspath(mdr)
        if mdr:
            for i in (os.listdir(mdr)):
                self.listWidget.addItem(i)
        return put

    def shifr(self, item):
        self.lineEdit.setText(str(2 + 2))

        with open('proba.txt', 'w', encoding='utf-8') as fp:
            print(put, file=fp, sep="\n")
            fp.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    wnd = ld()
    wnd.show()
    app.exec_()


if __name__ == '__main__':
    main()
