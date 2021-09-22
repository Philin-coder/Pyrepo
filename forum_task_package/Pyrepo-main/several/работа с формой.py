import random
import string
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Example(QMainWindow, gui.Ui_MainWindow):  # file with form with you sldo need to import
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.buttonClicked)

    def generate_pins(self, size=6, chars=string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def buttonClicked(self):
        self.textEdit.append(self.generate_pins(10))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
app.exec()
