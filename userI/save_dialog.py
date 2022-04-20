from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLineEdit


class DialogClass(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.name = QLineEdit("", self)
        self.name.move(20, 10)
        font = QFont()
        font.setPointSize(8)
        self.name.setPlaceholderText("Введите название сохранения")
        self.name.resize(210, 20)
        self.name.setFont(font)

        self.textbox_errors = QLineEdit("", self)
        self.textbox_errors.setReadOnly(True)
        self.textbox_errors.move(20, 40)
        self.textbox_errors.setFrame(False)
        font = QFont()
        font.setPointSize(10)
        self.textbox_errors.setFont(font)
        self.textbox_errors.setMinimumSize(15, 15)
        self.textbox_errors.setMaximumSize(300, 20)
        self.textbox_errors.resize(300, 20)

        self.ok_btn = QtWidgets.QPushButton(self)
        #self.ok_btn.clicked.connect(self.save)
        self.ok_btn.move(20, 70)
        self.close_btn = QtWidgets.QPushButton(self)
        self.close_btn.clicked.connect(self.close)
        self.close_btn.move(155, 70)
        self.ok_btn.setText("Сохранить")
        self.close_btn.setText("Закрыть")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    save_dialog = QtWidgets.QMainWindow()
    ui = DialogClass()
    ui.setupUi(save_dialog)
    save_dialog.show()
    sys.exit(app.exec_())
