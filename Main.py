import sys
from Model import Model
from View import AppWindow
from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    m = Model()
    win = AppWindow(m)
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
