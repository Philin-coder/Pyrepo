from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from PyQt5 import QtWidgets
import grab
import sys, os
import finder
import parse
import re
from PyQt5.QtWidgets import QMessageBox


class mgb(QtWidgets.QMainWindow, grab.Ui_MainWindow):

    def __init__(self):  # init в предке
        super().__init__()
        self.wim = fnd()
        self.newin = mparse()
        self.setupUi(self)
        self.lineEdit.setFocus()
        self.pushButton.clicked.connect(self.Mget)
        self.pushButton_2.clicked.connect(self.mwin)
        self.pushButton_3.clicked.connect(self.parshow)

    def Mget(self):
        # self.lineEdit.setText(str("www.yandex.ru"))
        url = "http://" + self.lineEdit.text()
        f = myhtml = urlopen(url)
        sp = BeautifulSoup(myhtml, "html.parser")
        self.plainTextEdit.appendPlainText(str(sp))
        # print(sp)
        QMessageBox.about(self, "Внимание!", "Объект получен")

        with open(str(time.time()) + '.' + 'txt', 'w', encoding='utf-8') as fp:
            print(sp, file=fp, sep="\n")
            fp.close()
            QMessageBox.about(self, "Внимание!", "код получен")

    def mwin(self):
        self.wim.show()

    def parshow(self):
        self.newin.show()


class fnd(QtWidgets.QMainWindow, finder.Ui_SW):  # U I

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.fget)

    def fget(self):
        self.listWidget.clear()
        mdir = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбирайте папку")
        if mdir:
            for i in (os.listdir(os.getcwd())):
                if i.endswith('txt'):
                    self.listWidget.addItem(i)


class mparse(QtWidgets.QWidget, parse.Ui_parswidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #     self.pushButton.clicked.connect(self.test)
    #     self.pushButton_2.clicked.connect(self.lister)
    # def test(self):
    #     mdir1 = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбирайте папку с копией")
    #     if mdir1:
    #         for i in (os.listdir(os.getcwd())):
    #             if i.endswith('txt'):
    #                 with open(i, 'r', encoding='utf-8') as fp:
    #                     tegs = []
    #                     res = []
    #                     tegs = fp.readlines()
    #                     fp.close()
    #                     tegs = str(tegs)
    #                     self.plainTextEdit.appendPlainText(str(tegs))
    #                     QMessageBox.about(self, "Внимание!", "Файл прочитан")
    #                     fstr = self.lineEdit.text()
    #                     for i in re.findall(fstr, tegs):
    #                         res.append(i)
    #                     res=str(res)
    #                     self.plainTextEdit.clear()
    #                     self.plainTextEdit.appendPlainText(str(res))
    #                     mlist = list(res)
    #
    # def lister(self):
    #     mdir2 = QtWidgets.QFileDialog.getExistingDirectory(self, "Выбирайте папку с копией")
    #     if mdir2:
    #         for i in (os.listdir(os.getcwd())):
    #             if i.endswith('txt'):
    #                 with open(i, 'r', encoding='utf-8') as fp:
    #                     mlist=[]
    #                     mlist2 = []
    #                     mlist = fp.readlines()
    #                     fp.close()
    #                     # print(mlist)
    #                     for i in mlist:
    #                         i=str(i)
    #                         i.replace(str(self.lineEdit.text), str(self.lineEdit_2.text))
    #                         mlist2.append(i)
    #                         print(mlist2)
    # перренести


def main():
    app = QtWidgets.QApplication(sys.argv)
    wnd = mgb()
    wnd.show()
    app.exec_()


if __name__ == '__main__':
    main()
