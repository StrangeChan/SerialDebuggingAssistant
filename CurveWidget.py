# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtCore import QMargins
from PyQt5.QtGui import QPen,QPainter
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
import threading
import time
import random
from PyQt5.QtChart import QChart, QChartView, QLineSeries,QValueAxis,QAbstractAxis

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
        self.__xlimMin = 0
        # self.ax.legend()
        self.ax.set_ylim(self.__yMin, self.__yMax)
        self.change_xlim_max(self.get_xlim_max())
        self.fig.canvas.mpl_connect('resize_event', self.resize_fig)
        # self.ax.set_xticks([])
        self.ax.grid(linestyle='--')

        self.curveObj = [None] * 7  # draw object
        # print(len(self.curveObj))

    def change_ylim(self, _min, _max):
        self.ax.set_ylim(_min, _max)

    def mouse_pressed(self, e):
        self.__isMousePress = True
        self.__data_y = e.ydata
        # print(self.__data_y)
        self.setCursor(Qt.ClosedHandCursor)

    def mouse_released(self, e):
        pass
        # self.__isMouseRelease = True
        # self.__isMousePress = False

    # 通过鼠标移动图像
    def mouse_move_fig(self, e):
        if self.__isMousePress and (e.ydata is not None) and (self.__data_y is not None):
            ylim = self.ax.get_ylim()
            # print(ylim[0],ylim[1],e.ydata,self.__data_y)
            self.ax.set_ylim(ylim[0]-e.ydata+self.__data_y, ylim[1]-e.ydata+self.__data_y)
            self.draw()
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
            self.draw()
        # self.__widget.setCursor(Qt.ArrowCursor)

    # 获取当前窗口大小对应X坐标最大值
    def get_xlim_max(self):
        return self.fig.get_size_inches()[0] * self.__xlimFigSizeRadio

    def set_xlim_min(self, x_min = 0):
        self.__xlimMin = x_min
        # print(self.__xlimMin)

    def change_xlim_max(self, max):
        self.ax.set_xlim(self.__xlimMin,self.__xlimMin + max)

    # slot 与滑动条连接  滑动条（-50~50）
    def change_the_radio(self, _int):
        print(_int)
        if _int > 0:
            self.__xlimFigSizeRadio = 200 *1.2**_int
        elif _int < 0:
            _int = -_int
            self.__xlimFigSizeRadio = 200/(1.2**_int)
        self.change_xlim_max(self.get_xlim_max())
        self.draw()


    # x坐标范围随窗口变化而变化，使间距相等
    def resize_fig(self,e):
        # print(e.width)
        self.change_xlim_max(self.get_xlim_max())

    def plot(self, dataX, dataY, index = 0):
        print('draw_start', time.time())
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
        self.change_xlim_max(self.get_xlim_max())
        self.draw()
        print('draw_end', time.time())


class CurveDataS(QObject):
    plot_data = pyqtSignal(list,list,int)
    def __init__(self,curve, num_channel = 7):
        super().__init__()
        self.Id = 0
        self.curve = curve
        self.count_x = 0
        self.__is_x_max = False
        self.__timerID = 0
        self.__numChannel = num_channel
        self.dataX = [[],[],[],[],[],[],[]]
        self.dataY = [[],[],[],[],[],[],[]]
        self.isRun = False
        self.__startTime = 0
        # 虚拟波形生成标志
        self.generating = False
        self.exit = False
        self.isRandomRun = False
        self.__randomPlotChannel = 0

    def init_random_data_generator(self):
        self.exit = False
        self.isRandomRun = False
        self.tData = threading.Thread(name="dataGenerator", target=self.generate_data)
        self.tData.start()
        self.isRandomRun = True

    def start_random_plot(self, num = 0):
        if not self.isRandomRun:
            self.init_random_data_generator()
        if not self.isRun:
            self.generating = True
            self.__randomPlotChannel = num
            # 数据生成开始时间  并设置图像坐标最小值
            self.__startTime = time.time()*200
            # print(self.__startTime)
            self.curve.set_xlim_min(self.__startTime)
            # self.__timerID = self.startTimer(10)
        # self.tData.start()

    def pause_random_plot(self):
        self.generating = False
        # self.killTimer(self.__timerID)
        self.dataX[0] = []
        self.dataY[0] = []
        self.plot_data.emit(self.dataX[0], self.dataY[0], self.__randomPlotChannel)

    def release_random_plot(self):
        self.exit = True
        if self.generating:
            self.pause_random_plot()
        self.tData.join()
        self.isRandomRun = False
        # print(self.tData.run())

    def add_random_data(self, data):
        self.dataY[0].append(data)
        now_time = time.time()*200
        self.dataX[0].append(now_time)
        # 时间超出显示范围
        if now_time - self.curve.get_xlim_max() >= self.__startTime:
            self.curve.set_xlim_min(now_time - self.curve.get_xlim_max())
            self.__startTime = now_time - self.curve.get_xlim_max()
            # self.curve.change_xlim_max(self.get_xlim_max())
            self.dataY[0].pop(0)
            self.dataX[0].pop(0)
        self.plot_data.emit(self.dataX[0], self.dataY[0], self.__randomPlotChannel)

    def start_plot(self):
       #  关闭随机数生成
        if self.isRandomRun:
            self.release_random_plot()
        self.isRun = True
        for i in range(7):
            self.plot_data.emit([], [], i)
        # 数据生成开始时间  并设置图像坐标最小值
        self.__startTime = time.time() * 200
        print(self.__startTime)
        self.curve.set_xlim_min(self.__startTime)
        # self.__timerID = self.startTimer(5)

    def stop_plot(self):
        if self.isRun:
            # self.killTimer(self.__timerID)
            self.dataX = [[],[],[],[],[],[],[]]
            self.dataY = [[],[],[],[],[],[],[]]
            self.isRun = False
        if self.isRandomRun:
            self.release_random_plot()


    def add_data(self, data, num):
        start = time.time()
        print('add_start', time.time())
        self.dataY[num].append(data)
        now_time = time.time() * 200
        self.dataX[num].append(now_time)
        # 时间超出显示范围
        if now_time - self.curve.get_xlim_max() >= self.__startTime:
            self.curve.set_xlim_min(now_time - self.curve.get_xlim_max())
            self.__startTime = now_time - self.curve.get_xlim_max()
            # self.curve.change_xlim_max(self.get_xlim_max())
            if self.dataX[num][0] < self.__startTime:
                self.dataY[num].pop(0)
                self.dataX[num].pop(0)
        end = time.time()
        self.plot_data.emit(self.dataX[num], self.dataY[num], num)

        print('add_data_time', end - start)

    # 移动曲线图像实现动态
    def timerEvent(self, e):
        if self.__timerID == e.timerId():
            if self.count_x >= self.curve.get_xlim_max():
                # 图像超出边界
                self.__is_x_max = True
                for i in range(len(self.dataX)):
                    if len(self.dataX[i]) > 0:
                        # 从头部将超出边界的去掉，实现曲线滚动
                        for j in range(len(self.dataX[i])):
                            self.dataX[i][j] = \
                                self.dataX[i][j] + self.curve.get_xlim_max() - self.count_x - 1
                        while self.dataX[i][0] < 0:
                            self.dataX[i].pop(0)
                            self.dataY[i].pop(0)
                self.count_x = int(self.curve.get_xlim_max())
            else:
                self.count_x += 1

    def generate_data(self):
        while True:
            if self.exit:
                break
            if self.generating:
                new_data = random.randint(Y_MIN, Y_MAX)
                self.add_random_data(new_data)
                # self.add_data(new_data,self.__randomPlotChannel)
                # self.add_data(new_data+69, self.__randomPlotChannel+1)
                time.sleep(INTERVAL)


