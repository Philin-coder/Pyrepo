# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parse.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_parswidget(object):
    def setupUi(self, parswidget):
        parswidget.setObjectName("parswidget")
        parswidget.resize(686, 360)
        self.verticalLayout = QtWidgets.QVBoxLayout(parswidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parswidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parswidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(parswidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(parswidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parswidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(parswidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(parswidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)

        self.retranslateUi(parswidget)
        QtCore.QMetaObject.connectSlotsByName(parswidget)

    def retranslateUi(self, parswidget):
        _translate = QtCore.QCoreApplication.translate
        parswidget.setWindowTitle(_translate("parswidget", "Form"))
        self.label.setText(_translate("parswidget", "введите искомы тег"))
        self.label_2.setText(_translate("parswidget", "введите убираемый фрагмент "))
        self.pushButton.setText(_translate("parswidget", "найти тег"))
        self.pushButton_2.setText(_translate("parswidget", "Очистить"))
