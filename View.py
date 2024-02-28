import time
from MainUi import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QLineEdit
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import pyqtSignal, QSignalMapper, pyqtSlot


class AppWindow(QMainWindow):
    def __init__(self, model):
        super(AppWindow, self).__init__()
        self.model = model
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.model.signals.stbar_msg.connect(self.status_bar_ui)
        self.model.signals.finish_read.connect(self.fill_ui)
        self.model.signals.flag_adr.connect(self.find_adr_ui)

        self.com_port()
        self.smap_line_edit()
        self.buttons()

    def smap_line_edit(self):
        smap = QSignalMapper(self)

        self.ui.diff_speed_wind.clicked.connect(smap.map)
        smap.setMapping(self.ui.diff_speed_wind, 1)

        self.ui.diff_humidity.clicked.connect(smap.map)
        smap.setMapping(self.ui.diff_humidity, 2)

        self.ui.diff_voltage.clicked.connect(smap.map)
        smap.setMapping(self.ui.diff_voltage, 3)

        smap.mapped.connect(self.on_click_koef)

    @pyqtSlot(int)
    def on_click_koef(self, index):
        self.stop_read_ui()
        self.model.stop_read()

    def closeEvent(self, event):
        self.model.exit_read()
        self.model.disconnect_client()
        self.close()

    def status_bar_ui(self, txt_bar):
        try:
            self.ui.statusBar.showMessage(txt_bar)

        except Exception as e:
            print(str(e))

    def com_port(self):
        try:
            for i in range(len(self.model.available_ports)):
                self.ui.com_port_cb.addItem(self.model.available_ports[i])

            self.model.settings['comport'] = self.ui.com_port_cb.currentText()

            self.ui.com_port_cb.activated[str].connect(self.select_comport)

        except Exception as e:
            txt_log = 'ERROR in view/com_port - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(txt_log)

    def select_comport(self, port):
        try:
            self.model.settings['comport'] = port

        except Exception as e:
            txt_log = 'ERROR in view/select_comport - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(txt_log)

    def find_adr_ui(self):
        try:
            adr_dev = str(self.model.settings['dev_id'])
            self.ui.adr_control_start.setText(adr_dev)
            self.ui.adr_control.setText(adr_dev)

        except Exception as e:
            txt_log = 'ERROR in view/find_adr_ui - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def fill_ui(self):
        try:
            self.ui.adr_control.setText(str(self.model.settings['dev_id']))
            self.ui.direct_wind_acp.setText(str(self.model.data_meteo['napr_veter_adc']))
            self.ui.direct_wind.setText(str(self.model.data_meteo['napr_veter_gr']))
            self.ui.direct_wind_avarage.setText(str(self.model.data_meteo['napr_veter_sr']))
            self.ui.speed_wind.setText(str(self.model.data_meteo['scor_veter_adc']))
            self.ui.humidity_counter.setText(str(self.model.data_meteo['himid_adc']))
            self.ui.speed_wind_metr.setText(str(self.model.data_meteo['adr_scor_veter']))
            self.ui.speed_wind_avarage.setText(str(self.model.data_meteo['scor_veter_sr']))
            self.ui.humidity.setText(str(self.model.data_meteo['himid']))
            self.ui.temp_ds18b20.setText(str(self.model.data_meteo['t_18b20']))
            self.ui.calc_humidity.setText(str(self.model.data_meteo['c_himid']))
            self.ui.voltage.setText(str(self.model.data_meteo['u_bat_d']))
            self.ui.diff_speed_wind.setText(str(self.model.data_meteo['k_scor_veter']))
            self.ui.diff_humidity.setText(str(self.model.data_meteo['cpar_himid']))
            self.ui.diff_voltage.setText(str(self.model.data_meteo['k_upit']))

        except Exception as e:
            txt_log = 'ERROR in view/fill_ui - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(txt_log)

    def buttons(self):
        self.ui.write_adr_btn.setEnabled(False)
        self.ui.find_addr_btn.setEnabled(False)
        self.ui.read_base_btn.setEnabled(False)
        self.ui.write_adr_btn.clicked.connect(self.write_adr)
        self.ui.connect_btn.clicked.connect(self.connect_base)
        self.ui.find_addr_btn.clicked.connect(self.model.find_adr_meteo)
        self.ui.read_base_btn.clicked.connect(self.read_base)

        self.ui.diff_speed_wind.returnPressed.connect(self.writeKoefWind)
        self.ui.diff_voltage.returnPressed.connect(self.writeKoefVolt)
        self.ui.diff_humidity.returnPressed.connect(self.writeKoefHumi)

    def connect_base(self):
        try:
            temp = self.ui.connect_btn.text()
            if temp == 'Подключиться':
                self.model.create_client()
                self.model.connect_client()
                if self.model.client:
                    self.connect_base_ui()
                    self.ui.adr_control_start.setText(str(self.model.settings['dev_id']))

            elif temp == 'Отключиться':
                self.model.disconnect_client()
                if not self.model.client:
                    self.disconnect_base_ui()

        except Exception as e:
            txt_log = 'ERROR in view/connect_base - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def connect_base_ui(self):
        self.ui.connect_btn.setText('Отключиться')
        self.ui.read_base_btn.setEnabled(True)
        self.ui.write_adr_btn.setEnabled(True)
        self.ui.find_addr_btn.setEnabled(True)

    def disconnect_base_ui(self):
        self.ui.connect_btn.setText('Подключиться')
        self.ui.read_base_btn.setEnabled(False)
        self.ui.write_adr_btn.setEnabled(False)
        self.ui.find_addr_btn.setEnabled(False)
        self.stop_read_ui()

    def start_read_ui(self):
        self.ui.read_base_btn.setText('Остановить')

    def stop_read_ui(self):
        self.ui.read_base_btn.setText('Читать')

    def read_base(self):
        try:
            temp = self.ui.read_base_btn.text()
            if temp == 'Читать':
                self.model.settings['dev_id'] = int(self.ui.adr_control_start.text())
                self.model.start_read()
                self.start_read_ui()

            elif temp == 'Остановить':
                self.model.stop_read()
                self.stop_read_ui()

        except Exception as e:
            txt_log = 'ERROR in view/read_base - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def write_adr(self):
        try:
            self.model.stop_read()
            self.stop_read_ui()
            self.model.unblock_write_base()
            arr = []
            arr.append(int(self.ui.adr_control_start.text()))
            self.model.settings['value'] = arr
            self.model.settings['start_adr'] = 0
            self.model.write_value()

            self.model.settings['dev_id'] = arr[0]
            self.model.block_write_base()
            self.find_adr_ui()

            self.model.start_read()
            self.start_read_ui()

        except Exception as e:
            txt_log = 'ERROR in view/write_adr - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def writeKoefWind(self):
        try:
            self.model.stop_read()
            self.stop_read_ui()
            value = float(self.ui.diff_speed_wind.text())
            start_adr = 4205
            self.write_koef(start_adr=start_adr, value=value)

        except Exception as e:
            txt_log = 'ERROR in view/write_koef_wind - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def writeKoefHumi(self):
        try:
            self.model.stop_read()
            self.stop_read_ui()
            value = float(self.ui.diff_humidity.text())
            start_adr = 4207
            self.write_koef(start_adr=start_adr, value=value)

        except Exception as e:
            txt_log = 'ERROR in view/write_koef_humi - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def writeKoefVolt(self):
        try:
            self.model.stop_read()
            self.stop_read_ui()
            value = float(self.ui.diff_voltage.text())
            start_adr = 4211
            self.write_koef(start_adr=start_adr, value=value)

        except Exception as e:
            txt_log = 'ERROR in view/write_koef_volt - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

    def write_koef(self, **kwargs):
        try:
            value = kwargs.get('value')
            start_adr = kwargs.get('start_adr')
            self.model.floatToByte(start_adr, value)
            time.sleep(0.1)
            self.model.start_read()
            self.start_read_ui()

        except Exception as e:
            txt_log = 'ERROR in view/write_koef - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))

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
            self.ui.calc_humidity.clear()
            self.ui.voltage.clear()
            self.ui.diff_speed_wind.clear()
            self.ui.diff_humidity.clear()
            self.ui.diff_voltage.clear()

        except Exception as e:
            txt_log = 'ERROR in view/cleara_ui - {}'.format(e)
            self.status_bar_ui(txt_log)
            print(str(txt_log))
