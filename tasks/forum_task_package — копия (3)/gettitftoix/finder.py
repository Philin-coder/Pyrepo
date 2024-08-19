# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finder.UI'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SW(object):
    def setupUi(self, SW):
        SW.setObjectName("SW")
        SW.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SW)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        SW.setCentralWidget(self.centralwidget)

        self.retranslateUi(SW)
        QtCore.QMetaObject.connectSlotsByName(SW)

    def retranslateUi(self, SW):
        _translate = QtCore.QCoreApplication.translate
        SW.setWindowTitle(_translate("SW", "MainWindow"))
        self.pushButton.setText(_translate("SW", "найти файлы"))
