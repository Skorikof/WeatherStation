import sys
from Model import Model
from Controller import Controller
from View import AppWindow
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    m = Model()
    c = Controller(m)
    win = AppWindow(m, c)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()