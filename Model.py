import serial.tools.list_ports
import time
from struct import pack
from PyQt5.QtCore import QObject, QThreadPool, pyqtSignal
from pymodbus.client import ModbusSerialClient as ModbusClient
from Threads import FindAdr, Reader, Writer


class WindowSignals(QObject):
    stbar_msg = pyqtSignal(str)
    flag_adr = pyqtSignal()
    finish_read = pyqtSignal()

    startRead = pyqtSignal(object, int)
    stopRead = pyqtSignal()
    exitRead = pyqtSignal()


class Model:
    def __init__(self):

        self.settings = {
            'comport': 'COM1',
            'dev_id': 1,
            'start_reg': 0,
            'value': [],
            'client': None,
        }

        self.data_meteo = {
            'napr_veter_adc': 0,
            'napr_veter_gr': 0,
            'napr_veter_sr': 0,
            'scor_veter_adc': 0,
            'himid_adc': 0,
            'adr_scor_veter': 0,
            'scor_veter_sr': 0,
            'himid': 0,
            't_18b20': 0,
            'k_scor_veter': 0,
            'cpar_himid': 0,
            'c_himid': 0,
            'k_upit': 0,
            'u_bat_d': 0,
        }

        self.client = None
        self.reader = None
        self.writer = None
        self.flag_init_write = False
        self.find_adr = None
        self.flag_init_adr = False

        self.signals = WindowSignals()
        self.threadpool = QThreadPool()

        self.available_ports = self.port_scan()

        self.init_reader()

    def status_bar_msg(self, text_bar):
        self.signals.stbar_msg.emit(text_bar)

    def port_scan(self):
        try:
            result = []
            ports = serial.tools.list_ports.comports()
            for port in ports:
                result.append(port.device)

            return result

        except Exception as e:
            print(str(e))

    def create_client(self):
        try:
            comport = self.settings.get('comport')
            self.client = ModbusClient(method='rtu', port=comport,
                                       parity='N', baudrate=57600, startbit=1,
                                       databits=8, stopbits=1, strict=False)

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))

    def connect_client(self):
        self.client.connect()
        txt_bar = 'Подключение к контроллеру'
        self.status_bar_msg(txt_bar)
        if self.client.connect:
            txt_bar = 'Контроллер подключен'
            self.settings['client'] = self.client
        else:
            txt_bar = 'Подключение не удалось'
        self.status_bar_msg(txt_bar)

    def disconnect_client(self):
        if self.client:
            self.stop_read()
            self.client.close()
            txt_bar = 'Контроллер отключен'
            self.status_bar_msg(txt_bar)
            self.client = None
            self.settings['client'] = None

    def thread_log(self, txt):
        self.status_bar_msg(txt)
        print(txt)

    def init_reader(self):
        try:
            self.reader = Reader()
            self.reader.signals.read_result.connect(self.read_result)
            self.reader.signals.thread_log.connect(self.thread_log)
            self.signals.startRead.connect(self.reader.startThread)
            self.signals.stopRead.connect(self.reader.stopThread)
            self.signals.exitRead.connect(self.reader.exitThread)
            self.threadpool.start(self.reader)

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))

    def start_read(self):
        client = self.settings.get('client')
        dev_id = self.settings.get('dev_id')
        self.signals.startRead.emit(client, dev_id)

    def stop_read(self):
        self.signals.stopRead.emit()
        txt_log = 'Чтение контроллера остановлено'
        self.status_bar_msg(txt_log)

    def exit_read(self):
        self.signals.exitRead.emit()

    def read_result(self, data):
        try:
            self.data_meteo = data
            self.signals.finish_read.emit()

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))

    def write_value(self):
        client = self.settings.get('client')
        start_adr = self.settings.get('start_adr')
        value = self.settings.get('value')
        dev_id = self.settings.get('dev_id')
        self.writer = Writer(client=client,
                             start_adr=start_adr,
                             value=value,
                             dev_id=dev_id)
        if not self.flag_init_write:
            self.writer.signal.thread_log.connect(self.thread_log)
            self.flag_init_write = True
        self.threadpool.start(self.writer)

    def unblock_write_base(self):
        try:
            self.settings['start_adr'] = 0x0002
            self.settings['value'] = [5046]
            self.write_value()
            time.sleep(0.1)

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))

    def block_write_base(self):
        try:
            self.settings['start_adr'] = 0x0002
            self.settings['value'] = [1000]
            self.write_value()
            time.sleep(0.1)

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))

    def find_adr_meteo(self):
        self.stop_read()
        client = self.settings.get('client')
        self.find_adr = FindAdr(client=client)
        if not self.flag_init_adr:
            self.find_adr.signals.thread_log.connect(self.thread_log)
            self.find_adr.signals.find_result.connect(self.find_adr_result)
            self.flag_init_adr = True
        self.threadpool.start(self.find_adr)

    def find_adr_result(self, data):
        self.settings['dev_id'] = data
        self.signals.flag_adr.emit()

    def floatToByte(self, start_adr, value):
        try:
            val_d = float(value)
            val_regs = []
            b = pack('>f', val_d)
            byt = []
            byt.append(b[0])
            byt.append(b[1])
            val_d = int.from_bytes(byt, 'big', signed=False)
            val_regs.append(val_d)
            byt = []
            byt.append(b[2])
            byt.append(b[3])
            val_d = int.from_bytes(byt, 'big', signed=False)
            val_regs.append(val_d)

            self.unblock_write_base()

            self.settings['start_adr'] = start_adr
            self.settings['value'] = val_regs

            self.write_value()

            self.block_write_base()

        except Exception as e:
            self.status_bar_msg(str(e))
            print(str(e))
