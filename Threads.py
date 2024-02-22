import time
from datetime import datetime
from struct import pack, unpack
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class Signals(QObject):
    find_result = pyqtSignal(int)
    find_log = pyqtSignal(str)
    find_error = pyqtSignal(str)
    read_result = pyqtSignal(str, list)
    read_error = pyqtSignal(str)
    read_log = pyqtSignal(str)
    write_adr = pyqtSignal(int)
    write_koef = pyqtSignal()
    write_error = pyqtSignal(object)
    write_log = pyqtSignal(str)


class FindAdr(QRunnable):
    signals = Signals()

    def __init__(self):
        super(FindAdr, self).__init__()
        self.find_cycle = True
        self.find_is_run = False

    @pyqtSlot()
    def run(self):
        while self.find_cycle:
            try:
                if not self.find_is_run:
                    time.sleep(0.1)
                else:
                    self.txt_log = 'Определение адреса контроллера..'
                    self.signals.find_log.emit(self.txt_log)
                    for i in range(1, 33):
                        rr = self.client.read_holding_registers(0, 1, slave=i)
                        if not rr.isError():
                            self.signals.find_result.emit(rr.registers[0])
                            self.txt_log = 'Адрес контроллера определён - {}'.format(i)
                            self.signals.find_log.emit(self.txt_log)
                            self.find_is_run = False
                            break

                        else:
                            self.txt_log = 'Определение адреса контроллера.. - {} не верен'.format(i)
                            self.signals.find_log.emit(self.txt_log)

            except Exception as e:
                self.signals.find_error.emit(str(e))

    def startThread(self, client):
        self.client = client
        self.find_is_run = True

    def stopThread(self):
        self.find_is_run = False

    def exitThread(self):
        self.find_cycle = False


class Reader(QRunnable):
    signals = Signals()

    def __init__(self):
        super(Reader, self).__init__()
        self.cycle = True
        self.is_run = False
        self.read_koef = True
        self.tag = 'without_koef'

    @pyqtSlot()
    def run(self):
        while self.cycle:
            try:
                if not self.is_run:
                    time.sleep(0.01)
                else:
                    temp_list = []
                    rr = self.client.read_holding_registers(4192, 5, slave=self.dev_id)
                    if not rr.isError():
                        for i in range(5):
                            temp_list.append(rr.registers[i])

                    else:
                        self.signals.read_error.emit(str(rr))

                    rr = self.client.read_holding_registers(4197, 8, slave=self.dev_id)
                    if not rr.isError():
                        for i in range(0, 8, 2):
                            temp_u = unpack('f', pack('<HH', rr.registers[i + 1], rr.registers[i]))[0]
                            temp_list.append(temp_u)

                    else:
                        self.signals.read_error.emit(str(rr))

                    rr = self.client.read_holding_registers(4209, 2, slave=self.dev_id)
                    if not rr.isError():
                        temp_u = unpack('f', pack('<HH', rr.registers[1], rr.registers[0]))[0]
                        temp_list.append(temp_u)

                    else:
                        self.signals.read_error.emit(str(rr))

                    rr = self.client.read_holding_registers(4213, 2, slave=self.dev_id)
                    if not rr.isError():
                        temp_u = unpack('f', pack('<HH', rr.registers[1], rr.registers[0]))[0]
                        temp_list.append(temp_u)

                    else:
                        self.signals.read_error.emit(str(rr))
                    self.tag = 'without_koef'

                    if self.read_koef:
                        rr = self.client.read_holding_registers(4205, 4, slave=self.dev_id)
                        if not rr.isError():
                            temp_u = unpack('f', pack('<HH', rr.registers[1], rr.registers[0]))[0]
                            temp_list.append(temp_u)
                            temp_u = unpack('f', pack('<HH', rr.registers[3], rr.registers[2]))[0]
                            temp_list.append(temp_u)

                        else:
                            self.signals.read_error.emit(str(rr))

                        rr = self.client.read_holding_registers(4211, 2, slave=self.dev_id)
                        if not rr.isError():
                            temp_u = unpack('f', pack('<HH', rr.registers[1], rr.registers[0]))[0]
                            temp_list.append(temp_u)
                            self.read_koef = False
                            self.tag = 'with_koef'

                        else:
                            self.signals.read_error.emit(str(rr))

                    self.signals.read_result.emit(self.tag, temp_list)
                    txt_log = 'Данные получены ' + str(datetime.now())[:-3]
                    self.signals.read_log.emit(txt_log)
                    time.sleep(0.5)

            except Exception as e:
                self.signals.read_error.emit(str(e))

    def startThread(self, client, dev_id, read_koef):
        self.client = client
        self.dev_id = dev_id
        self.read_koef = read_koef
        self.is_run = True

    def stopThread(self):
        self.is_run = False

    def exitThread(self):
        self.cycle = False


class Writer(QRunnable):
    signals = Signals()

    def __init__(self):
        super(Writer, self).__init__()
        self.cycle = True
        self.is_run = False
        self.num_attempts = 0
        self.max_attempts = 4
        self.flag_write = False

    @pyqtSlot()
    def run(self):
        while self.cycle:
            try:
                if not self.is_run:
                    time.sleep(0.01)
                else:
                    rq = self.client.write_registers(2, 5046, slave=self.dev_id)
                    if self.tag == 'adr':
                        rq = self.client.write_registers(self.start_adr, self.values[0], slave=self.dev_id)
                        time.sleep(0.1)
                        txt_log = 'Адрес контроллера - {}'.format(self.values[0])
                        self.signals.write_log.emit(txt_log)
                        self.signals.write_adr.emit(self.values[0])

                    if self.tag == 'koef':
                        rq = self.client.write_registers(self.start_adr, self.values, slave=self.dev_id)
                        time.sleep(0.1)
                        txt_log = 'Коэффициент записан'
                        self.signals.write_log.emit(txt_log)
                        self.signals.write_koef.emit()
                    rq = self.client.write_registers(2, 65535, unit=self.dev_id)
                    self.is_run = False

            except Exception as e:
                self.signals.write_error.emit(str(e))

    def startThread(self, client, tag, start_adr, values, dev_id):
        self.tag = tag
        self.client = client
        self.dev_id = dev_id
        self.start_adr = start_adr
        self.values = values
        self.is_run = True

    def stopThread(self):
        self.is_run = False

    def exitThread(self):
        self.cycle = False

