import serial
from struct import pack, unpack
from PyQt5.QtCore import QObject, QThreadPool, pyqtSignal
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from Threads import FindAdr, Reader, Writer


class StructController:
    def __init__(self):
        self.adr_dev = 1
        self.napr_veter_adc = 0
        self.napr_veter_gr = 0
        self.napr_veter_sr = 0
        self.scor_veter_adc = 0
        self.himid_adc = 0
        self.adr_scor_veter = 0
        self.scor_veter_sr = 0
        self.himid = 0
        self.t_18b20 = 0
        self.k_scor_veter = 0
        self.cpar_himid = 0
        self.c_himid = 0
        self.k_upit = 0
        self.u_bat_d = 0


class WindowSignals(QObject):
    startFind = pyqtSignal(object)
    stopFind = pyqtSignal()
    exitFind = pyqtSignal()
    startRead = pyqtSignal(object, int)
    stopRead = pyqtSignal()
    exitRead = pyqtSignal()
    startWrite = pyqtSignal(object, str, int, list, int)
    stopWrite = pyqtSignal()
    exitWrite = pyqtSignal()
    stbar_msg = pyqtSignal(str)
    finish_read = pyqtSignal()
    flag_adr = pyqtSignal()
    pauseProg = pyqtSignal()


class Model:
    def __init__(self):
        self.struct = StructController()
        self.com_port = ''
        self.flag_connect = False
        self.signals = WindowSignals()
        self.threadpool = QThreadPool()

        self.available_ports = self.port_scan()
        self.initFindAdr()
        self.initReader()
        self.initWriter()

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

    def StatusBarMsg(self, text_bar):
        self.signals.stbar_msg.emit(text_bar)

    def initClient(self):
        try:
            self.client = ModbusClient(method='rtu', port=self.com_port,
                                       parity='N', baudrate=57600, startbit=1,
                                       databits=8, stopbits=1, strict=False)

            self.flag_connect = self.client.connect()
            txt_bar = 'Подключение к контроллеру'
            self.StatusBarMsg(txt_bar)

            if self.flag_connect:
                txt_bar = 'Контроллер подключен'

            else:
                txt_bar = 'Подключение не удалось'
            self.StatusBarMsg(txt_bar)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def stopClient(self):
        self.client.close()
        self.flag_connect = False
        txt_bar = 'Контроллер отключен'
        self.StatusBarMsg(txt_bar)

    def initFindAdr(self):
        try:
            self.findAdr = FindAdr()
            self.findAdr.signals.find_result.connect(self.findResult)
            self.findAdr.signals.find_log.connect(self.printLog)
            self.findAdr.signals.find_error.connect(self.findError)
            self.signals.startFind.connect(self.findAdr.startThread)
            self.signals.stopFind.connect(self.findAdr.stopThread)
            self.signals.exitFind.connect(self.findAdr.exitThread)
            self.threadpool.start(self.findAdr)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def startFind(self):
        self.signals.startFind.emit(self.client)

    def stopFind(self):
        self.signals.stopFind.emit()

    def exitFind(self):
        self.signals.exitFind.emit()

    def findResult(self, data):
        self.struct.adr_dev = data
        self.signals.flag_adr.emit()

    def findError(self, data):
        self.StatusBarMsg(data)
        print(data)

    def printLog(self, txt_log):
        self.StatusBarMsg(txt_log)
        print(txt_log)

    def initReader(self):
        try:
            self.reader = Reader()
            self.reader.signals.read_result.connect(self.readResult)
            self.reader.signals.read_error.connect(self.readError)
            self.reader.signals.read_log.connect(self.printLog)
            self.signals.startRead.connect(self.reader.startThread)
            self.signals.stopRead.connect(self.reader.stopThread)
            self.signals.exitRead.connect(self.reader.exitThread)
            self.threadpool.start(self.reader)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def startRead(self):
        self.signals.startRead.emit(self.client, self.struct.adr_dev)

    def stopRead(self):
        self.signals.stopRead.emit()
        txt_log = 'Чтение контроллера остановлено'
        self.StatusBarMsg(txt_log)

    def exitRead(self):
        self.signals.exitRead.emit()

    def readError(self, txt_log):
        self.StatusBarMsg(txt_log)
        print(txt_log)

    def readResult(self, data):
        try:
            self.struct.napr_veter_adc = data[0]
            self.struct.napr_veter_gr = data[1]
            self.struct.napr_veter_sr = data[2]
            if data[3] == 65535:
                data[3] = 0
            self.struct.scor_veter_adc = data[3]
            self.struct.himid_adc = data[4]
            self.struct.adr_scor_veter = data[5]
            self.struct.scor_veter_sr = data[6]
            self.struct.himid = data[7]
            self.struct.t_18b20 = data[8]
            self.struct.k_scor_veter = data[9]
            self.struct.cpar_himid = data[10]
            self.struct.c_himid = data[11]
            self.struct.k_upit = data[12]
            self.struct.u_bat_d = data[13]

            self.signals.finish_read.emit()

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def initWriter(self):
        try:
            self.writer = Writer()
            self.writer.signals.write_adr.connect(self.writeAdr)
            self.writer.signals.write_koef.connect(self.writeKoef)
            self.writer.signals.write_error.connect(self.writeError)
            self.writer.signals.write_log.connect(self.printLog)
            self.signals.startWrite.connect(self.writer.startThread)
            self.signals.stopWrite.connect(self.writer.stopThread)
            self.signals.exitWrite.connect(self.writer.exitThread)

            self.threadpool.start(self.writer)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))

    def startWriter(self, tag, start_adr, values, dev_id):
        self.signals.startWrite.emit(self.client, tag, start_adr, values, dev_id)

    def stopWriter(self):
        self.signals.stopWrite.emit()

    def exitWriter(self):
        self.signals.exitWrite.emit()

    def writeAdr(self, data):
        self.stopWriter()
        self.struct.adr_dev = data
        self.signals.flag_adr.emit()
        self.pauseProg()

    def writeKoef(self):
        self.stopWriter()
        self.pauseProg()

    def writeError(self, txt_log):
        self.stopWriter()
        self.StatusBarMsg(txt_log)
        print(txt_log)

    def pauseProg(self):
        self.signals.pauseProg.emit()

    def floatToByte(self, start_adr, value, dev_id):
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

            self.startWriter('koef', start_adr, val_regs, dev_id)

        except Exception as e:
            self.StatusBarMsg(str(e))
            print(str(e))
