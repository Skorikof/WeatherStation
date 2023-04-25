import time
from PyQt5.QtCore import QObject, QRunnable, pyqtSignal, pyqtSlot


class Signals(QObject):
    result = pyqtSignal(object)
    result_find = pyqtSignal(int)
    error_read = pyqtSignal(str)
    finish_write = pyqtSignal()
    error_write = pyqtSignal(object)
    result_log = pyqtSignal(object)

class FindAdr(QRunnable):
    signals = Signals()

    def __init__(self,client):
        super(FindAdr, self).__init__()
        self.client = client

    @pyqtSlot()
    def run(self):
        try:
            for i in range(1, 33):
                rr = self.client.read_holding_registers(0, 1, unit=i)
                if not rr.isError():
                    self.signals.result_find.emit(rr.registers[0])
                    txt_log = 'Адрес контроллера определён - {}'.format(i)
                    break
                else:
                    txt_log = 'Определение адреса контроллера.. - {} не подходит'.format(i)

            self.signals.result_log.emit(txt_log)

        except Exception as e:
            print('Exception: ' + str(e))


class Reader(QRunnable):
    signals = Signals()

    def __init__(self, client, dev_id):
        super(Reader, self).__init__()
        self.client = client
        self.dev_id = dev_id
        self.cycle = True
        self.is_run = False

    @pyqtSlot()
    def run(self):
        while self.cycle:
            try:
                if not self.is_run:
                    time.sleep(0.01)
                else:
                    rr = self.client.read_holding_registers(4192, 23, unit=self.dev_id)
                    if not rr.isError():
                        self.signals.result.emit(rr)
                    else:
                        self.signals.error_read.emit(rr)

            except Exception as e:
                self.signals.error_read.emit(rr)

    def startThread(self):
        self.is_run = True

    def stopThread(self):
        self.is_run = False

    def exitThread(self):
        self.cycle = False


class Writer(QRunnable):
    signals = Signals()

    def __init__(self, client, dev_id, start_adr, values):
        super(Writer,self).__init__()
        self.client = client
        self.dev_id = dev_id
        self.start_adr = start_adr
        self.values = values
        self.num_attempts = 0
        self.max_attempts = 4
        self.flag_write = False

    @pyqtSlot()
    def run(self):
        try:
            while self.num_attempts <= self.max_attempts:
                rr = self.client.write_registers(self.start_adr, self.values, unit=self.dev_id)
                if not rr.isError():
                    self.flag_write = True
                    self.num_attempts = self.max_attempts + 1
                    self.signals.finish_write.emit()

            if not self.flag_write:
                self.signals.error_write.emit(rr)

        except Exception as e:
            self.signals.error_write.emit(e)
