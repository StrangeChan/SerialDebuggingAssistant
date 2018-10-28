# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets,QtSerialPort
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QToolTip
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QCursor
from ui_mainwidow import Ui_MainWindow
from Receive import Receive

OFF = False
ON = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.__uartState = OFF
        self.__serialPort = QtSerialPort.QSerialPort()
        self.__receiveThread = QThread(self)
        self.__uartReceive = Receive(self.__serialPort)
        self.__uartReceive.moveToThread(self.__receiveThread)
        self.uart_init()

        self.ui.pushButton_uart_sw.clicked.connect(self.change_uart_state)
        self.ui.pushButton_uart_rfresh.clicked.connect(self.refresh_uart_info)
        self.ui.comboBox_com.currentTextChanged.connect(self.change_combox_tooltip)

    def uart_init(self):
        self.__uartState = OFF
        self.ui.comboBox_com.clear()

        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ui.comboBox_com.addItem(info.portName() + ":" + info.description())

        self.ui.comboBox_com.setCurrentIndex(0)
        self.ui.comboBox_com.setToolTip(self.ui.comboBox_com.currentText())

    def change_uart_state(self):
        if self.__uartState:
            self.__serialPort.close()
            self.__uartState = OFF
            self.ui.pushButton_uart_sw.setText("打开串口")
            self.ui.comboBox_com.setEnabled(True)
        else:
            self.__serialPort.setPortName(self.ui.comboBox_com.currentText().split(':')[0])
            self.__serialPort.setBaudRate(int(self.ui.comboBox_baud.currentText()))
            self.__serialPort.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)
            self.__serialPort.setDataBits(QtSerialPort.QSerialPort.Data8)
            self.__serialPort.setStopBits(QtSerialPort.QSerialPort.OneStop)
            self.__serialPort.setParity(QtSerialPort.QSerialPort.NoParity)
            self.__serialPort.setReadBufferSize(10)

            # print(self.__serialPort.open(QtSerialPort.QSerialPort.ReadWrite))

            if self.__serialPort.open(QtSerialPort.QSerialPort.ReadWrite):
                self.__uartState = ON
                self.__receiveThread.start()
                self.__serialPort.readyRead.connect(self.__uartReceive.receive_uart_data)

                self.ui.pushButton_uart_sw.setText("关闭串口")
                self.ui.comboBox_baud.setEnabled(False)
                self.ui.comboBox_com.setEnabled(False)
            else:
                QMessageBox.critical(self,"Error","Fail to turn on this device!")
                print(self.__serialPort.error())

    def refresh_uart_info(self):
        if self.__uartState == ON:
            QToolTip.showText(QCursor.pos(),"Please turn off the current device first.")
        else:
            self.uart_init()

    def change_combox_tooltip(self):
        self.ui.comboBox_com.setToolTip(self.ui.comboBox_com.currentText())
