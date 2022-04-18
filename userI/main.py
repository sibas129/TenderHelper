import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QSplitter, QLabel, QLineEdit, QHBoxLayout, \
    QPushButton, QComboBox


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.predict = QPushButton("Создание нового предсказания", self.frame)
        self.predict.clicked.connect(lambda: self.go_to_main())
        font = QFont()
        font.setPointSize(15)
        self.predict.setFont(font)
        self.predict.resize(400, 40)
        self.predict.move(40, 40)

        self.comb = QComboBox(self.frame)
        font = QFont()
        font.setPointSize(15)
        self.comb.setFont(font)
        self.comb.resize(400, 40)
        self.comb.move(40, 160)

        self.open = QPushButton("Загрузить", self.frame)
        font = QFont()
        font.setPointSize(15)
        self.open.setFont(font)
        self.open.resize(200, 40)
        self.open.move(40, 205)

        self.clos = QPushButton("Удалить", self.frame)
        font = QFont()
        font.setPointSize(15)
        self.clos.setFont(font)
        self.clos.resize(200, 40)
        self.clos.move(240, 205)

        self.ad = QPushButton("Выход", self.frame)
        self.ad.clicked.connect(lambda: exit(0))
        font = QFont()
        font.setPointSize(15)
        self.ad.setFont(font)
        self.ad.resize(400, 40)
        self.ad.move(40, 265)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.frame)

        self.setLayout(hbox)
        self.close()

    def go_to_main(self):
        global main_window
        from userI import main_window
        ex = main_window.Ui_main_window()
        ex.setGeometry(1000, 1000, 1000, 600)
        ex.setWindowTitle('TenderHelper')
        ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
        self.close()
        ex.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    ex.setGeometry(1000, 1000, 1000, 600)
    ex.setFixedSize(500, 350)
    ex.setWindowTitle('TenderHelper')
    ex.move(QApplication.desktop().screen().rect().center() - ex.rect().center())
    ex.show()
    sys.exit(app.exec_())
