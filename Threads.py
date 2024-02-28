import time
from datetime import datetime
from struct import pack, unpack
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class Signals(QObject):
    thread_log = pyqtSignal(str)
    find_result = pyqtSignal(int)
    read_result = pyqtSignal(dict)


class FindAdr(QRunnable):
    signals = Signals()

    def __init__(self, **kwargs):
        super(FindAdr, self).__init__()
        self.client = kwargs.get('client')

    @pyqtSlot()
    def run(self):
        try:
            txt_log = 'Определение адреса контроллера..'
            self.signals.thread_log.emit(txt_log)
            for i in range(1, 33):
                rr = self.client.read_holding_registers(0, 1, slave=i)
                if not rr.isError():
                    self.signals.find_result.emit(rr.registers[0])
                    txt_log = 'Адрес контроллера определён - {}'.format(i)
                    self.signals.thread_log.emit(txt_log)
                    break

                else:
                    txt_log = 'Определение адреса контроллера.. - {} не верен'.format(i)
                    self.signals.thread_log.emit(txt_log)

        except Exception as e:
            txt_log = 'ERROR in thread FindAdr - {}'.format(e)
            self.signals.thread_log.emit(txt_log)


class Reader(QRunnable):
    signals = Signals()

    def __init__(self):
        super(Reader, self).__init__()
        self.cycle = True
        self.is_run = False

    @pyqtSlot()
    def run(self):
        while self.cycle:
            try:
                if not self.is_run:
                    time.sleep(0.01)
                else:
                    rr = self.client.read_holding_registers(0x1060, 23, slave=self.dev_id)
                    if not rr.isError():

                        result = self.parse_registers(rr.registers)

                        self.signals.read_result.emit(result)
                        txt_log = 'Данные получены ' + str(datetime.now())[:-3]
                        self.signals.thread_log.emit(txt_log)
                        time.sleep(1)

                    else:
                        self.signals.thread_log.emit(str(rr))

            except Exception as e:
                self.signals.thread_log.emit(str(e))

    def parse_registers(self, registers):
        decode = dict()
        decode['napr_veter_adc'] = registers[0]
        decode['napr_veter_gr'] = registers[1]
        decode['napr_veter_sr'] = registers[2]
        decode['scor_veter_adc'] = registers[3]
        decode['himid_adc'] = registers[4]
        decode['adr_scor_veter'] = round(unpack('f', pack('<HH', registers[6], registers[5]))[0], 2)
        decode['scor_veter_sr'] = round(unpack('f', pack('<HH', registers[8], registers[7]))[0], 2)
        decode['himid'] = round(unpack('f', pack('<HH', registers[10], registers[9]))[0], 2)
        decode['t_18b20'] = round(unpack('f', pack('<HH', registers[12], registers[11]))[0], 2)
        decode['k_scor_veter'] = round(unpack('f', pack('<HH', registers[14], registers[13]))[0], 2)
        decode['cpar_himid'] = round(unpack('f', pack('<HH', registers[16], registers[15]))[0], 2)
        decode['c_himid'] = round(unpack('f', pack('<HH', registers[18], registers[17]))[0], 2)
        decode['k_upit'] = round(unpack('f', pack('<HH', registers[20], registers[19]))[0], 2)
        decode['u_bat_d'] = round(unpack('f', pack('<HH', registers[22], registers[21]))[0], 2)

        return decode

    def startThread(self, client, dev_id):
        self.client = client
        self.dev_id = dev_id
        self.is_run = True

    def stopThread(self):
        self.is_run = False

    def exitThread(self):
        self.cycle = False


class Writer(QRunnable):
    signal = Signals()

    def __init__(self, **kwargs):
        super(Writer, self).__init__()
        self.client = kwargs.get('client')
        self.start_adr = kwargs.get('start_adr')
        self.values = kwargs.get('value')
        self.dev_id = kwargs.get('dev_id')
        self.number_attempts = 0
        self.max_attempts = 5
        self.flag_write = False

    @pyqtSlot()
    def run(self):
        try:
            while self.number_attempts <= self.max_attempts:
                txt = 'Writer, start_adr - {}, value - {}'.format(self.start_adr, self.values)
                self.signal.thread_log.emit(txt)
                rq = self.client.write_registers(self.start_adr, self.values, slave=self.dev_id)
                time.sleep(0.1)
                if not rq.isError():
                    txt = 'Complite write value {} in reg - {}'.format(self.values, self.start_adr)
                    self.signal.thread_log.emit(txt)
                    self.flag_write = True
                    self.number_attempts = self.max_attempts + 1

                else:
                    txt = 'Attempts write: {}, value {} in reg - {}'.format(self.number_attempts, self.values,
                                                                            self.start_adr)
                    self.signal.thread_log.emit(txt)
                    self.number_attempts += 1
                    time.sleep(0.5)

        except Exception as e:
            txt_log = 'ERROR in thread Write - {}'.format(e)
            self.signal.thread_log.emit(txt_log)
