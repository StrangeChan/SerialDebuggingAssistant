from PyQt5.QtSerialPort import QSerialPort
from PyQt5.QtCore import *
import struct


class Receive(QObject):
    receive_success = pyqtSignal(int,float)
    def __init__(self, uart):
        super().__init__()
        self.__serialPort = uart
        self.__data = bytearray()
        self.__count = 0
        self.__receiveDataNum = 0
        self.__receiveStartFlag = False

    # start num float ...
    # start '$'
    # num 通道数
    # float 4个字节*num
    def receive_uart_data(self):
        if self.__serialPort.isReadable():
            data = bytearray()
            data.extend(self.__serialPort.readAll())
            print(data.hex())
            if len(data) > 0:
                for i in range(len(data)):
                    # 第一次收到 $
                    if data[i] == ord('$') and (not self.__receiveStartFlag):
                        self.__receiveStartFlag = True

                    if self.__receiveStartFlag:
                        self.__data.append(data[i])
                        if len(self.__data) == 2:
                            # 判断第二位
                            if self.__data[1] > 7 or self.__data[1] <1:
                                # 第二位不对，接收失败
                                self.receive_fail()
                                break
                            else:
                                self.__receiveDataNum = self.__data[1]

                        if len(self.__data) == self.__receiveDataNum*4+2:
                            self.data_processing()
                        if len(self.__data) > self.__receiveDataNum*4+2:
                            self.receive_fail()

    def data_processing(self):
        self.__data.pop(0)
        self.__data.pop(0)
        for i in range(self.__receiveDataNum):
            data_float = struct.unpack('<f', bytes(self.__data[i*4:4+i*4]))
            print(data_float)
            self.receive_success.emit(i+1,data_float[0])
        # data_float = struct.unpack('>f', bytes(self.__data))
        # print(data_float)
        self.__receiveStartFlag = False
        self.__data.clear()
        self.__receiveDataNum = 0
        print('success')

    def receive_fail(self):
        self.__receiveStartFlag = False
        self.__data.clear()
        self.__receiveDataNum = 0
        print('fail')

