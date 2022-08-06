import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.layoutH = QHBoxLayout()
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500
        self.title = "Absolute Return"
        self.setWindowTitle(self.title)
        self.InitUI()

    def InitUI(self):
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())