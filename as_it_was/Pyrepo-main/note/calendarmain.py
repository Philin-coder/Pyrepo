import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from calendar import CalendarWindow


class MainScreen(QMainWindow):
    def __init__(self):
        super(MainScreen, self).__init__()
        self.ui = CalendarWindow()
        self.ui.setupUi(self)


app = QApplication(sys.argv)
myapp = MainScreen()
myapp.show()
sys.exit(app.exec_())
