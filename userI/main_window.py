import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMenu, QMainWindow, QApplication, QFrame
from core import analyzer
from core.analyzer import result
import pandas as pd
import numpy as np
from sklearn import linear_model


class Ui_main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.answer = QtWidgets.QFrame(self)
        self.answer.setGeometry(QtCore.QRect(9, 9, 401, 351))
        self.answer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.answer.setFrameShadow(QtWidgets.QFrame.Raised)

        self.company_name = QtWidgets.QLabel(self.answer)
        self.company_name.setGeometry(QtCore.QRect(20, 10, 380, 60))
        self.company_name.setText("")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.company_name.setFont(font)

        self.companies = QtWidgets.QFrame(self)
        self.companies.setGeometry(QtCore.QRect(420, 10, 230, 351))
        self.companies.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.companies.setFrameShadow(QtWidgets.QFrame.Raised)

        self.add_btn = QtWidgets.QPushButton(self.companies)
        self.add_btn.setGeometry(QtCore.QRect(10, 160, 210, 40))
        self.add_btn.setText("Добавить...")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_btn.setFont(font)

        self.lineEdit = QtWidgets.QLineEdit(self.companies)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.companies)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.companies)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 210, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_main_window()
    ex.setGeometry(300, 500, 650, 500)
    ex.setWindowTitle('TenderHelper')
    ex.company_name.setText("HSE" + str(result(0)))
    ex.show()
    sys.exit(app.exec_())