class CurveChart(QChart):
    def __init__(self, parent = None):
        super().__init__(parent)
        # 7个显示通道
        self.__series = []
        for i in range(7):
            self.__series.append(QLineSeries())
            self.addSeries(self.__series[i])
        # 轴
        self.__axis = QValueAxis()
        self.createDefaultAxes()
        # 轴和series关联
        for i in range(7):
            self.setAxisX(self.__axis, self.__series[i])
        # 刻度数量
        self.__axis.setTickCount(2)
        self.axisY().setTickCount(5)
        self.axisY().setMinorTickCount(2)
        self.axisY().setLabelFormat("%d")
        # self.setAnimationOptions(QChart.GridAxisAnimations)
        # 设置边缘空白
        self.setContentsMargins(-10,-20,-20,-30)
        # 坐标刻度设置
        self.__yMax = 100
        self.__yMin = -100
        self.__yAxisAdjust = 1.1  # 滚轮调整Y轴限制变化率
        self.__isMousePress = False  # 鼠标是否按下
        self.__data_y = 0  # 按下鼠标时Y坐标
        self.axisY().setRange(self.__yMin,self.__yMax)
        self.__xAxisFigSizeRadio = 2      # x轴坐标范围和图像宽度比值
        self.__xAxisMin = 0
        self.axisX().setRange(self.__xAxisMin,100)#self.get_plot_area_width())

        # print(self.get_plot_area_width())

    def get_plot_area_width(self):
        return self.plotArea().width()*self.__xAxisFigSizeRadio

    def change_the_radio(self, _int):
        print(_int)
        if _int > 0:
            self.__xAxisFigSizeRadio = 2 *1.1**_int
        elif _int < 0:
            _int = -_int
            self.__xAxisFigSizeRadio = 2/(1.1**_int)
        self.axisX().setRange(self.__xAxisMin, self.get_plot_area_width())

    def resizeEvent(self, e):
        self.axisX().setRange(self.__xAxisMin, self.get_plot_area_width())

    def wheelEvent(self, e):
        # print(e.delta(),e.pos().y(),self.plotArea().height(),self.rect().height())
        # 计算当前鼠标坐标
        _y = self.axisY().max() - \
             (e.pos().y()-self.plotArea().y())/self.plotArea().height()*(self.__yMax-self.__yMin)
        if e.delta() > 0:
            self.__yMax = self.__yMax / self.__yAxisAdjust
            self.__yMin = self.__yMin / self.__yAxisAdjust
        else:
            self.__yMax,self.__yMin = \
                self.__yMax * self.__yAxisAdjust,self.__yMin * self.__yAxisAdjust
        print(self.__yMax,self.__yMin)
        self.axisY().setRange(self.__yMin+_y, self.__yMax+_y)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            print(e.button())
            if e.pos().y()>self.plotArea().y() and e.pos().y()<self.plotArea().bottom():
                self.__isMousePress = True
                self.__data_y = e.pos().y()
                print(2)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            if e.pos().y()>self.plotArea().y() and e.pos().y()<self.plotArea().bottom():
                self.__isMousePress = True
                # self.__data_y = e.pos().y()
                self.scroll(0,e.pos().y()-self.__data_y)
                print(1,e.pos().y())

