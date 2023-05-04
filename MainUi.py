# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 900)
        MainWindow.setMinimumSize(QtCore.QSize(450, 900))
        MainWindow.setMaximumSize(QtCore.QSize(450, 900))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connect_btn = QtWidgets.QPushButton(self.centralwidget)
        self.connect_btn.setGeometry(QtCore.QRect(10, 50, 120, 30))
        self.connect_btn.setMinimumSize(QtCore.QSize(120, 30))
        self.connect_btn.setMaximumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.connect_btn.setFont(font)
        self.connect_btn.setObjectName("connect_btn")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 668, 240, 45))
        self.label_13.setMinimumSize(QtCore.QSize(240, 0))
        self.label_13.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 240, 40))
        self.label_7.setMinimumSize(QtCore.QSize(240, 0))
        self.label_7.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.diff_humidity = QtWidgets.QLineEdit(self.centralwidget)
        self.diff_humidity.setGeometry(QtCore.QRect(280, 670, 100, 40))
        self.diff_humidity.setMinimumSize(QtCore.QSize(100, 40))
        self.diff_humidity.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.diff_humidity.setFont(font)
        self.diff_humidity.setStyleSheet("background-color: rgb(148, 255, 173);")
        self.diff_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.diff_humidity.setObjectName("diff_humidity")
        self.direct_wind_avarage = QtWidgets.QLineEdit(self.centralwidget)
        self.direct_wind_avarage.setGeometry(QtCore.QRect(280, 271, 100, 40))
        self.direct_wind_avarage.setMinimumSize(QtCore.QSize(100, 40))
        self.direct_wind_avarage.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.direct_wind_avarage.setFont(font)
        self.direct_wind_avarage.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.direct_wind_avarage.setAlignment(QtCore.Qt.AlignCenter)
        self.direct_wind_avarage.setReadOnly(True)
        self.direct_wind_avarage.setObjectName("direct_wind_avarage")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 269, 240, 45))
        self.label_5.setMinimumSize(QtCore.QSize(240, 0))
        self.label_5.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.temp_ds18b20 = QtWidgets.QLineEdit(self.centralwidget)
        self.temp_ds18b20.setGeometry(QtCore.QRect(280, 569, 100, 40))
        self.temp_ds18b20.setMinimumSize(QtCore.QSize(100, 40))
        self.temp_ds18b20.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.temp_ds18b20.setFont(font)
        self.temp_ds18b20.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.temp_ds18b20.setAlignment(QtCore.Qt.AlignCenter)
        self.temp_ds18b20.setReadOnly(True)
        self.temp_ds18b20.setObjectName("temp_ds18b20")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 115, 240, 22))
        self.label.setMinimumSize(QtCore.QSize(240, 0))
        self.label.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.direct_wind = QtWidgets.QLineEdit(self.centralwidget)
        self.direct_wind.setGeometry(QtCore.QRect(280, 218, 100, 40))
        self.direct_wind.setMinimumSize(QtCore.QSize(100, 40))
        self.direct_wind.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.direct_wind.setFont(font)
        self.direct_wind.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.direct_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.direct_wind.setReadOnly(True)
        self.direct_wind.setObjectName("direct_wind")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 322, 240, 22))
        self.label_6.setMinimumSize(QtCore.QSize(240, 0))
        self.label_6.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 418, 240, 22))
        self.label_8.setMinimumSize(QtCore.QSize(240, 0))
        self.label_8.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.speed_wind_avarage = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_wind_avarage.setGeometry(QtCore.QRect(280, 468, 100, 40))
        self.speed_wind_avarage.setMinimumSize(QtCore.QSize(100, 40))
        self.speed_wind_avarage.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.speed_wind_avarage.setFont(font)
        self.speed_wind_avarage.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.speed_wind_avarage.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_wind_avarage.setReadOnly(True)
        self.speed_wind_avarage.setObjectName("speed_wind_avarage")
        self.humidity = QtWidgets.QLineEdit(self.centralwidget)
        self.humidity.setGeometry(QtCore.QRect(280, 519, 100, 40))
        self.humidity.setMinimumSize(QtCore.QSize(100, 40))
        self.humidity.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.humidity.setFont(font)
        self.humidity.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity.setReadOnly(True)
        self.humidity.setObjectName("humidity")
        self.adr_control = QtWidgets.QLineEdit(self.centralwidget)
        self.adr_control.setGeometry(QtCore.QRect(280, 115, 100, 40))
        self.adr_control.setMinimumSize(QtCore.QSize(100, 40))
        self.adr_control.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.adr_control.setFont(font)
        self.adr_control.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.adr_control.setText("")
        self.adr_control.setCursorPosition(0)
        self.adr_control.setAlignment(QtCore.Qt.AlignCenter)
        self.adr_control.setReadOnly(True)
        self.adr_control.setObjectName("adr_control")
        self.direct_wind_acp = QtWidgets.QLineEdit(self.centralwidget)
        self.direct_wind_acp.setGeometry(QtCore.QRect(280, 165, 100, 40))
        self.direct_wind_acp.setMinimumSize(QtCore.QSize(100, 40))
        self.direct_wind_acp.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.direct_wind_acp.setFont(font)
        self.direct_wind_acp.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.direct_wind_acp.setText("")
        self.direct_wind_acp.setAlignment(QtCore.Qt.AlignCenter)
        self.direct_wind_acp.setReadOnly(True)
        self.direct_wind_acp.setObjectName("direct_wind_acp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 216, 240, 45))
        self.label_4.setMinimumSize(QtCore.QSize(240, 0))
        self.label_4.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.speed_wind_metr = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_wind_metr.setGeometry(QtCore.QRect(280, 418, 100, 40))
        self.speed_wind_metr.setMinimumSize(QtCore.QSize(100, 40))
        self.speed_wind_metr.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.speed_wind_metr.setFont(font)
        self.speed_wind_metr.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.speed_wind_metr.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_wind_metr.setReadOnly(True)
        self.speed_wind_metr.setObjectName("speed_wind_metr")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 466, 240, 45))
        self.label_9.setMinimumSize(QtCore.QSize(240, 0))
        self.label_9.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 567, 240, 45))
        self.label_11.setMinimumSize(QtCore.QSize(240, 0))
        self.label_11.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 620, 240, 22))
        self.label_12.setMinimumSize(QtCore.QSize(240, 0))
        self.label_12.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.humidity_counter = QtWidgets.QLineEdit(self.centralwidget)
        self.humidity_counter.setGeometry(QtCore.QRect(280, 370, 100, 40))
        self.humidity_counter.setMinimumSize(QtCore.QSize(100, 40))
        self.humidity_counter.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.humidity_counter.setFont(font)
        self.humidity_counter.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.humidity_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.humidity_counter.setReadOnly(True)
        self.humidity_counter.setObjectName("humidity_counter")
        self.speed_wind = QtWidgets.QLineEdit(self.centralwidget)
        self.speed_wind.setGeometry(QtCore.QRect(280, 322, 100, 40))
        self.speed_wind.setMinimumSize(QtCore.QSize(100, 40))
        self.speed_wind.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.speed_wind.setFont(font)
        self.speed_wind.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_wind.setReadOnly(True)
        self.speed_wind.setObjectName("speed_wind")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 163, 240, 45))
        self.label_3.setMinimumSize(QtCore.QSize(240, 0))
        self.label_3.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 519, 240, 22))
        self.label_10.setMinimumSize(QtCore.QSize(240, 0))
        self.label_10.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.diff_speed_wind = QtWidgets.QLineEdit(self.centralwidget)
        self.diff_speed_wind.setGeometry(QtCore.QRect(280, 620, 100, 40))
        self.diff_speed_wind.setMinimumSize(QtCore.QSize(100, 40))
        self.diff_speed_wind.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.diff_speed_wind.setFont(font)
        self.diff_speed_wind.setStyleSheet("background-color: rgb(148, 255, 173);")
        self.diff_speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.diff_speed_wind.setObjectName("diff_speed_wind")
        self.calc_humidity = QtWidgets.QLineEdit(self.centralwidget)
        self.calc_humidity.setGeometry(QtCore.QRect(280, 723, 100, 40))
        self.calc_humidity.setMinimumSize(QtCore.QSize(100, 40))
        self.calc_humidity.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.calc_humidity.setFont(font)
        self.calc_humidity.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.calc_humidity.setAlignment(QtCore.Qt.AlignCenter)
        self.calc_humidity.setReadOnly(True)
        self.calc_humidity.setObjectName("calc_humidity")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 774, 240, 45))
        self.label_15.setMinimumSize(QtCore.QSize(240, 0))
        self.label_15.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.diff_voltage = QtWidgets.QLineEdit(self.centralwidget)
        self.diff_voltage.setGeometry(QtCore.QRect(280, 776, 100, 40))
        self.diff_voltage.setMinimumSize(QtCore.QSize(100, 40))
        self.diff_voltage.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.diff_voltage.setFont(font)
        self.diff_voltage.setStyleSheet("background-color: rgb(148, 255, 173);")
        self.diff_voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.diff_voltage.setObjectName("diff_voltage")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(20, 721, 240, 45))
        self.label_14.setMinimumSize(QtCore.QSize(240, 0))
        self.label_14.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(20, 827, 240, 22))
        self.label_16.setMinimumSize(QtCore.QSize(240, 0))
        self.label_16.setMaximumSize(QtCore.QSize(240, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.voltage = QtWidgets.QLineEdit(self.centralwidget)
        self.voltage.setGeometry(QtCore.QRect(280, 827, 100, 40))
        self.voltage.setMinimumSize(QtCore.QSize(100, 40))
        self.voltage.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.voltage.setFont(font)
        self.voltage.setStyleSheet("background-color: rgb(161, 255, 255);")
        self.voltage.setAlignment(QtCore.Qt.AlignCenter)
        self.voltage.setReadOnly(True)
        self.voltage.setObjectName("voltage")
        self.com_port_cb = QtWidgets.QComboBox(self.centralwidget)
        self.com_port_cb.setGeometry(QtCore.QRect(10, 10, 90, 30))
        self.com_port_cb.setMinimumSize(QtCore.QSize(90, 30))
        self.com_port_cb.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.com_port_cb.setFont(font)
        self.com_port_cb.setObjectName("com_port_cb")
        self.read_base_btn = QtWidgets.QPushButton(self.centralwidget)
        self.read_base_btn.setGeometry(QtCore.QRect(280, 10, 150, 30))
        self.read_base_btn.setMinimumSize(QtCore.QSize(150, 30))
        self.read_base_btn.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.read_base_btn.setFont(font)
        self.read_base_btn.setObjectName("read_base_btn")
        self.find_addr_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_addr_btn.setGeometry(QtCore.QRect(150, 50, 180, 30))
        self.find_addr_btn.setMinimumSize(QtCore.QSize(180, 30))
        self.find_addr_btn.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.find_addr_btn.setFont(font)
        self.find_addr_btn.setObjectName("find_addr_btn")
        self.adr_control_start = QtWidgets.QLineEdit(self.centralwidget)
        self.adr_control_start.setGeometry(QtCore.QRect(110, 10, 50, 30))
        self.adr_control_start.setMinimumSize(QtCore.QSize(50, 30))
        self.adr_control_start.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.adr_control_start.setFont(font)
        self.adr_control_start.setStyleSheet("background-color: rgb(148, 255, 173);")
        self.adr_control_start.setText("")
        self.adr_control_start.setCursorPosition(0)
        self.adr_control_start.setAlignment(QtCore.Qt.AlignCenter)
        self.adr_control_start.setObjectName("adr_control_start")
        self.write_adr_btn = QtWidgets.QPushButton(self.centralwidget)
        self.write_adr_btn.setGeometry(QtCore.QRect(170, 10, 90, 30))
        self.write_adr_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.write_adr_btn.setMaximumSize(QtCore.QSize(90, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.write_adr_btn.setFont(font)
        self.write_adr_btn.setObjectName("write_adr_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.statusBar.setFont(font)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Контроллер метеостанции"))
        self.connect_btn.setText(_translate("MainWindow", "Подключиться"))
        self.label_13.setText(_translate("MainWindow", "Паразитная ёмкость\n"
"датчика влажности"))
        self.label_7.setText(_translate("MainWindow", "Счётчик датчика влажности"))
        self.label_5.setText(_translate("MainWindow", "Усреднённое направление\n"
"ветра в градусах"))
        self.label.setText(_translate("MainWindow", "Адрес контроллера"))
        self.label_6.setText(_translate("MainWindow", "Скорость ветра"))
        self.label_8.setText(_translate("MainWindow", "Скорость ветра, м/с"))
        self.label_4.setText(_translate("MainWindow", "Направление ветра\n"
"в градусах"))
        self.label_9.setText(_translate("MainWindow", "Скорость ветра\n"
"средняя за 10 мин, м/с"))
        self.label_11.setText(_translate("MainWindow", "Температура с датчика\n"
" DS18B20 в градусах"))
        self.label_12.setText(_translate("MainWindow", "Поправка скорости ветра"))
        self.label_3.setText(_translate("MainWindow", "Направление ветра\n"
"в битах АЦП"))
        self.label_10.setText(_translate("MainWindow", "Влажность, %"))
        self.label_15.setText(_translate("MainWindow", "Поправка напряжения\n"
"питания"))
        self.label_14.setText(_translate("MainWindow", "Вычисленная ёмкость\n"
"датчика влажности"))
        self.label_16.setText(_translate("MainWindow", "Напряжение батареи"))
        self.read_base_btn.setText(_translate("MainWindow", "Читать"))
        self.find_addr_btn.setText(_translate("MainWindow", "Определить адрес"))
        self.write_adr_btn.setText(_translate("MainWindow", "Записать"))
