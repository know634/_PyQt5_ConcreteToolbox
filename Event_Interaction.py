# -- coding: utf-8 --
import os
# 导入PyQt5模块
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QMainWindow, QGraphicsScene
from PyQt5.QtGui import QColor, QPixmap
# 导入sys模块
import sys
# 导入UI模块
import Main
import Rectangle
import Tshape
# 导入其他模块
import pandas as pd
import math
import matplotlib.pyplot as plt

Parameters_ls = []

# 创建一个类，继承自QMainWindow
class MainWindow(QMainWindow, Main.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Parameters.clicked.connect(self.Parameters)
        self.pushButton_Rectangle.clicked.connect(self.Rectangle)
        self.pushButton_Tshape.clicked.connect(self.Tshape)
        self.pushButton_Specification.clicked.connect(self.Specification)

    def Parameters(self):
        Parameters_ls.clear()
        # 安全等级系数
        self.textEdit_Security.setTextColor(QColor(255, 0, 0))
        if self.comboBox_Security.currentText() == '安全等级一级':
            self.textEdit_Security.setText('一级：γ_0=1.1')
            self.gamma_0 = 1.1
        elif self.comboBox_Security.currentText() == '安全等级二级':
            self.textEdit_Security.setText('二级：γ_0=1.0')
            self.gamma_0 = 1.0
        elif self.comboBox_Security.currentText() == '安全等级三级':
            self.textEdit_Security.setText('三级：γ_0=0.9')
            self.gamma_0 = 0.9

        self.textEdit_Parameters.clear()

        self.textEdit_Parameters.setTextColor(QColor(255, 0, 0))
        self.textEdit_Parameters.append('{}、{}'.format(self.comboBox_Rebar.currentText(), self.comboBox_Concrete.currentText()))
        self.textEdit_Parameters.setTextColor(QColor(0, 0, 0))
        # f_y
        sheet_f_y = pd.read_excel(os.path.dirname(__file__) + '\\Specification\\Appendix.xlsx', sheet_name='普通钢筋强度设计值', header=0, index_col=0)
        self.f_y = sheet_f_y.loc[self.comboBox_Rebar.currentText(), '抗拉强度设计值']
        self.textEdit_Parameters.append('f_y= ' + str(self.f_y) + ' N/mm^2')
        # f_c和f_t
        sheet_f_c_t = pd.read_excel(os.path.dirname(__file__) + '\\Specification\\Appendix.xlsx', sheet_name='混凝土强度设计值', header=0, index_col=0)
        self.f_c = sheet_f_c_t.loc['f_c', self.comboBox_Concrete.currentText()]
        self.f_t = sheet_f_c_t.loc['f_t', self.comboBox_Concrete.currentText()]
        self.textEdit_Parameters.append('f_c= ' + str(self.f_c) + ' N/mm^2')
        self.textEdit_Parameters.append('f_t= ' + str(self.f_t) + ' N/mm^2')
        # α_1和β_1和ξ_b
        sheet_alpha_1_beta_1 = pd.read_excel(os.path.dirname(__file__) + '\\Specification\\Appendix.xlsx', sheet_name='混凝土受压区等效矩形应力图形系数', header=0, index_col=0)
        self.alpha_1 = sheet_alpha_1_beta_1.loc['α1', self.comboBox_Concrete.currentText()]
        self.beta_1 = sheet_alpha_1_beta_1.loc['β1', self.comboBox_Concrete.currentText()]
        self.textEdit_Parameters.append('α_1= ' + str(self.alpha_1))
        self.textEdit_Parameters.append('β_1= ' + str(self.beta_1))
        sheet_xi_b = pd.read_excel(os.path.dirname(__file__) + '\\Specification\\Appendix.xlsx', sheet_name='有屈服点钢筋的ξb值', header=0, index_col=0)
        self.xi_b = sheet_xi_b.loc[self.comboBox_Rebar.currentText(), self.comboBox_Concrete.currentText()]
        self.textEdit_Parameters.append('ξ_b= ' + str(self.xi_b))

        Parameters_ls.append(self.gamma_0)
        Parameters_ls.append(self.f_y)
        Parameters_ls.append(self.f_c)
        Parameters_ls.append(self.f_t)
        Parameters_ls.append(self.alpha_1)
        Parameters_ls.append(self.beta_1)
        Parameters_ls.append(self.xi_b)

    def Rectangle(self):
        self.RectangleWindow = RectangleWindow()
        self.RectangleWindow.show()

    def Tshape(self):
        self.TshapeWindow = TshapeWindow()
        self.TshapeWindow.show()

    def Specification(self):
        os.system(f'start {os.path.dirname(__file__)}\\Specification\\GB_50010_2010.pdf')

# 创建子类，继承自QWidget
class RectangleWindow(QWidget, Rectangle.Ui_Rectangle):
    def __init__(self, parent=None):
        super(RectangleWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_Calculation.clicked.connect(self.Calculation)
        self.pushButton_Drawing.clicked.connect(self.Drawing)

        self.textEdit_b.setText('250')
        self.textEdit_h.setText('600')
        self.textEdit_a_s.setText('40')
        self.textEdit_M.setText('240')
        self.textEdit_c.setText('20')

    def Calculation(self):
        self.textEdit.clear()
        try:
            self.gamma_0 = (Parameters_ls[0])
            self.f_y = (Parameters_ls[1])
            self.f_c = (Parameters_ls[2])
            self.f_t = (Parameters_ls[3])
            self.alpha_1 = (Parameters_ls[4])
            self.beta_1 = (Parameters_ls[5])
            self.xi_b = (Parameters_ls[6])
        except:
            self.textEdit.setText('请先在主界面“确定参数”')
            self.box0 = QMessageBox(QMessageBox.Warning, '警告', '请先在主界面“确定参数”')
            self.box0.setStandardButtons(QMessageBox.Ok)
            self.box0.button(QMessageBox.Ok).setText('确定')
            self.box0.exec_()
        try:
            self.b = float(self.textEdit_b.toPlainText())
            self.h = float(self.textEdit_h.toPlainText())
            self.a_s = float(self.textEdit_a_s.toPlainText())
            self.M = float(self.textEdit_M.toPlainText())
        except:
            self.textEdit.setText('请输入正确的宽度、高度、a_s、弯矩和保护层厚度')
            self.box1 = QMessageBox(QMessageBox.Warning, '警告', '请输入正确的宽度、高度、a_s、弯矩和保护层厚度')
            self.box1.setStandardButtons(QMessageBox.Ok)
            self.box1.button(QMessageBox.Ok).setText('确定')
            self.box1.exec_()

        rho_min = max(0.45*self.f_t/self.f_y, 0.002)
        self.textEdit.append('ρ_min = {:.5f}'.format(rho_min))

        h_0 = self.h - self.a_s
        self.textEdit.append('h_0 = ' + str(h_0))

        alpha_s = self.gamma_0 * self.M * 1e6 /(self.alpha_1*self.f_c*self.b*h_0**2)
        self.textEdit.append('α_s = {:.3f}'.format(alpha_s))
        try:
            xi = 1 - (1 - 2 * alpha_s)**0.5
        except:
            self.textEdit.append('α_s > 0.5，ξ无解')
            self.box2 = QMessageBox(QMessageBox.Warning, '警告', 'α_s > 0.5，ξ无解')
            self.box2.setStandardButtons(QMessageBox.Ok)
            self.box2.button(QMessageBox.Ok).setText('确定')
            self.box2.exec_()

        if xi > self.xi_b:
            self.textEdit.append('ξ={:.3f}>ξ_b={}，不满足适筋梁的条件，请重新设计。'.format(xi, self.xi_b))
            self.box3 = QMessageBox(QMessageBox.Warning, '警告', 'ξ={:3f}>ξ_b={}，不满足适筋梁的条件，请重新设计。'.format(xi, self.xi_b))
            self.box3.setStandardButtons(QMessageBox.Ok)
            self.box3.button(QMessageBox.Ok).setText('确定')
            self.box3.exec_()
        else:
            self.textEdit.append('ξ={:.3f}<ξ_b={}，满足适筋梁的条件。'.format(xi, self.xi_b))

        A_s = self.alpha_1*self.f_c*self.b*h_0*xi/(self.f_y)
        self.textEdit.append('\nA_s= {:.3f}mm^2'.format(A_s))

        sheet_A_s = pd.read_excel(os.path.dirname(__file__) + '\\Specification\\Appendix.xlsx', sheet_name='钢筋的公称直径、公称截面面积及理论重量', header=0, index_col=0)
        tmp1 = sheet_A_s.iloc[:, 0:9] - A_s
        tmp2 = tmp1[tmp1 > 0].idxmin(axis=0)
        tmp3 = tmp1[tmp1 > 0].min(axis=0)
        tmp4 = pd.concat([tmp2, tmp3], axis=1)
        tmp5 = tmp4.sort_values(by=[1, 0], ascending=[True, False])
        self.number = tmp5.index[0]
        diameter = tmp5.iloc[0, 0]
        positive_difference = tmp5.iloc[0, 1]
        self.textEdit.setTextColor(QColor(255, 0, 0))
        self.textEdit.append('\n查表，欲使差值最小应选{}根直径为{}mm钢筋，且实配钢筋面积为A_s_real={:.3f}mm^2，正差值为{:.3f}mm^2，单根钢筋每米理论重量为{}kg。'.format(self.number, diameter, A_s + positive_difference, positive_difference, sheet_A_s['单根钢筋每米理论重量'][diameter]))
        self.textEdit.setTextColor(QColor(0, 0, 0))

        A_s_min = rho_min*self.b*h_0
        self.textEdit.append('\nA_s_min = {:.3f}mm^2'.format(A_s_min))
        if A_s > A_s_min:
            self.textEdit.append('A_s > A_s_min，满足最小钢筋量要求。\n')
        else:
            self.textEdit.append('A_s < A_s_min，不满足最小钢筋量要求。\n')
        self.textEdit_n.setTextColor(QColor(255, 0, 0))
        self.textEdit_n.setText(str(self.number))
        self.textEdit_d.setTextColor(QColor(255, 0, 0))
        self.textEdit_d.setText(str(diameter))

    def Drawing(self):
        plt.figure(figsize=(4, 5))
        # 解决中文显示问题
        plt.rcParams['font.sans-serif'] = ['SimSun']
        plt.rcParams['axes.unicode_minus'] = False
        # 限制坐标轴范围
        h = eval(self.textEdit_h.toPlainText())
        b = eval(self.textEdit_b.toPlainText())
        plt.xlim(0, b)
        plt.ylim(0, h)
        # 绘制保护层
        c = float(self.textEdit_c.toPlainText())
        plt.plot([c, c], [c, h-c], color='black', linewidth=2)
        plt.plot([b-c, b-c], [c, h-c], color='black', linewidth=2)
        plt.plot([c, b-c], [c, c], color='black', linewidth=2)
        plt.plot([c, b-c], [h-c, h-c], color='black', linewidth=2)
        # 让坐标刻度不显示
        plt.xticks([])
        plt.yticks([])
        # 显示坐标轴标签
        plt.xlabel('b = {}mm'.format(b), fontsize=16)
        plt.ylabel('h = {}mm'.format(h), fontsize=16)
        # 把坐标轴字体设置为Times New Roman
        plt.rcParams['font.sans-serif'] = ['Times New Roman']
        plt.rcParams['axes.unicode_minus'] = False

        # 绘制钢筋
        n = eval(self.textEdit_n.toPlainText())
        D = eval(self.textEdit_d.toPlainText())
        d = (b-2*c)/(n-1)
        X = [c+i*d for i in range(n)]
        Y = [self.a_s for _ in range(n)]

        self.textEdit.setTextColor(QColor(255, 0, 0))
        self.textEdit.append('Info：输入的实配钢筋面积为{:.3f}mm^2。'.format(n * math.pi * D**2 / 4))
        self.textEdit.setTextColor(QColor(0, 0, 0))

        plt.scatter(X, Y, s=60, marker='o', color='red')
        plt.savefig(os.path.dirname(__file__) + '\\temp.jpg', bbox_inches='tight')
        # 点的标签
        plt.savefig(os.path.dirname(__file__) + '\\temp（坐标）.jpg', dpi=1200, bbox_inches='tight')

        self.scene = QGraphicsScene()
        self.scene.clear()
        self.scene.addPixmap(QPixmap(os.path.dirname(__file__) + '\\temp.jpg'))
        self.graphicsView.setScene(self.scene)


class TshapeWindow(QWidget, Tshape.Ui_Tshape):
    def __init__(self, parent=None):
        super(TshapeWindow, self).__init__(parent)
        self.setupUi(self)
        self.textEdit.setText('我是计算T形截面的程序界面')

# 创建一个窗口实例
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()
    sys.exit(app.exec_())