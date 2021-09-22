# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_passphrase(object):
    def setupUi(self, passphrase):
        passphrase.setObjectName("passphrase")
        passphrase.resize(400, 76)
        self.label = QtWidgets.QLabel(passphrase)
        self.label.setGeometry(QtCore.QRect(10, 0, 47, 13))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(passphrase)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 381, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(passphrase)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 381, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(passphrase)
        QtCore.QMetaObject.connectSlotsByName(passphrase)

    def retranslateUi(self, passphrase):
        _translate = QtCore.QCoreApplication.translate
        passphrase.setWindowTitle(_translate("passphrase", "пароль"))
        self.label.setText(_translate("passphrase", "пароль"))
        self.pushButton.setText(_translate("passphrase", "создать"))
