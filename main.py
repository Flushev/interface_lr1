from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from Lab1_v2 import Ui_MainWindow, MyWin
import sys


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())

