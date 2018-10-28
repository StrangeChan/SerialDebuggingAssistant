# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwidow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(60, 20, 271, 144))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_25 = QtWidgets.QLabel(self.layoutWidget)
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 3)
        self.label_26 = QtWidgets.QLabel(self.layoutWidget)
        self.label_26.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_26.setObjectName("label_26")
        self.gridLayout.addWidget(self.label_26, 1, 0, 1, 1)
        self.comboBox_com = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_com.setObjectName("comboBox_com")
        self.gridLayout.addWidget(self.comboBox_com, 1, 1, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.layoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 2, 0, 1, 1)
        self.comboBox_baud = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.gridLayout.addWidget(self.comboBox_baud, 2, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.layoutWidget)
        self.label_28.setStyleSheet("background:rgb(85, 170, 255)")
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 3, 0, 1, 1)
        self.pushButton_uart_rfresh = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_uart_rfresh.sizePolicy().hasHeightForWidth())
        self.pushButton_uart_rfresh.setSizePolicy(sizePolicy)
        self.pushButton_uart_rfresh.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_uart_rfresh.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_uart_rfresh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_uart_rfresh.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_uart_rfresh.setObjectName("pushButton_uart_rfresh")
        self.gridLayout.addWidget(self.pushButton_uart_rfresh, 3, 1, 1, 1)
        self.pushButton_uart_sw = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_uart_sw.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_uart_sw.setObjectName("pushButton_uart_sw")
        self.gridLayout.addWidget(self.pushButton_uart_sw, 3, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口调试助手"))
        self.label_25.setText(_translate("MainWindow", "串口通讯"))
        self.label_26.setText(_translate("MainWindow", "选择"))
        self.label_27.setText(_translate("MainWindow", "波特率"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "115200"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(2, _translate("MainWindow", "38400"))
        self.label_28.setText(_translate("MainWindow", "操作"))
        self.pushButton_uart_rfresh.setText(_translate("MainWindow", "刷新"))
        self.pushButton_uart_sw.setText(_translate("MainWindow", "打开串口"))

