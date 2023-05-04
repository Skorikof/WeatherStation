import time
from MainUi import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow


class AppWindow(QMainWindow):
    def __init__(self, model):
        super(AppWindow, self).__init__()
        self.model = model
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model.signals.stbar_msg.connect(self.StatusBarMsg)
        self.model.signals.finish_read.connect(self.fillUi)
        self.model.signals.flag_adr.connect(self.selectAdr)

        self.com_port()

        self.buttons()

        self.ui.diff_speed_wind.returnPressed.connect(self.writeKoefWind)
        self.ui.diff_voltage.returnPressed.connect(self.writeKoefVolt)
        self.ui.diff_humidity.returnPressed.connect(self.writeKoefHumi)
        self.ui.diff_voltage.selectionChanged.connect(self.printSignal)

    def closeEvent(self, event):
        self.model.exitFind()
        self.model.exitRead()
        self.model.exitWriter()
        self.close()

    def com_port(self):
        try:
            for i in range(len(self.model.available_ports)):
                self.ui.com_port_cb.addItem(self.model.available_ports[i])

            self.model.com_port = self.ui.com_port_cb.currentText()

            self.ui.com_port_cb.activated[str].connect(self.select_port)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def select_port(self, port):
        try:
            self.model.com_port = port

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def buttons(self):
        self.ui.write_adr_btn.setEnabled(False)
        self.ui.find_addr_btn.setEnabled(False)
        self.ui.read_base_btn.setEnabled(False)
        self.ui.write_adr_btn.clicked.connect(self.writeAdr)
        self.ui.connect_btn.clicked.connect(self.connectBase)
        self.ui.find_addr_btn.clicked.connect(self.model.startFind)
        self.ui.read_base_btn.clicked.connect(self.readBase)

    def StatusBarMsg(self, txt_bar):
        try:
            self.ui.statusBar.showMessage(txt_bar)

        except Exception as e:
            print(str(e))

    def connectBase(self):
        try:
            temp = self.ui.connect_btn.text()
            if temp == 'Подключиться':
                self.model.initClient()
                self.ui.connect_btn.setText('Отключиться')

            elif temp == 'Отключиться':
                self.model.stopClient()
                self.ui.connect_btn.setText('Подключиться')

            if self.model.flag_connect:
                self.ui.adr_control_start.setText(str(self.model.struct.adr_dev))
                self.ui.write_adr_btn.setEnabled(True)
                self.ui.find_addr_btn.setEnabled(True)
                self.ui.read_base_btn.setEnabled(True)

            elif not self.model.flag_connect:
                self.clearUi()
                self.ui.write_adr_btn.setEnabled(False)
                self.ui.find_addr_btn.setEnabled(False)
                self.ui.read_base_btn.setEnabled(False)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def readBase(self):
        try:
            temp = self.ui.read_base_btn.text()
            if temp == 'Читать':
                self.model.struct.adr_dev = int(self.ui.adr_control_start.text())
                self.model.startRead()
                self.ui.read_base_btn.setText('Остановить')

            elif temp == 'Остановить':
                self.model.stopRead()
                self.ui.read_base_btn.setText('Читать')

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def fillUi(self):
        try:
            self.ui.adr_control.setText(str(self.model.struct.adr_dev))
            self.ui.direct_wind_acp.setText(str(self.model.struct.napr_veter_adc))
            self.ui.direct_wind.setText(str(self.model.struct.napr_veter_gr))
            self.ui.direct_wind_avarage.setText(str(self.model.struct.napr_veter_sr))
            self.ui.speed_wind.setText(str(self.model.struct.scor_veter_adc))
            self.ui.humidity_counter.setText(str(self.model.struct.himid_adc))
            self.ui.speed_wind_metr.setText(str(self.model.struct.adr_scor_veter))
            self.ui.speed_wind_avarage.setText(str(self.model.struct.scor_veter_sr))
            self.ui.humidity.setText(str(self.model.struct.himid))
            self.ui.temp_ds18b20.setText(str(self.model.struct.t_18b20))
            self.ui.diff_speed_wind.setText(str(self.model.struct.k_scor_veter))
            self.ui.diff_humidity.setText(str(self.model.struct.cpar_himid))
            self.ui.calc_humidity.setText(str(self.model.struct.c_himid))
            self.ui.diff_voltage.setText(str(self.model.struct.k_upit))
            self.ui.voltage.setText(str(self.model.struct.u_bat_d))

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def writeAdr(self):
        try:
            arr = []
            arr.append(int(self.ui.adr_control_start.text()))
            start_adr = 0
            self.model.startWriter('adr', start_adr, arr, self.model.struct.adr_dev)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def selectAdr(self):
        try:
            self.ui.adr_control_start.setText(str(self.model.struct.adr_dev))

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def writeKoefWind(self):
        try:
            value = float(self.ui.diff_speed_wind.text())
            start_adr = 4205
            self.model.floatToByte(start_adr, value, self.model.struct.adr_dev)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def writeKoefHumi(self):
        try:
            value = float(self.ui.diff_humidity.text())
            start_adr = 4207
            self.model.floatToByte(start_adr, value, self.model.struct.adr_dev)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def writeKoefVolt(self):
        try:
            value = float(self.ui.diff_voltage.text())
            start_adr = 4211
            self.model.floatToByte(start_adr, value, self.model.struct.adr_dev)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def clearUi(self):
        try:
            self.ui.adr_control_start.clear()
            self.ui.adr_control.clear()
            self.ui.direct_wind_acp.clear()
            self.ui.direct_wind.clear()
            self.ui.direct_wind_avarage.clear()
            self.ui.speed_wind.clear()
            self.ui.humidity_counter.clear()
            self.ui.speed_wind_metr.clear()
            self.ui.speed_wind_avarage.clear()
            self.ui.humidity.clear()
            self.ui.temp_ds18b20.clear()
            self.ui.diff_speed_wind.clear()
            self.ui.diff_humidity.clear()
            self.ui.calc_humidity.clear()
            self.ui.diff_voltage.clear()
            self.ui.voltage.clear()

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def printSignal(self):
        self.model.stopRead()
        time.sleep(1)
        self.model.startRead()
