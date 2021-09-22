# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ParseForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Parseform(object):
    def setupUi(self, Parseform):
        Parseform.setObjectName("Parseform")
        Parseform.resize(766, 600)
        self.centralwidget = QtWidgets.QWidget(Parseform)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 0, 781, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 781, 511))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 540, 771, 23))
        self.pushButton.setObjectName("pushButton")
        Parseform.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Parseform)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 766, 21))
        self.menubar.setObjectName("menubar")
        Parseform.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Parseform)
        self.statusbar.setObjectName("statusbar")
        Parseform.setStatusBar(self.statusbar)

        self.retranslateUi(Parseform)
        QtCore.QMetaObject.connectSlotsByName(Parseform)

    def retranslateUi(self, Parseform):
        _translate = QtCore.QCoreApplication.translate
        Parseform.setWindowTitle(_translate("Parseform", "MainWindow"))
        self.pushButton.setText(_translate("Parseform", "Пjлучить Объект"))
