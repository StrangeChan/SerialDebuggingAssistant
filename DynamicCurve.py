# -*- coding: utf-8 -*-

from PyQt5 import QtGui,QtWidgets
from PyQt5.QtWidgets import QWidget,QMainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
from array import array
from matplotlib.dates import date2num, MinuteLocator, SecondLocator, DateFormatter
import threading
import time
import random
from datetime import datetime

'''
添加一个滑动条控制x轴坐标最大值，即分辨率

开一个定时器5ms一次 count_x ++  is_x_max = 0
count最大后，设一标志位is_x_max = 1，count = 0 ,self.dataY.pop（0）

串口接收完成后self.dataY.append(newData) self.dataX.append(count_x) 
is_x_max = 1   self.dataX 不变
'''
X_MINUTES = 1
Y_MAX = 100
Y_MIN = -100
INTERVAL = 0.1
MAX_COUNTER = 100#int(X_MINUTES * 60 / INTERVAL)


class CurveFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.fig.get_size_inches()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.set_tight_layout(True)
       # self.ax.set_xlabel("time of data generator")
       # self.ax.set_ylabel('random data value')
       # self.ax.legend()
        self.ax.set_ylim(Y_MIN, Y_MAX)
        self.ax.set_xlim(0, MAX_COUNTER)
        # 设置间隔
        #self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        #self.ax.xaxis.set_minor_locator(SecondLocator([10, 20, 30, 40, 50]))  # every 10 second is a minor locator
        #self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter

        self.curveObj = None  # draw object

    def change_xlim(self,max):
        self.ax.set_xlim(0, max)

    def plot(self, datax, datay):
        if self.curveObj is None:
            # create draw object once
            #self.curveObj, = self.ax.plot_date(np.array(datax), np.array(datay), 'bo-')
            self.curveObj, = self.ax.plot(np.array(datax), np.array(datay), 'b-')
        else:
            # update data of draw object
            self.curveObj.set_data(np.array(datax), np.array(datay))
            #print(type(self.curveObj))
            # update limit of X axis,to make sure it can move
            #self.ax.set_xlim(datax[0], datax[-1])
            self.ax.set_xlim(0, self.fig.get_size_inches()[1]*200)
        ticklabels = self.ax.xaxis.get_ticklabels()
        #for tick in ticklabels:
        #    tick.set_rotation(25)
        self.draw()
        #print(self.fig.get_size_inches())

class CurveWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.curve = CurveFigure()
        # 一个布局
        self.__vbLayout = QtWidgets.QVBoxLayout()
        # 工具栏
       # self.__nToolBar = NavigationToolbar(self.curve, parent)
       # self.__vbLayout.addWidget(self.__nToolBar)
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
        pass

    def timerEvent(self,e):
        if self.__timerID == e.timerId():
            if self.count_x >= self.curve.fig.get_size_inches()[1]*200:
                self.__is_x_max = True
                if len(self.dataX)>0:
                    for i in range(len(self.dataX)):
                        self.dataX[i] -= 1
                    if self.dataX[0] < 0:
                        self.dataX.pop(0)
                        self.dataY.pop(0)
            else:
                self.count_x += 1

    def generate_data(self):
        counter = 0
        while (True):
            if self.__exit:
                break
            if self.__generating:
                newData = random.randint(Y_MIN, Y_MAX)
               # newTime = date2num(datetime.now())

                #self.dataX.append(newTime)

                '''
                self.__curve.plot(self.dataX, self.dataY)

                if counter >= self.__curve.fig.get_size_inches()[1]*200:
                    #self.dataX.pop(0)
                    self.dataY.append(newData)
                    self.dataY.pop(0)
                else:
                    self.dataX.append(counter)
                    self.dataY.append(newData)
                    counter += 1
                '''
                if self.__is_x_max:
                    self.dataY.append(newData)
                    #self.dataY.pop(0)
                    self.dataX.append(self.count_x)
                else:
                    self.dataX.append(self.count_x)
                    self.dataY.append(newData)

                self.curve.plot(self.dataX, self.dataY)

            time.sleep(INTERVAL)

