# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Rectangle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Rectangle(object):
    def setupUi(self, Rectangle):
        Rectangle.setObjectName("Rectangle")
        Rectangle.resize(1100, 620)
        self.textEdit = QtWidgets.QTextEdit(Rectangle)
        self.textEdit.setGeometry(QtCore.QRect(130, 20, 500, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_b = QtWidgets.QLabel(Rectangle)
        self.label_b.setGeometry(QtCore.QRect(30, 20, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_b.setFont(font)
        self.label_b.setObjectName("label_b")
        self.textEdit_b = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_b.setGeometry(QtCore.QRect(20, 60, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_b.setFont(font)
        self.textEdit_b.setObjectName("textEdit_b")
        self.textEdit_h = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_h.setGeometry(QtCore.QRect(20, 140, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_h.setFont(font)
        self.textEdit_h.setObjectName("textEdit_h")
        self.label_h = QtWidgets.QLabel(Rectangle)
        self.label_h.setGeometry(QtCore.QRect(30, 100, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_h.setFont(font)
        self.label_h.setObjectName("label_h")
        self.label_M = QtWidgets.QLabel(Rectangle)
        self.label_M.setGeometry(QtCore.QRect(30, 260, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_M.setFont(font)
        self.label_M.setObjectName("label_M")
        self.textEdit_M = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_M.setGeometry(QtCore.QRect(20, 300, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_M.setFont(font)
        self.textEdit_M.setObjectName("textEdit_M")
        self.pushButton_Calculation = QtWidgets.QPushButton(Rectangle)
        self.pushButton_Calculation.setGeometry(QtCore.QRect(130, 550, 500, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Calculation.setFont(font)
        self.pushButton_Calculation.setObjectName("pushButton_Calculation")
        self.graphicsView = QtWidgets.QGraphicsView(Rectangle)
        self.graphicsView.setGeometry(QtCore.QRect(660, 20, 400, 500))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.graphicsView.setFont(font)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_Drawing = QtWidgets.QPushButton(Rectangle)
        self.pushButton_Drawing.setGeometry(QtCore.QRect(660, 550, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.pushButton_Drawing.setFont(font)
        self.pushButton_Drawing.setObjectName("pushButton_Drawing")
        self.label_a_s = QtWidgets.QLabel(Rectangle)
        self.label_a_s.setGeometry(QtCore.QRect(30, 180, 60, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_a_s.setFont(font)
        self.label_a_s.setObjectName("label_a_s")
        self.textEdit_a_s = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_a_s.setGeometry(QtCore.QRect(20, 220, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_a_s.setFont(font)
        self.textEdit_a_s.setObjectName("textEdit_a_s")
        self.textEdit_c = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_c.setGeometry(QtCore.QRect(20, 380, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_c.setFont(font)
        self.textEdit_c.setObjectName("textEdit_c")
        self.label_c = QtWidgets.QLabel(Rectangle)
        self.label_c.setGeometry(QtCore.QRect(20, 340, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_c.setFont(font)
        self.label_c.setObjectName("label_c")
        self.label_n = QtWidgets.QLabel(Rectangle)
        self.label_n.setGeometry(QtCore.QRect(20, 430, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_n.setFont(font)
        self.label_n.setObjectName("label_n")
        self.textEdit_n = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_n.setGeometry(QtCore.QRect(20, 470, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_n.setFont(font)
        self.textEdit_n.setObjectName("textEdit_n")
        self.textEdit_d = QtWidgets.QTextEdit(Rectangle)
        self.textEdit_d.setGeometry(QtCore.QRect(20, 550, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.textEdit_d.setFont(font)
        self.textEdit_d.setObjectName("textEdit_d")
        self.label_d = QtWidgets.QLabel(Rectangle)
        self.label_d.setGeometry(QtCore.QRect(20, 510, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.label_d.setFont(font)
        self.label_d.setObjectName("label_d")

        self.retranslateUi(Rectangle)
        QtCore.QMetaObject.connectSlotsByName(Rectangle)

    def retranslateUi(self, Rectangle):
        _translate = QtCore.QCoreApplication.translate
        Rectangle.setWindowTitle(_translate("Rectangle", "Form"))
        self.label_b.setText(_translate("Rectangle", "宽度"))
        self.label_h.setText(_translate("Rectangle", "高度"))
        self.label_M.setText(_translate("Rectangle", "弯矩"))
        self.pushButton_Calculation.setText(_translate("Rectangle", "开始计算（更新数据）"))
        self.pushButton_Drawing.setText(_translate("Rectangle", "开始配筋"))
        self.label_a_s.setText(_translate("Rectangle", "a_s"))
        self.label_c.setText(_translate("Rectangle", "保护层"))
        self.label_n.setText(_translate("Rectangle", "根数"))
        self.label_d.setText(_translate("Rectangle", "直径"))
