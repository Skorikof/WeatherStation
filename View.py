from MainUi import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class AppWindow(QMainWindow):
    def __init__(self, model, controller):
        super(AppWindow, self).__init__()
        self.model = model
        self.controller = controller
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.com_port()

        self.buttons()


    def closeEvent(self, event):
        self.model.exitThread()
        self.close()

    def com_port(self):
        try:
            for i in range(len(self.model.available_ports)):
                self.ui.com_port_cb.addItem(self.model.available_ports[i])

            self.ui.com_port_cb.activated[str].connect(self.connect_port)

        except Exception as e:
            print(str(e))

    def connect_port(self, port):
        self.model.initClient(port)

    def buttons(self):
        self.ui.find_addr_btn.clicked.connect(self.model.initFindAdr)
        self.ui.connect_btn.clicked.connect(self.model.startRead)


