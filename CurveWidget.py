# -*- coding: utf-8 -*-

from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import threading
import time
import random

X_MINUTES = 1
Y_MAX = 100
Y_MIN = -100
INTERVAL = 0.1
MAX_COUNTER = 100  # int(X_MINUTES * 60 / INTERVAL)


class CurveWidget(FigureCanvas):

    def __init__(self, widget):

        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        # FigureCanvas.setSizePolicy(self,QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.fig.set_tight_layout('true')
        self.__widget = widget
        # self.__widget.setCursor(Qt.CrossCursor)
        self.__yMax = 100
        self.__yMin = -100
        self.__ylimAdjust = 1.1         # 滚轮调整Y轴限制变化率
        self.__isMousePress = False     # 鼠标是否按下
        self.__data_y = 0    # 按下鼠标时Y坐标
        self.fig.canvas.mpl_connect('scroll_event', self.scroll_change_ylim)
        self.fig.canvas.mpl_connect('button_press_event', self.mouse_pressed)
        self.fig.canvas.mpl_connect('button_release_event', self.mouse_move_fig)

        self.__xlimFigSizeRadio = 200
        # self.ax.legend()
        self.ax.set_ylim(self.__yMin, self.__yMax)
        self.change_xlim_max(self.get_xlim_max())
        self.fig.canvas.mpl_connect('resize_event', self.resize_fig)
        self.ax.set_xticks([])

        self.curveObj = [None] * 7  # draw object
        # print(len(self.curveObj))

    def change_ylim(self, _min, _max):
        self.ax.set_ylim(_min, _max)

    def mouse_pressed(self, e):
        self.__isMousePress = True
        self.__data_y = e.ydata
        self.setCursor(Qt.ClosedHandCursor)

    def mouse_released(self, e):
        pass
        # self.__isMouseRelease = True
        # self.__isMousePress = False

    # 通过鼠标移动图像
    def mouse_move_fig(self, e):
        if self.__isMousePress and e.ydata is not None and self.__data_y is not None:
            ylim = self.ax.get_ylim()
            # print(ylim[0],ylim[1],e.ydata,self.__data_y)
            self.ax.set_ylim(ylim[0]-e.ydata+self.__data_y, ylim[1]-e.ydata+self.__data_y)
            self.__isMousePress = False
        self.setCursor(Qt.ArrowCursor)

    # 滚轮改变Y轴坐标
    def scroll_change_ylim(self, e):
        if e.step > 0:
            self.__yMax = self.__yMax / self.__ylimAdjust
            self.__yMin = self.__yMin / self.__ylimAdjust
        else:
            self.__yMax,self.__yMin = self.__yMax * self.__ylimAdjust,self.__yMin * self.__ylimAdjust
        if e.ydata != None:
            self.ax.set_ylim(e.ydata+self.__yMin, e.ydata+self.__yMax)
        # self.__widget.setCursor(Qt.ArrowCursor)

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
        self.draw()

    # x坐标范围随窗口变化而变化，使间距相等
    def resize_fig(self,e):
        # print(e.width)
        self.change_xlim_max(self.get_xlim_max())

    def plot(self, dataX, dataY, index = 0):
        if index == 0:
            color = 'b--'
        elif index == 1:
            color = 'r'
        elif index == 2:
            color = 'g'
        elif index == 3:
            color = 'b'
        elif index == 4:
            color = 'y'
        elif index == 5:
            color = 'm'
        elif index == 6:
            color = 'c'

        if self.curveObj[index] is None:
            # create draw object once
            self.curveObj[index], = self.ax.plot(np.array(dataX), np.array(dataY), color)
        else:
            self.curveObj[index].set_data(np.array(dataX), np.array(dataY))
        #self.change_xlim_max(self.get_xlim_max())
        self.draw()

class CurveData(QObject):
    plot_data = pyqtSignal(list,list,int)
    def __init__(self,curve):
        super().__init__()
        self.Id = 0
        self.curve = curve
        self.count_x = 0
        self.__is_x_max = False
        self.generating = False
        self.exit = False
        self.isRun = False
        self.__timerID = 0
        self.dataX = []
        self.dataY = []  # [[],[],[],[],[],[]]
        self.data = [[]]*7
        # print(len(self.data))
        # print(len(self.data))

    def init_data_generator(self):
        self.exit = False
        self.isRun = False
        self.tData = threading.Thread(name="dataGenerator", target=self.generate_data)
        self.tData.start()
        self.isRun = True

    def start_plot(self):
        if not self.isRun:
            self.init_data_generator()
        self.generating = True
        self.__timerID = self.startTimer(10)
        # self.tData.start()

    def pause_plot(self):
        self.generating = False
        self.killTimer(self.__timerID)
        self.dataX = []
        self.dataY = []
        self.data[0] = []
        self.count_x = 0
        self.plot_data.emit(self.dataX, self.dataY, self.Id)

    def release_plot(self):
        self.exit = True
        if self.generating:
            self.pause_plot()
        self.tData.join()
        self.isRun = False
        # print(self.tData.run())

    def add_data(self, data, num=None):
        self.dataY.append(data)
        self.dataX.append(self.count_x)
        # self.data[num].append([self.count_x, data])
        # dataX,dataY = [], []
        # for i in range(len(self.data[num])):
        #     dataX.append(self.data[num][i][0])
        #     dataY.append(self.data[num][i][1])
        if num is None:
            self.plot_data.emit(self.dataX, self.dataY, self.Id)
        else:
            self.plot_data.emit(self.dataX, self.dataY, num)

    # 移动曲线图像实现动态
    def timerEvent(self, e):
        if self.__timerID == e.timerId():
            if self.count_x >= self.curve.get_xlim_max():
                # 图像超出边界
                self.__is_x_max = True
                if len(self.dataX) > 0:
                    # 从头部将超出边界的去掉，实现曲线滚动
                    for i in range(len(self.dataX)):
                        self.dataX[i] = self.dataX[i] + self.curve.get_xlim_max() - self.count_x - 1
                    while self.dataX[0] < 0:
                        self.dataX.pop(0)
                        self.dataY.pop(0)
                        self.count_x = self.curve.get_xlim_max()
                # for i in range(len(self.data)):
                    # print(i)
                    # for j in range(len(self.data[i])):
                    #     self.data[i][j][0] = self.data[i][j][0] + self.curve.get_xlim_max() - self.count_x - 1

                    # while self.data[i][0][0]<0:
                    #     self.data[i].pop(0)
            else:
                self.count_x += 1

    def generate_data(self):
        while True:
            if self.exit:
                break
            if self.generating:
                new_data = random.randint(Y_MIN, Y_MAX)
                self.add_data(new_data)
                time.sleep(INTERVAL)
                # if self.__is_x_max:
                # self.dataY.append(newData)
                # self.dataX.append(self.count_x)
                # else:
                #     self.dataX.append(self.count_x)
                #     self.dataY.append(newData)
                # self.data.append([self.count_x,newData])
                # self.dataX, self.dataY = [],[]
                # for i in range(len(self.data)) :
                #     self.dataX.append(self.data[i][0])
                #     self.dataY.append( self.data[i][1])
                #
                # self.plot_data.emit(self.dataX, self.dataY,1)

                # self.add_data(newData+4,4)
                # self.plot_data.emit(self.dataX, self.dataY, 'b--')
                # self.curve.plot(self.dataX, self.dataY)

