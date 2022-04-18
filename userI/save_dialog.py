from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_save_dialog(object):
    def setupUi(self, save_dialog):
        save_dialog.setObjectName("save_dialog")
        save_dialog.resize(400, 170)
        self.frame = QtWidgets.QWidget(save_dialog)
        self.frame.setObjectName("frame")
        self.name = QtWidgets.QLineEdit(self.frame)
        self.name.setGeometry(QtCore.QRect(10, 30, 380, 40))
        self.name.setObjectName("name")
        self.ok_btn = QtWidgets.QPushButton(self.frame)
        self.ok_btn.setGeometry(QtCore.QRect(10, 90, 185, 40))
        self.ok_btn.setObjectName("ok_btn")
        self.close_btn = QtWidgets.QPushButton(self.frame)
        self.close_btn.setGeometry(QtCore.QRect(205, 90, 185, 40))
        self.close_btn.setObjectName("close_btn")
        save_dialog.setCentralWidget(self.frame)
        self.statusbar = QtWidgets.QStatusBar(save_dialog)
        self.statusbar.setObjectName("statusbar")
        save_dialog.setStatusBar(self.statusbar)

        self.retranslateUi(save_dialog)
        QtCore.QMetaObject.connectSlotsByName(save_dialog)

    def retranslateUi(self, save_dialog):
        _translate = QtCore.QCoreApplication.translate
        save_dialog.setWindowTitle(_translate("save_dialog", "Сохранение"))
        self.name.setText(_translate("save_dialog", "введите название сохранения"))
        self.ok_btn.setText(_translate("save_dialog", "Сохранить"))
        self.close_btn.setText(_translate("save_dialog", "Закрыть"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     save_dialog = QtWidgets.QMainWindow()
#     ui = Ui_save_dialog()
#     ui.setupUi(save_dialog)
#     save_dialog.show()
#     sys.exit(app.exec_())
