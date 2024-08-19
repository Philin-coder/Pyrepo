import requests
import pygame
import os
import sys

import myconstants
from myconstants import *
from pygame.locals import *
import shutil
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import lxml.html
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 609)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.texturl = QtGui.QLabel(self.centralwidget)
        self.texturl.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.texturl.setObjectName(_fromUtf8("texturl"))
        self.lineEditlink = QtGui.QLineEdit(self.centralwidget)
        self.lineEditlink.setGeometry(QtCore.QRect(80, 0, 671, 20))
        self.lineEditlink.setObjectName(_fromUtf8("lineEditlink"))
        self.folderedit = QtGui.QLineEdit(self.centralwidget)
        self.folderedit.setGeometry(QtCore.QRect(80, 20, 671, 20))
        self.folderedit.setObjectName(_fromUtf8("folderedit"))
        self.foldername = QtGui.QLabel(self.centralwidget)
        self.foldername.setGeometry(QtCore.QRect(0, 20, 71, 16))
        self.foldername.setObjectName(_fromUtf8("foldername"))
        self.restext = QtGui.QTextEdit(self.centralwidget)
        self.restext.setGeometry(QtCore.QRect(3, 70, 751, 441))
        self.restext.setObjectName(_fromUtf8("restext"))
        self.parsbutton = QtGui.QPushButton(self.centralwidget)
        self.parsbutton.setGeometry(QtCore.QRect(0, 510, 751, 61))
        self.parsbutton.setObjectName(_fromUtf8("parsbutton"))
        self.filenamelabel = QtGui.QLabel(self.centralwidget)
        self.filenamelabel.setGeometry(QtCore.QRect(0, 40, 71, 16))
        self.filenamelabel.setObjectName(_fromUtf8("filenamelabel"))
        self.filenameedit = QtGui.QLineEdit(self.centralwidget)
        self.filenameedit.setGeometry(QtCore.QRect(80, 40, 671, 20))
        self.filenameedit.setObjectName(_fromUtf8("filenameedit"))
        self.closer = QtGui.QPushButton(self.centralwidget)
        self.closer.setGeometry(QtCore.QRect(0, 570, 751, 41))
        self.closer.setObjectName(_fromUtf8("closer"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.texturl.setText(_translate("MainWindow", "текст ссылки", None))
        self.foldername.setText(_translate("MainWindow", "Имя папки", None))
        self.parsbutton.setText(_translate("MainWindow", "парсинг", None))
        self.filenamelabel.setText(_translate("MainWindow", "Имя файла", None))
        self.closer.setText(_translate("MainWindow", "выбрать", None))


if __name__ == "__main__":
    import sys

    linklist = []
    playlist = []
    app = QtGui.QApplication(sys.argv)

    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    QtCore.QObject.connect(ui.parsbutton, QtCore.SIGNAL("clicked()"), lambda: Mparser(ui))
    QtCore.QObject.connect(ui.closer, QtCore.SIGNAL("clicked()"), lambda: reader(ui))


    def Mparser(ui):
        f = myhtml = urlopen(URL)
        sp = BeautifulSoup(myhtml, "html.parser")
        lnk = sp.findAll("a", class_="playlist-btn-down")
        os.mkdir(ui.folderedit.text())
        os.chdir(os.getcwd() + '\\' + ui.folderedit.text() + '\\')
        char = "."
        for l in lnk:
            l = str(l)
            l = l.replace('"', ' ')
            l = l.replace('<a class=', ' ')
            l = l.replace('playlist-btn-down no-ajaxy', '')
            l = l.replace('\'', '')
            l = l.replace('target= _blank  title= скачать >(скачать)</a>', ' ')
            l = l.replace('download', 'listen')
            l = l.replace('href=', ' ')
            linklist.append(l)
        with open(ui.filenameedit.text() + '.' + fext2, 'w', encoding='utf-8') as fp:
            print(*linklist, file=fp, sep="\n")
            fp.close()
            msg = QtGui.QMessageBox()
            msg.setIcon(QtGui.QMessageBox.Information)
            msg.setInformativeText("Список создан")
            msg.addButton(QtGui.QMessageBox.Ok)
            msg.exec_()
            return linklist


    def reader(ui):
        msg1 = QtGui.QFileDialog


    MainWindow.show()
    sys.exit(app.exec_())
