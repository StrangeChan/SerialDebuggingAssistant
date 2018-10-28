from PyQt5.QtSerialPort import QSerialPort
from PyQt5 import QtCore

class Receive(QtCore.QObject):
    def __init__(self, uart):
        super().__init__()
        pass

    def receive_uart_data(self):
        pass