# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lwo(object):
    def setupUi(self, lwo):
        lwo.setObjectName("lwo")
        lwo.resize(897, 253)
        self.formLayoutWidget = QtWidgets.QWidget(lwo)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 894, 249))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.listWidget = QtWidgets.QListWidget(self.formLayoutWidget)
        self.listWidget.setObjectName("listWidget")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.listWidget)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)

        self.retranslateUi(lwo)
        QtCore.QMetaObject.connectSlotsByName(lwo)

    def retranslateUi(self, lwo):
        _translate = QtCore.QCoreApplication.translate
        lwo.setWindowTitle(_translate("lwo", "Шифратор"))
        self.label.setText(_translate("lwo", "статус"))
        self.pushButton.setText(_translate("lwo", "Найти файлы"))
