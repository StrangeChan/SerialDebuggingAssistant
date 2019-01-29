import sys
from PyQt5 import QtWidgets
from MainWindow import MainWindow
from QCandyUi import CandyWindow

# if __name__ == '__main__':
app = QtWidgets.QApplication(sys.argv)
widget = MainWindow()
widget = CandyWindow.createWindow(widget, 'blueDeep',"串口调试助手",'1.ico')
widget.show()
sys.exit(app.exec_())