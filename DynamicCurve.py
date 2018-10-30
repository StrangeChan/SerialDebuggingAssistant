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


X_MINUTES = 1
Y_MAX = 100
Y_MIN = 1
INTERVAL = 1
MAX_COUNTER = int(X_MINUTES * 60 / INTERVAL)


class CurveFigure(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        #ax = axis  轴
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.ax.set_xlabel("time of data generator")
        self.ax.set_ylabel('random data value')
       # self.ax.legend()
        self.ax.set_ylim(Y_MIN, Y_MAX)
        # 设置间隔
        self.ax.xaxis.set_major_locator(MinuteLocator())  # every minute is a major locator
        self.ax.xaxis.set_minor_locator(SecondLocator([10, 20, 30, 40, 50]))  # every 10 second is a minor locator
        self.ax.xaxis.set_major_formatter(DateFormatter('%H:%M:%S'))  # tick label formatter
        self.curveObj = None  # draw object

    def plot(self, datax, datay):
        if self.curveObj is None:
            # create draw object once
            self.curveObj, = self.ax.plot_date(np.array(datax), np.array(datay), 'bo-')
        else:
            # update data of draw object
            self.curveObj.set_data(np.array(datax), np.array(datay))
            # update limit of X axis,to make sure it can move
            self.ax.set_xlim(datax[0], datax[-1])
        ticklabels = self.ax.xaxis.get_ticklabels()
        for tick in ticklabels:
            tick.set_rotation(25)
        self.draw()

class CurveWidget(QWidget):
    def __init__(self,parent = None):
        super().__init__()
        self.__curve = CurveFigure()
        # 一个布局
        self.__vbLayout = QtWidgets.QVBoxLayout()
        # 工具栏
        self.__nToolBar = NavigationToolbar(self.__curve, parent)
        #self.__nToolBar.configure_subplots()
        self.__vbLayout.addWidget(self.__nToolBar)
        self.__vbLayout.addWidget(self.__curve)
        self.setLayout(self.__vbLayout)
        self.dataX = []
        self.dataY = []

    def start_plot(self):
        self.__generating = True

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

    def generate_data(self):
        counter = 0
        while (True):
            if self.__exit:
                break
            if self.__generating:
                newData = random.randint(Y_MIN, Y_MAX)
                newTime = date2num(datetime.now())

                self.dataX.append(newTime)
                self.dataY.append(newData)

                self.canvas.plot(self.dataX, self.dataY)

                if counter >= MAX_COUNTER:
                    self.dataX.pop(0)
                    self.dataY.pop(0)
                else:
                    counter += 1
            time.sleep(INTERVAL)

