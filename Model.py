import sys
import serial
from PyQt5.QtCore import QObject, QThreadPool, pyqtSignal
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from Threads import FindAdr, Reader, Writer


class WindowSignals(QObject):
    startRead = pyqtSignal()
    stopRead = pyqtSignal()
    exitRead = pyqtSignal()


class Model:
    def __init__(self):
        self.signals = WindowSignals()
        self.threadpool = QThreadPool()

        self.available_ports = self.port_scan()


    def port_scan(self):
        try:
            result = []
            ports = ['COM{}'.format(i + 1) for i in range(256)]
            for port in ports:
                try:
                    s = serial.Serial(port)
                    s.close()
                    result.append(port)

                except:
                    pass

            return result

        except Exception as e:
            print(str(e))

    def initClient(self, com):
        try:
            self.client = ModbusClient(method='rtu', port=com,
                                       parity='N', baudrate=57600, startbit=1,
                                       databits=8, stopbits=1, strict=False)

            self.client.connect()

        except Exception as e:
            print(str(e))

    def initFindAdr(self):
        try:
            self.findAdr = FindAdr(self.client)
            self.findAdr.signals.result_find.connect(self.findResult)
            self.findAdr.signals.result_log.connect(self.printLog)
            self.findAdr.signals.error_read.connect(self.printError)
            self.threadpool.start(self.findAdr)

        except Exception as e:
            print(str(e))

    def findResult(self, data):
        self.adr_contr = data

    def printError(self, data):
        print(data)

    def printLog(self, txt_log):
        print(txt_log)

    def initReader(self, dev_id=1):
        try:
            self.reader = Reader(self.client, dev_id)
            self.reader.signals.result.connect(self.resultRead)
            self.reader.signals.error_read.connect(self.printError)
            self.signals.startRead.connect(self.reader.startThread)
            self.signals.stopRead.connect(self.reader.stopThread)
            self.signals.exitRead.connect(self.reader.exitThread)
            self.threadpool.start(self.reader)

        except Exception as e:
            print(str(e))

    def startRead(self):
        self.signals.startRead.emit()

    def stopRead(self):
        self.signals.stopRead.emit()

    def exitRead(self):
        self.signals.exitRead.emit()

    def resultRead(self, data):
        print(data)