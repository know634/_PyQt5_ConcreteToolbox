# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tshape.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tshape(object):
    def setupUi(self, Tshape):
        Tshape.setObjectName("Tshape")
        Tshape.resize(400, 400)
        self.textEdit = QtWidgets.QTextEdit(Tshape)
        self.textEdit.setGeometry(QtCore.QRect(90, 90, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Tshape)
        QtCore.QMetaObject.connectSlotsByName(Tshape)

    def retranslateUi(self, Tshape):
        _translate = QtCore.QCoreApplication.translate
        Tshape.setWindowTitle(_translate("Tshape", "Form"))

