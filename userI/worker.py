import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from core import analyzer
from core.analyzer import result
import pandas as pd
import numpy as np
from sklearn import linear_model

from userI import main
from userI.main import Menu
from userI.save_dialog import DialogClass


class PredictionFrame(QWidget):
    def __init__(self):
        super().__init__()

        self.leftFrame = QFrame()
        self.leftFrame.setFrameShape(QFrame.StyledPanel)

        self.rightFrame = QFrame()
        self.rightFrame.setFrameShape(QFrame.StyledPanel)

        splitter2 = QSplitter(Qt.Horizontal)

        splitter2.addWidget(self.leftFrame)
        splitter2.addWidget(self.rightFrame)
        splitter2.setSizes([29, 15])

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)

        self.setLayout(hbox)
        self.crt()

    def crt(self):
        self.company_name = QLineEdit("", self.leftFrame)
        self.company_name.setReadOnly(True)
        self.company_name.setGeometry(20, 10, 380, 60)
        self.company_name.setFrame(False)
        font = QFont()
        font.setPointSize(22)
        self.company_name.setFont(font)

        self.add_btn = QPushButton("Добавить...", self.rightFrame)
        self.add_btn.setGeometry(QtCore.QRect(10, 160, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_btn.setFont(font)
        self.add_btn.clicked.connect(self.predict)

        self.lineEdit = QLineEdit(self.rightFrame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)

        self.lineEdit_2 = QLineEdit(self.rightFrame)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 60, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)

        self.lineEdit_3 = QLineEdit(self.rightFrame)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 110, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)

    def refactor(self, str):
        i = str.find(',')
        nstr1 = str[i + 1:]

        str_lst1 = nstr1.split(',')
        int_lst1 = [int(x) for x in str_lst1]
        return int_lst1

    def predict(self):
        self.company_name.clear()
        if not self.lineEdit.text() and not self.lineEdit_2.text() and not self.lineEdit_3.text():
            return
        if self.lineEdit.text():
            int_lst1 = self.refactor(self.lineEdit.text())
            self.company_name.setText(str(int_lst1[1]))

        if self.lineEdit_2.text():
            int_lst2 = self.refactor(self.lineEdit_2.text())

        if self.lineEdit_3.text():
            int_lst3 = self.refactor(self.lineEdit.text())

    


    # def save(self):
    #     if self.system.text():
    #         acts.system_name = self.system.text()
    #     dialog = DialogClass()
    #     dialog.setWindowTitle('сохранение')
    #     dialog.setFixedSize(250, 100)
    #     dialog.exec_()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.createMenus()
        self.area = PredictionFrame()
        self.setCentralWidget(self.area)

    def createMenus(self):
        self.sv = self.menuBar().addAction("&Сохранить", self.save)

        self.toMenu = self.menuBar().addAction("&Меню", self.menu)

        self.exit = self.menuBar().addAction("&Выход", self.close)

    def save(self):
        self.area.save()

    def menu(self):
        self.close()
        main.ex = Menu()
        main.ex.setGeometry(1000, 1000, 1100, 600)
        main.ex.setFixedSize(500, 450)
        main.ex.move(QApplication.desktop().screen().rect().center() - main.ex.rect().center())
        main.ex.setWindowTitle('TenderHelper')
        main.ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(300, 500, 650, 500)
    ex.setWindowTitle('TenderHelper')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    # ex.company_name.setText("HSE" + str(result(0)))
    ex.show()
    sys.exit(app.exec_())



