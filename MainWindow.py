# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtSerialPort,QtWidgets
from PyQt5.QtWidgets import QMessageBox,QMainWindow,QToolTip,QFileDialog
from PyQt5.QtCore import QThread,QFile
from PyQt5.QtGui import QCursor,QIcon,QPainter
from PyQt5.QtChart import QChartView
from ui_mainwidow import Ui_MainWindow
from Receive import Receive
from CurveWidget import CurveChart
import struct
# import chardet
# from QCandyUi import CandyWindow
# from QCandyUi.CandyWindow import colorful
# import time

OFF = False
ON = True

# @colorful('blue Green')
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui = CandyWindow.createWindow(self.ui, 'blueGreen',"串口调试助手",'1.ico')
        self.setWindowIcon(QIcon('1.ico'))

        self.__curveChart = CurveChart()
        self.__curveChart.legend().hide()
        self.__chartView = QChartView(self.__curveChart)
        self.__chartView.setRenderHint(QPainter.Antialiasing)   #反走样
        # self.__chartView.setMargins(100,0,0,0)
        self.__layOut = QtWidgets.QVBoxLayout(self.ui.widget_dynamic_curve)
        self.__layOut.addWidget(self.__chartView)
        # self.__layOut.setContentsMargins(0,0,0,0)

        self.__uartState = OFF  # 常规串口
        self.__serialPort = QtSerialPort.QSerialPort()
        self.__uart2State = OFF  # PID调参串口
        self.__serialPort2 = QtSerialPort.QSerialPort()

        self.__receiveThread = QThread(self)
        self.__uartReceive = Receive(self.__serialPort2)
        self.__uartReceive.moveToThread(self.__receiveThread)
        self.__plotThread = QThread(self)
        self.ui.widget_dynamic_curve.moveToThread(self.__plotThread)
        self.__plotThread.start()

        self.uart_init()
        self.uart2_init()
        # PID滑动条初始化
        self.__maxP = 10.0
        self.__maxI = 0.1
        self.__maxD = 1.0
        self.ui.doubleSpinBox_max_P.setValue(self.__maxP)
        self.ui.doubleSpinBox_max_I.setValue(self.__maxI)
        self.ui.doubleSpinBox_max_D.setValue(self.__maxD)
        self.ui.doubleSpinBox_P.setDecimals(1)
        self.ui.doubleSpinBox_I.setDecimals(3)
        self.ui.doubleSpinBox_D.setDecimals(2)

        # self.__curveDataS = CurveDataS(self.ui.widget_dynamic_curve)
        # signal and slot
        self.ui.pushButton_uart_sw.clicked.connect(self.change_uart_state)
        self.ui.pushButton_uart_rfresh.clicked.connect(self.refresh_uart_info)
        self.ui.comboBox_com.currentTextChanged.connect(self.change_combox_tooltip)
        self.ui.radioButton_show_ascii.toggled.connect(self.display_ascii)
        self.ui.radioButton_show_hex.toggled.connect(self.display_hex)
        self.ui.pushButton_clean.clicked.connect(self.clean_display)
        self.ui.pushButton_save.clicked.connect(self.save_receive_data)
        self.ui.radioButton_tx_hex.toggled.connect(self.change_tx_mode)
        # self.ui.radioButton_tx_ascii.toggled.connect(self.change_tx_mode)
        self.ui.pushButton_tx.clicked.connect(self.transmit_data)

        self.ui.pushButton_uart_sw_2.clicked.connect(self.change_uart2_state)
        self.ui.pushButton_uart_rfresh_2.clicked.connect(self.refresh_uart2_info)
        self.ui.comboBox_com_2.currentTextChanged.connect(self.change_combox_tooltip)

        self.ui.doubleSpinBox_max_P.valueChanged.connect(self.set_p_max_value)
        self.ui.doubleSpinBox_max_I.valueChanged.connect(self.set_i_max_value)
        self.ui.doubleSpinBox_max_D.valueChanged.connect(self.set_d_max_value)
        self.ui.verticalSlider_P.valueChanged.connect(self.change_p_para_display)
        self.ui.verticalSlider_I.valueChanged.connect(self.change_i_para_display)
        self.ui.verticalSlider_D.valueChanged.connect(self.change_d_para_display)
        self.ui.doubleSpinBox_P.valueChanged.connect(self.change_p_slider_value)
        self.ui.doubleSpinBox_I.valueChanged.connect(self.change_i_slider_value)
        self.ui.doubleSpinBox_D.valueChanged.connect(self.change_d_slider_value)
        # 滑动条改变曲线图X大小
        # self.ui.horizontalSlider.valueChanged.connect(self.ui.widget_dynamic_curve.change_the_radio)
        self.ui.horizontalSlider.valueChanged.connect(self.__curveChart.change_the_radio)
        self.ui.checkBox_curve_show_random.toggled.connect(self.plot_random_data)
        # for i in range(len(self.__curveData)):
        #     self.__curveData[i].plot_data.connect(self.ui.widget_dynamic_curve.plot)
        #     self.__curveData[i].Id = i      # 设置标号 对应显示通道数目
        # self.__curveDataS.plot_data.connect(self.ui.widget_dynamic_curve.plot)
        self.__uartReceive.receive_success.connect(self.add_plot_data)

    def uart_init(self):
        self.__uartState = OFF
        self.ui.comboBox_com.clear()
        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ui.comboBox_com.addItem(info.portName() + ":" + info.description())
        self.ui.comboBox_com.setCurrentIndex(0)
        self.ui.comboBox_com.setToolTip(self.ui.comboBox_com.currentText())

    def uart2_init(self):
        self.__uart2State = OFF
        self.ui.comboBox_com_2.clear()
        for info in QtSerialPort.QSerialPortInfo.availablePorts():
            self.ui.comboBox_com_2.addItem(info.portName() + ":" + info.description())
        self.ui.comboBox_com_2.setCurrentIndex(0)
        self.ui.comboBox_com_2.setToolTip(self.ui.comboBox_com.currentText())

    def change_uart_state(self):
        if self.__uartState:
            self.__serialPort.close()
            self.__uartState = OFF
            self.ui.pushButton_uart_sw.setText("打开串口")
            self.ui.comboBox_com.setEnabled(True)
            self.ui.comboBox_baud.setEnabled(True)
        else:
            self.__serialPort.setPortName(self.ui.comboBox_com.currentText().split(':')[0])
            self.__serialPort.setBaudRate(int(self.ui.comboBox_baud.currentText()))
            self.__serialPort.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)
            self.__serialPort.setDataBits(QtSerialPort.QSerialPort.Data8)
            self.__serialPort.setStopBits(QtSerialPort.QSerialPort.OneStop)
            self.__serialPort.setParity(QtSerialPort.QSerialPort.NoParity)
            self.__serialPort.setReadBufferSize(10)

            if self.__serialPort.open(QtSerialPort.QSerialPort.ReadWrite):
                self.__uartState = ON
                # 常规模式
                self.__serialPort.readyRead.connect(self.receive_uart_data)

                self.ui.pushButton_uart_sw.setText("关闭串口")
                self.ui.comboBox_baud.setEnabled(False)
                self.ui.comboBox_com.setEnabled(False)
            else:
                QMessageBox.critical(self,"Error","Fail to turn on this device!")
                print(self.__serialPort.error())

    def change_uart2_state(self):
        if self.__uart2State:
            self.__serialPort2.close()
            self.__uart2State = OFF
            if self.__receiveThread.isRunning():
                self.__receiveThread.quit()
                self.__receiveThread.exit()
            self.ui.pushButton_uart_sw_2.setText("打开串口")
            self.ui.comboBox_com_2.setEnabled(True)
            self.ui.comboBox_baud_2.setEnabled(True)
            # 开启随机点
            self.ui.checkBox_curve_show_random.setEnabled(True)
            # self.__curveDataS.stop_plot()
        else:
            self.__serialPort2.setPortName(self.ui.comboBox_com_2.currentText().split(':')[0])
            self.__serialPort2.setBaudRate(int(self.ui.comboBox_baud_2.currentText()))
            self.__serialPort2.setFlowControl(QtSerialPort.QSerialPort.NoFlowControl)
            self.__serialPort2.setDataBits(QtSerialPort.QSerialPort.Data8)
            self.__serialPort2.setStopBits(QtSerialPort.QSerialPort.OneStop)
            self.__serialPort2.setParity(QtSerialPort.QSerialPort.NoParity)
            self.__serialPort2.setReadBufferSize(10)

            if self.__serialPort2.open(QtSerialPort.QSerialPort.ReadWrite):
                self.__uart2State = ON
                self.__receiveThread.start()
                # PID调参模式
                self.__serialPort2.readyRead.connect(self.__uartReceive.receive_uart_data)

                self.ui.pushButton_uart_sw_2.setText("关闭串口")
                self.ui.comboBox_baud_2.setEnabled(False)
                self.ui.comboBox_com_2.setEnabled(False)
                # 关闭随机点
                self.ui.checkBox_curve_show_random.setChecked(False)
                self.ui.checkBox_curve_show_random.setEnabled(False)
                self.__curveChart.start_plot()
            else:
                QMessageBox.critical(self,"Error","Fail to turn on this device!")
                # print(self.__serialPort2.error())

    def refresh_uart_info(self):
        if self.__uartState == ON:
            QToolTip.showText(QCursor.pos(),"Please turn off the current device first.")
        else:
            self.uart_init()

    def refresh_uart2_info(self):
        if self.__uart2State == ON:
            QToolTip.showText(QCursor.pos(),"Please turn off the current device first.")
        else:
            self.uart2_init()

    def change_combox_tooltip(self):
        self.ui.comboBox_com.setToolTip(self.ui.comboBox_com.currentText())
        self.ui.comboBox_com_2.setToolTip(self.ui.comboBox_com_2.currentText())

    def receive_uart_data(self):
        if self.__serialPort.isReadable():
            data = self.__serialPort.readAll()
            # _bytes = bytearray(data)
            # print(data)
            # print(data.length())
            if data.isEmpty():
                return
            self.ui.plainTextEdit_rx.moveCursor(QtGui.QTextCursor.End)

            if self.ui.radioButton_show_ascii.isChecked():
                # _bytes.decode('utf8')
                # print(chardet.detect(_bytes))
                try:
                    self.ui.plainTextEdit_rx.insertPlainText(str(data, encoding='gbk'))
                except :
                    self.ui.plainTextEdit_rx.insertPlainText(str(data))

            else:
                hexText = data.toHex().toUpper()
                # print(hexText)
                # print(hexText.length())
                for i in range(0,hexText.length(),2):
                    self.ui.plainTextEdit_rx.insertPlainText(' '+str(hexText.mid(i,2),encoding='gbk'))

    def display_ascii(self,checked):
        if checked:
            hexText = self.ui.plainTextEdit_rx.toPlainText().replace(" ","")#encode('gbk')
            # print(hexText)
            text =bytes.fromhex(hexText)
            # print(text)
            try:
                self.ui.plainTextEdit_rx.setPlainText(str(text, encoding='gbk'))
            except:
                self.ui.plainTextEdit_rx.setPlainText(str(text))

    def display_hex(self,checked):
        if checked:
            asciiText = self.ui.plainTextEdit_rx.toPlainText()
            hexText = bytes(asciiText,encoding='gbk').hex().upper()
            #print(hexText)
            self.ui.plainTextEdit_rx.setPlainText("")
            #print(len(hexText))
            for i in range(0,len(hexText),2):
                self.ui.plainTextEdit_rx.insertPlainText(' ' + hexText[i:i+2])

    def clean_display(self):
        self.ui.plainTextEdit_rx.clear()

    def save_receive_data(self):
        filename = QFileDialog.getSaveFileName(self,"Save as","/", "*.txt;;*.log")
        print(filename)
        print(type(filename))
        if len(filename[0]) > 0:
            file = QFile(filename[0])
            if file.open(QFile.WriteOnly|QFile.Text):
                os = QtCore.QTextStream(file)
                os << self.ui.plainTextEdit_rx.toPlainText()

    def change_tx_mode(self,checked):
        data = self.ui.plainTextEdit_tx.toPlainText()
        if checked:
            if len(data) > 0:
                hexText = bytes(data, encoding='gbk').hex().upper()
                self.ui.plainTextEdit_tx.setPlainText("")
                for i in range(0, len(hexText), 2):
                    self.ui.plainTextEdit_tx.insertPlainText(' ' + hexText[i:i + 2])
        else:
            if len(data) > 0:
                hexText = self.ui.plainTextEdit_tx.toPlainText().replace(" ", "")
                text = bytes.fromhex(hexText)
                try:
                    self.ui.plainTextEdit_tx.setPlainText(str(text, encoding='gbk'))
                except:
                    self.ui.plainTextEdit_tx.setPlainText(str(text))

    def transmit_data(self):
        data = self.ui.plainTextEdit_tx.toPlainText()
        if self.ui.radioButton_tx_hex.isChecked():
            data = bytes.fromhex(data.replace(" ", ""))
            # print(data)
            # data = str(text, encoding='gbk')
        else:
            data =  bytes(data, encoding='gbk')
        self.__serialPort.write(data)

    # 关闭窗口关闭线程
    def closeEvent(self, e):
        # print(1)
        b=QMessageBox.question(self, "滑稽", "陈奇是不是你爸爸",
                                   QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        while b == QMessageBox.No:
            b = QMessageBox.question(self, "滑稽", "陈奇是不是你爸爸",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        # 关闭串口
        if self.__uartState:
            self.__serialPort.close()
        if self.__uart2State:
            self.__serialPort2.close()
        # 关闭数据接收线程
        if self.__receiveThread.isRunning():
            self.__receiveThread.quit()
            self.__receiveThread.exit()
        # 关闭随机模拟曲线数据生成线程
        # for i in range(len(self.__curveData)):
        #     if self.__curveData[i].isRun == True:
        #         self.__curveData[i].release_plot()
        # if self.__curveDataS.isRandomRun:
        #     self.__curveDataS.release_random_plot()
        # self.__curveDataS.stop_plot()
        self.__curveChart.stop_random_plot()
        # print('k88888')
        # else:
        #     e.ignore()

    # 滑动条部分操作
    def set_p_max_value(self,max):
        self.__maxP = max
        if self.__maxP < 0.1:
            self.__maxP = 0.1
            self.ui.doubleSpinBox_max_P.setValue(0.1)
        if self.__maxP >= 100:
            self.ui.doubleSpinBox_P.setDecimals(0)
            self.ui.doubleSpinBox_P.setSingleStep(1)
        elif self.__maxP >= 10:
            self.ui.doubleSpinBox_P.setDecimals(1)
            self.ui.doubleSpinBox_P.setSingleStep(0.1)
        elif self.__maxP >= 1:
            self.ui.doubleSpinBox_P.setDecimals(2)
            self.ui.doubleSpinBox_P.setSingleStep(0.01)
        else:
            self.ui.doubleSpinBox_P.setDecimals(3)
            self.ui.doubleSpinBox_P.setSingleStep(0.001)
        # self.ui.doubleSpinBox_P.setValue(self.ui.verticalSlider_P.value() * self.__maxP / 100)

    def set_i_max_value(self,max):
        self.__maxI = max
        if self.__maxI < 0.1:
            self.__maxI = 0.1
            self.ui.doubleSpinBox_max_I.setValue(0.1)
        if self.__maxI >= 100:
            self.ui.doubleSpinBox_I.setDecimals(0)
            self.ui.doubleSpinBox_I.setSingleStep(1)
        elif self.__maxI >=10:
            self.ui.doubleSpinBox_I.setDecimals(1)
            self.ui.doubleSpinBox_I.setSingleStep(0.1)
        elif self.__maxI >= 1:
            self.ui.doubleSpinBox_I.setDecimals(2)
            self.ui.doubleSpinBox_I.setSingleStep(0.01)
        else:
            self.ui.doubleSpinBox_I.setDecimals(3)
            self.ui.doubleSpinBox_I.setSingleStep(0.001)
        # print(self.ui.verticalSlider_I.value(),1,self.__maxI)
        # self.ui.doubleSpinBox_I.setValue(self.ui.verticalSlider_I.value() * self.__maxI / 100)
        # print(self.ui.verticalSlider_I.value(),self.__maxI)

    def set_d_max_value(self,max):
        self.__maxD = max
        if self.__maxD < 0.1:
            self.__maxD = 0.1
            self.ui.doubleSpinBox_max_D.setValue(0.1)
        if self.__maxD >= 100:
            self.ui.doubleSpinBox_D.setDecimals(0)
            self.ui.doubleSpinBox_D.setSingleStep(1)
        elif self.__maxD >= 10:
            self.ui.doubleSpinBox_D.setDecimals(1)
            self.ui.doubleSpinBox_D.setSingleStep(0.1)
        elif self.__maxD >= 1:
            self.ui.doubleSpinBox_D.setDecimals(2)
            self.ui.doubleSpinBox_D.setSingleStep(0.01)
        else:
            self.ui.doubleSpinBox_D.setDecimals(3)
            self.ui.doubleSpinBox_D.setSingleStep(0.001)
        # self.ui.doubleSpinBox_D.setValue(self.ui.verticalSlider_D.value() * self.__maxD / 100)

    def change_p_para_display(self,para):
        self.ui.doubleSpinBox_P.setValue(para*self.__maxP/100)

    def change_i_para_display(self,para):
        self.ui.doubleSpinBox_I.setValue(para * self.__maxI / 100)

    def change_d_para_display(self,para):
        self.ui.doubleSpinBox_D.setValue(para * self.__maxD / 100)
        self.send_pid_para('d', para * self.__maxD / 100)

    def change_p_slider_value(self, value):
        if value > self.__maxP:
            value = self.__maxP
            self.ui.doubleSpinBox_P.setValue(value)
        self.send_pid_para('p', value)
        value = value * 100 / self.__maxP
        self.ui.verticalSlider_P.setValue(value)

    def change_i_slider_value(self, value):
        if value > self.__maxI:
            value = self.__maxI
            self.ui.doubleSpinBox_I.setValue(value)
        self.send_pid_para('i', value)
        value = value * 100 / self.__maxI
        self.ui.verticalSlider_I.setValue(value)

    def change_d_slider_value(self, value):
        if value > self.__maxD:
            value = self.__maxD
            self.ui.doubleSpinBox_D.setValue(value)
        self.send_pid_para('d', value)
        value = value * 100 / self.__maxD
        self.ui.verticalSlider_D.setValue(value)

    # cmd = ‘p' 'i' 'd'
    # sign = '-'/'+'
    # para_float --> para_8*4
    # sum = cmd + sign + para_8*4
    def send_pid_para(self, cmd, para):
        para_8 = struct.pack('f',para)      # float to byte
        send = bytearray(3)
        send[0] = ord('$')
        send[1] = ord(cmd)
        if cmd == 'p':
            if self.ui.checkBox_P.isChecked():
                send[2] = ord('-')
            else:
                send[2] = ord('+')
        elif cmd == 'i':
            if self.ui.checkBox_I.isChecked():
                send[2] = ord('-')
            else:
                send[2] = ord('+')
        elif cmd == 'd':
            if self.ui.checkBox_D.isChecked():
                send[2] = ord('-')
            else:
                send[2] = ord('+')
        # for i in range(len(para_8)):
        #     send[2+i] = para_8[i]
        send.extend(para_8)
        sum = 0
        for i in range(len(send)):
            sum += send[i]
        # print(sum|0xff)
        send.append(sum&0xff)
        # print(send.hex())
        # print(send)
        if not self.__uart2State:
            QToolTip.showText(QCursor.pos(), "请打开串口")
        else:
            self.__serialPort2.write(send)

    def which_channel_show(self):
        num = []
        if self.ui.checkBox_1.isChecked():
            num.append(1)
        if self.ui.checkBox_2.isChecked():
            num.append(2)
        if self.ui.checkBox_3.isChecked():
            num.append(3)
        if self.ui.checkBox_4.isChecked():
            num.append(4)
        if self.ui.checkBox_5.isChecked():
            num.append(5)
        if self.ui.checkBox_6.isChecked():
            num.append(6)
        return num

    def plot_random_data(self, checked):
        if checked:
            # if 1 in self.which_channel_show():
            #     self.__curveDataS.start_random_plot(1)
            if len(self.which_channel_show()) > 0:
                self.__curveChart.start_random_plot(self.which_channel_show()[0])
            else:
                self.__curveChart.start_random_plot(0)
        else:
            self.__curveChart.stop_random_plot()

    def add_plot_data(self, data, num):
        # start = time.time()
        # print('add_plot_data_start', start)
        # print(1, data, num)
        data = round(data,3)
        if num == 0:
            self.ui.lineEdit_7.setText(str(data))
        elif num ==1:
            self.ui.lineEdit_8.setText(str(data))
        elif num ==2:
            self.ui.lineEdit_9.setText(str(data))
        elif num ==3:
            self.ui.lineEdit_10.setText(str(data))
        elif num ==4:
            self.ui.lineEdit_11.setText(str(data))
        elif num ==5:
            self.ui.lineEdit_12.setText(str(data))
        if num+1 in self.which_channel_show():
            # print(2, data, num)
            self.__curveChart.add_data(data,num)
        else:
            self.__curveChart.clear_data(num)
        # end = time.time()
        # print('add_plot_data_time',end - start)

