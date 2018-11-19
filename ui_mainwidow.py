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
        MainWindow.resize(1289, 710)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setIconSize(QtCore.QSize(18, 18))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 1, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 0, 0, 1, 1)
        self.comboBox_baud = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_baud.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_baud, 1, 1, 1, 2)
        self.label_28 = QtWidgets.QLabel(self.groupBox)
        self.label_28.setStyleSheet("background:rgb(85, 170, 255);\n"
"border:1px solid gray;\n"
"        width:300px;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.label_28.setObjectName("label_28")
        self.gridLayout_2.addWidget(self.label_28, 2, 0, 1, 1)
        self.comboBox_com = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_com.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_com.setObjectName("comboBox_com")
        self.gridLayout_2.addWidget(self.comboBox_com, 0, 1, 1, 2)
        self.pushButton_uart_sw = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_uart_sw.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_uart_sw.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.pushButton_uart_sw.setObjectName("pushButton_uart_sw")
        self.gridLayout_2.addWidget(self.pushButton_uart_sw, 2, 2, 1, 1)
        self.pushButton_uart_rfresh = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_uart_rfresh.sizePolicy().hasHeightForWidth())
        self.pushButton_uart_rfresh.setSizePolicy(sizePolicy)
        self.pushButton_uart_rfresh.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_uart_rfresh.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_uart_rfresh.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_uart_rfresh.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.pushButton_uart_rfresh.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_uart_rfresh.setObjectName("pushButton_uart_rfresh")
        self.gridLayout_2.addWidget(self.pushButton_uart_rfresh, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.plainTextEdit_rx = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_rx.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_rx.setReadOnly(True)
        self.plainTextEdit_rx.setCenterOnScroll(True)
        self.plainTextEdit_rx.setObjectName("plainTextEdit_rx")
        self.gridLayout_4.addWidget(self.plainTextEdit_rx, 0, 1, 2, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_show_ascii = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_show_ascii.setMinimumSize(QtCore.QSize(0, 33))
        self.radioButton_show_ascii.setCheckable(True)
        self.radioButton_show_ascii.setChecked(True)
        self.radioButton_show_ascii.setAutoExclusive(True)
        self.radioButton_show_ascii.setObjectName("radioButton_show_ascii")
        self.gridLayout.addWidget(self.radioButton_show_ascii, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_save.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 0, 1, 1)
        self.radioButton_show_hex = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_show_hex.setMinimumSize(QtCore.QSize(0, 33))
        self.radioButton_show_hex.setChecked(False)
        self.radioButton_show_hex.setObjectName("radioButton_show_hex")
        self.gridLayout.addWidget(self.radioButton_show_hex, 0, 1, 1, 1)
        self.pushButton_clean = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_clean.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.gridLayout.addWidget(self.pushButton_clean, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.radioButton_tx_ascii = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_tx_ascii.setMinimumSize(QtCore.QSize(0, 33))
        self.radioButton_tx_ascii.setCheckable(True)
        self.radioButton_tx_ascii.setChecked(True)
        self.radioButton_tx_ascii.setAutoExclusive(True)
        self.radioButton_tx_ascii.setObjectName("radioButton_tx_ascii")
        self.gridLayout_3.addWidget(self.radioButton_tx_ascii, 0, 0, 1, 1)
        self.radioButton_tx_hex = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_tx_hex.setMinimumSize(QtCore.QSize(0, 33))
        self.radioButton_tx_hex.setChecked(False)
        self.radioButton_tx_hex.setObjectName("radioButton_tx_hex")
        self.gridLayout_3.addWidget(self.radioButton_tx_hex, 0, 1, 1, 1)
        self.pushButton_tx = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_tx.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_tx.setObjectName("pushButton_tx")
        self.gridLayout_3.addWidget(self.pushButton_tx, 1, 0, 1, 1)
        self.pushButton_clean_tx = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_clean_tx.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_clean_tx.setObjectName("pushButton_clean_tx")
        self.gridLayout_3.addWidget(self.pushButton_clean_tx, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.plainTextEdit_tx = QtWidgets.QPlainTextEdit(self.tab)
        self.plainTextEdit_tx.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.plainTextEdit_tx.setObjectName("plainTextEdit_tx")
        self.gridLayout_4.addWidget(self.plainTextEdit_tx, 2, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 4)
        self.gridLayout_4.setRowStretch(0, 3)
        self.gridLayout_4.setRowStretch(1, 2)
        self.gridLayout_4.setRowStretch(2, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setObjectName("label_29")
        self.gridLayout_5.addWidget(self.label_29, 1, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_4)
        self.label_30.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_30.setObjectName("label_30")
        self.gridLayout_5.addWidget(self.label_30, 0, 0, 1, 1)
        self.comboBox_baud_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_baud_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_baud_2.setObjectName("comboBox_baud_2")
        self.comboBox_baud_2.addItem("")
        self.comboBox_baud_2.addItem("")
        self.comboBox_baud_2.addItem("")
        self.gridLayout_5.addWidget(self.comboBox_baud_2, 1, 1, 1, 2)
        self.label_31 = QtWidgets.QLabel(self.groupBox_4)
        self.label_31.setStyleSheet("background:rgb(85, 170, 255);\n"
"border:1px solid gray;\n"
"        width:300px;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.label_31.setObjectName("label_31")
        self.gridLayout_5.addWidget(self.label_31, 2, 0, 1, 1)
        self.comboBox_com_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_com_2.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.comboBox_com_2.setObjectName("comboBox_com_2")
        self.gridLayout_5.addWidget(self.comboBox_com_2, 0, 1, 1, 2)
        self.pushButton_uart_sw_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_uart_sw_2.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_uart_sw_2.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.pushButton_uart_sw_2.setObjectName("pushButton_uart_sw_2")
        self.gridLayout_5.addWidget(self.pushButton_uart_sw_2, 2, 2, 1, 1)
        self.pushButton_uart_rfresh_2 = QtWidgets.QPushButton(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_uart_rfresh_2.sizePolicy().hasHeightForWidth())
        self.pushButton_uart_rfresh_2.setSizePolicy(sizePolicy)
        self.pushButton_uart_rfresh_2.setMinimumSize(QtCore.QSize(0, 33))
        self.pushButton_uart_rfresh_2.setBaseSize(QtCore.QSize(0, 0))
        self.pushButton_uart_rfresh_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_uart_rfresh_2.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.pushButton_uart_rfresh_2.setIconSize(QtCore.QSize(12, 12))
        self.pushButton_uart_rfresh_2.setObjectName("pushButton_uart_rfresh_2")
        self.gridLayout_5.addWidget(self.pushButton_uart_rfresh_2, 2, 1, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_1.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_1.setText("")
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_9.addWidget(self.checkBox_1, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_9.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_7.setStyleSheet("background:rgb(255, 0, 0);color:rgb(255, 255, 255)\n"
";border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_9.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_9)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_2.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_10.addWidget(self.checkBox_2, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_2.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_10.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_10.addItem(spacerItem1, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_8.setStyleSheet("background:rgb(0,255, 0);color:rgb(0,0,0);border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_10.addWidget(self.lineEdit_8, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_10)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_3.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_11.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_3.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_11.addWidget(self.lineEdit_3, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem2, 1, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_9.setStyleSheet("background:rgb(0, 0, 255);color:rgb(255, 255, 255);border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_11.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_11)
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_4.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout_12.addWidget(self.checkBox_4, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_4.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_12.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem3, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_10.setStyleSheet("background:rgb(255, 255, 0);color:rgb(0,0,0);border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_12.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_12)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_5.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout_13.addWidget(self.checkBox_5, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_5.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_13.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_13.addItem(spacerItem4, 1, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_11.setStyleSheet("background:rgb(255, 0, 255);color:rgb(0,0,0);border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_13.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_13)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem5 = QtWidgets.QSpacerItem(17, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem5, 1, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_6.setMaximumSize(QtCore.QSize(20, 20))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout_14.addWidget(self.checkBox_6, 0, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_12.setStyleSheet("background:rgb(0, 255, 255);color:rgb(0,0,0);border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_14.addWidget(self.lineEdit_12, 1, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_6.setStyleSheet("border:1px solid gray;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;\n"
"")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_14.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_14)
        self.gridLayout_15.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_15.addItem(spacerItem6, 1, 1, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox_6)
        self.horizontalSlider.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.horizontalSlider.setMinimum(-25)
        self.horizontalSlider.setMaximum(25)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setProperty("value", 0)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(1)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout_15.addWidget(self.horizontalSlider, 2, 0, 1, 2)
        self.checkBox_curve_show_random = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_curve_show_random.setObjectName("checkBox_curve_show_random")
        self.gridLayout_15.addWidget(self.checkBox_curve_show_random, 1, 0, 1, 1)
        self.gridLayout_15.setColumnStretch(0, 1)
        self.gridLayout_15.setRowStretch(0, 2)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.horizontalLayout_2.setStretch(0, 4)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.widget_dynamic_curve = QtWidgets.QWidget(self.tab_2)
        self.widget_dynamic_curve.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_dynamic_curve.setObjectName("widget_dynamic_curve")
        self.gridLayout_8.addWidget(self.widget_dynamic_curve, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_5)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("background:rgb(255, 0, 0);\n"
"border:1px solid gray;\n"
"        width:300px;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background:rgb(0, 255, 0);\n"
"border:1px solid gray;\n"
"        width:300px;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 2, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background:rgb(255, 255, 127);\n"
"border:1px solid gray;\n"
"        width:300px;\n"
"        border-radius:10px;\n"
"        padding:2px 4px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_6.addWidget(self.label_5, 0, 4, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_5)
        self.label_6.setObjectName("label_6")
        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)
        self.doubleSpinBox_max_P = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_max_P.setMinimumSize(QtCore.QSize(0, 20))
        self.doubleSpinBox_max_P.setDecimals(1)
        self.doubleSpinBox_max_P.setMinimum(0.0)
        self.doubleSpinBox_max_P.setObjectName("doubleSpinBox_max_P")
        self.gridLayout_6.addWidget(self.doubleSpinBox_max_P, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_5)
        self.label_7.setObjectName("label_7")
        self.gridLayout_6.addWidget(self.label_7, 1, 2, 1, 1)
        self.doubleSpinBox_max_I = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_max_I.setMinimumSize(QtCore.QSize(50, 20))
        self.doubleSpinBox_max_I.setDecimals(2)
        self.doubleSpinBox_max_I.setMaximum(100.0)
        self.doubleSpinBox_max_I.setSingleStep(0.1)
        self.doubleSpinBox_max_I.setObjectName("doubleSpinBox_max_I")
        self.gridLayout_6.addWidget(self.doubleSpinBox_max_I, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_5)
        self.label_8.setObjectName("label_8")
        self.gridLayout_6.addWidget(self.label_8, 1, 4, 1, 1)
        self.doubleSpinBox_max_D = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doubleSpinBox_max_D.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_max_D.setSizePolicy(sizePolicy)
        self.doubleSpinBox_max_D.setMinimumSize(QtCore.QSize(30, 20))
        self.doubleSpinBox_max_D.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.doubleSpinBox_max_D.setDecimals(2)
        self.doubleSpinBox_max_D.setMaximum(100.0)
        self.doubleSpinBox_max_D.setSingleStep(0.1)
        self.doubleSpinBox_max_D.setObjectName("doubleSpinBox_max_D")
        self.gridLayout_6.addWidget(self.doubleSpinBox_max_D, 1, 5, 1, 1)
        self.verticalSlider_P = QtWidgets.QSlider(self.groupBox_5)
        self.verticalSlider_P.setStyleSheet("handle:vertical{width:13;margin-top:-3;margin-bottom:-3;border-radius:6;background:qradialgradient(spread:pad,cx:0.5,cy:0.5,radius:0.5,fx:0.5,fy:0.5,stop:0.6 #FFFFFF,stop:0.8 #4c73a8);}\n"
"        ")
        self.verticalSlider_P.setMinimum(0)
        self.verticalSlider_P.setMaximum(100)
        self.verticalSlider_P.setPageStep(1)
        self.verticalSlider_P.setProperty("value", 0)
        self.verticalSlider_P.setSliderPosition(0)
        self.verticalSlider_P.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_P.setInvertedAppearance(False)
        self.verticalSlider_P.setObjectName("verticalSlider_P")
        self.gridLayout_6.addWidget(self.verticalSlider_P, 2, 0, 3, 1)
        self.doubleSpinBox_P = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_P.setMinimumSize(QtCore.QSize(0, 20))
        self.doubleSpinBox_P.setDecimals(2)
        self.doubleSpinBox_P.setMaximum(100.0)
        self.doubleSpinBox_P.setSingleStep(0.1)
        self.doubleSpinBox_P.setObjectName("doubleSpinBox_P")
        self.gridLayout_6.addWidget(self.doubleSpinBox_P, 2, 1, 1, 1)
        self.verticalSlider_I = QtWidgets.QSlider(self.groupBox_5)
        self.verticalSlider_I.setMinimum(0)
        self.verticalSlider_I.setMaximum(100)
        self.verticalSlider_I.setPageStep(1)
        self.verticalSlider_I.setProperty("value", 0)
        self.verticalSlider_I.setSliderPosition(0)
        self.verticalSlider_I.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_I.setInvertedAppearance(False)
        self.verticalSlider_I.setObjectName("verticalSlider_I")
        self.gridLayout_6.addWidget(self.verticalSlider_I, 2, 2, 3, 1)
        self.doubleSpinBox_I = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_I.setMinimumSize(QtCore.QSize(0, 20))
        self.doubleSpinBox_I.setDecimals(2)
        self.doubleSpinBox_I.setMaximum(100.0)
        self.doubleSpinBox_I.setSingleStep(0.001)
        self.doubleSpinBox_I.setObjectName("doubleSpinBox_I")
        self.gridLayout_6.addWidget(self.doubleSpinBox_I, 2, 3, 1, 1)
        self.verticalSlider_D = QtWidgets.QSlider(self.groupBox_5)
        self.verticalSlider_D.setMinimum(0)
        self.verticalSlider_D.setMaximum(100)
        self.verticalSlider_D.setPageStep(1)
        self.verticalSlider_D.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_D.setObjectName("verticalSlider_D")
        self.gridLayout_6.addWidget(self.verticalSlider_D, 2, 4, 3, 1)
        self.doubleSpinBox_D = QtWidgets.QDoubleSpinBox(self.groupBox_5)
        self.doubleSpinBox_D.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.doubleSpinBox_D.setFont(font)
        self.doubleSpinBox_D.setDecimals(2)
        self.doubleSpinBox_D.setMaximum(100.0)
        self.doubleSpinBox_D.setSingleStep(0.01)
        self.doubleSpinBox_D.setObjectName("doubleSpinBox_D")
        self.gridLayout_6.addWidget(self.doubleSpinBox_D, 2, 5, 1, 1)
        self.checkBox_P = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_P.setFont(font)
        self.checkBox_P.setIconSize(QtCore.QSize(10, 10))
        self.checkBox_P.setObjectName("checkBox_P")
        self.gridLayout_6.addWidget(self.checkBox_P, 3, 1, 1, 1)
        self.checkBox_I = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_I.setFont(font)
        self.checkBox_I.setObjectName("checkBox_I")
        self.gridLayout_6.addWidget(self.checkBox_I, 3, 3, 1, 1)
        self.checkBox_D = QtWidgets.QCheckBox(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.checkBox_D.setFont(font)
        self.checkBox_D.setChecked(False)
        self.checkBox_D.setObjectName("checkBox_D")
        self.gridLayout_6.addWidget(self.checkBox_D, 3, 5, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 269, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 4, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 269, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 4, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 269, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem10, 4, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_6.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_5)
        self.label_10.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_6.addWidget(self.label_10, 5, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_6.addWidget(self.label_11, 5, 4, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.gridLayout_8.setColumnStretch(0, 1)
        self.gridLayout_8.setRowStretch(0, 1)
        self.gridLayout_8.setRowStretch(1, 3)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_7.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口调试助手"))
        self.groupBox.setTitle(_translate("MainWindow", "串口选择"))
        self.label_27.setText(_translate("MainWindow", "波特率"))
        self.label_26.setText(_translate("MainWindow", "选择"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "115200"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(2, _translate("MainWindow", "38400"))
        self.label_28.setText(_translate("MainWindow", "操作"))
        self.pushButton_uart_sw.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_uart_rfresh.setText(_translate("MainWindow", "刷新"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收选项"))
        self.radioButton_show_ascii.setText(_translate("MainWindow", "文本显示"))
        self.pushButton_save.setText(_translate("MainWindow", "保存"))
        self.radioButton_show_hex.setText(_translate("MainWindow", "十六进制显示"))
        self.pushButton_clean.setText(_translate("MainWindow", "清除接收"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送选项"))
        self.radioButton_tx_ascii.setText(_translate("MainWindow", "文本显示"))
        self.radioButton_tx_hex.setText(_translate("MainWindow", "十六进制显示"))
        self.pushButton_tx.setText(_translate("MainWindow", "发送"))
        self.pushButton_clean_tx.setText(_translate("MainWindow", "清除发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "常规"))
        self.groupBox_4.setTitle(_translate("MainWindow", "串口选择"))
        self.label_29.setText(_translate("MainWindow", "波特率"))
        self.label_30.setText(_translate("MainWindow", "选择"))
        self.comboBox_baud_2.setItemText(0, _translate("MainWindow", "115200"))
        self.comboBox_baud_2.setItemText(1, _translate("MainWindow", "9600"))
        self.comboBox_baud_2.setItemText(2, _translate("MainWindow", "38400"))
        self.label_31.setText(_translate("MainWindow", "操作"))
        self.pushButton_uart_sw_2.setText(_translate("MainWindow", "打开串口"))
        self.pushButton_uart_rfresh_2.setText(_translate("MainWindow", "刷新"))
        self.groupBox_6.setTitle(_translate("MainWindow", "GroupBox"))
        self.lineEdit_7.setText(_translate("MainWindow", "red"))
        self.lineEdit_8.setText(_translate("MainWindow", "green"))
        self.lineEdit_9.setText(_translate("MainWindow", "blue"))
        self.lineEdit_10.setText(_translate("MainWindow", "yellow"))
        self.lineEdit_11.setText(_translate("MainWindow", "magenta"))
        self.lineEdit_12.setText(_translate("MainWindow", "cyan"))
        self.checkBox_curve_show_random.setText(_translate("MainWindow", "随机点曲线"))
        self.groupBox_5.setTitle(_translate("MainWindow", "PID参数"))
        self.label.setText(_translate("MainWindow", "P"))
        self.label_2.setText(_translate("MainWindow", "I"))
        self.label_5.setText(_translate("MainWindow", "D"))
        self.label_6.setText(_translate("MainWindow", "MAX"))
        self.label_7.setText(_translate("MainWindow", "MAX"))
        self.label_8.setText(_translate("MainWindow", "MAX"))
        self.checkBox_P.setText(_translate("MainWindow", "为负数"))
        self.checkBox_I.setText(_translate("MainWindow", "为负数"))
        self.checkBox_D.setText(_translate("MainWindow", "为负数"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "0"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "PID调参"))

