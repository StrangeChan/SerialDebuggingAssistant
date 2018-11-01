# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from array import array
from matplotlib.dates import date2num, MinuteLocator, SecondLocator, DateFormatter
import threading
import time
import random
from datetime import datetime

'''
x轴坐标最大值由窗口大小控制
开一个定时器5ms一次 count_x ++  is_x_max = 0
添加一个滑动条控制x轴坐标最大值与窗口的倍数达到控制采样率的效果
count_x最大后，设一标志位is_x_max = 1，count = 0 ,self.dataY.pop（0）

串口接收完成后self.dataY.append(newData) self.dataX.append(count_x) 
is_x_max = 1   self.dataX 不变
'''
X_MINUTES = 1
Y_MAX = 100
Y_MIN = -100
INTERVAL = 0.1
MAX_COUNTER = 100 #int(X_MINUTES * 60 / INTERVAL)


class CurveFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.fig.set_tight_layout(True)

        self.__xlimFigSizeRadio = 200
       # self.ax.legend()
        self.ax.set_ylim(Y_MIN, Y_MAX)
        self.ax.set_xlim(0, MAX_COUNTER)

        self.curveObj = None  # draw object

    def change_ylim(self,min,max):
        self.ax.set_ylim(min, max)

    # 获取当前窗口大小对应X坐标最大值
    def get_xlim_max(self):
        return self.fig.get_size_inches()[0] * self.__xlimFigSizeRadio

    def change_xlim_max(self,max):
        self.ax.set_xlim(0,max)

    # slot 与滑动条连接  滑动条（-50~50）
    def change_the_radio(self,int):
        if int > 0:
            self.__xlimFigSizeRadio = 200 * int
        elif int < 0:
            int = -int
            self.__xlimFigSizeRadio = 200/int
        self.change_xlim_max(self.get_xlim_max())

    def plot(self, dataX, dataY):
        if self.curveObj is None:
            # create draw object once
            self.curveObj, = self.ax.plot(np.array(dataX), np.array(dataY), 'b-')
        else:
            self.curveObj.set_data(np.array(dataX), np.array(dataY))

        self.draw()



class CurveWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.curve = CurveFigure()
        # 一个布局
        self.__vbLayout = QtWidgets.QVBoxLayout()
        self.__vbLayout.addWidget(self.curve)
        self.setLayout(self.__vbLayout)

        self.count_x = 0
        self.__is_x_max = False

        self.dataX = []
        self.dataY = []

        self.init_data_generator()
        self.start_plot()

    def start_plot(self):
        self.__generating = True
        self.__timerID = self.startTimer(10)

    def pause_plot(self):
        self.__generating = False

    def init_data_generator(self):
        self.__generating = False
        self.__exit = False

        self.tData = threading.Thread(name="dataGenerator", target=self.generate_data)
        self.tData.start()

    def release_plot(self):
        self.__exit = True
        self.tData.join()

    def add_data(self,data):
        if self.__is_x_max:
            self.dataY.append(data)
            # self.dataY.pop(0)
            self.dataX.append(self.count_x)
        else:
            self.dataX.append(self.count_x)
            self.dataY.append(data)

        self.curve.plot(self.dataX, self.dataY)

    # 移动曲线图像实现动态
    def timerEvent(self,e):
        if self.__timerID == e.timerId():
            if self.count_x >= self.curve.get_xlim_max():
                # 图像超出边界
                self.__is_x_max = True
                if len(self.dataX)>0:
                   # 从头部将超出边界的去掉，实现曲线滚动
                    for i in range(len(self.dataX)):
                        self.dataX[i] = self.dataX[i] + self.curve.get_xlim_max() - self.count_x - 1
                    while self.dataX[0] < 0:
                        self.dataX.pop(0)
                        self.dataY.pop(0)
                    self.count_x = self.curve.get_xlim_max()
            else:
                self.count_x += 1

    # 重置图像大小
    def resizeEvent(self, e):
        self.curve.change_xlim_max(self.curve.get_xlim_max())

    def generate_data(self):
        counter = 0
        while (True):
            if self.__exit:
                break
            if self.__generating:
                newData = random.randint(Y_MIN, Y_MAX)

                if self.__is_x_max:
                    self.dataY.append(newData)
                    #self.dataY.pop(0)
                    self.dataX.append(self.count_x)
                else:
                    self.dataX.append(self.count_x)
                    self.dataY.append(newData)

                self.curve.plot(self.dataX, self.dataY)

            time.sleep(INTERVAL)

