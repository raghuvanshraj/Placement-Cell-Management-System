# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Placement_Cell.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 652)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 131, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Notifications.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 190, 131, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Job.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 270, 131, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Applications.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 430, 131, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Account.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 20, 801, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.listView = QtWidgets.QListView(self.tab)
        self.listView.setGeometry(QtCore.QRect(20, 80, 731, 171))
        self.listView.setObjectName("listView")
        self.label_33 = QtWidgets.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(30, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 80, 751, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(30, 30, 731, 22))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.pushButton_11 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_11.setGeometry(QtCore.QRect(680, 30, 81, 21))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_11.setIcon(icon4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 10, 801, 561))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab_6)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 511))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(110, 40, 611, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 71, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 80, 611, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 81, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 120, 611, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(110, 160, 611, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 160, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 240, 91, 16))
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(520, 200, 81, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(20, 330, 91, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(290, 200, 51, 16))
        self.label_11.setObjectName("label_11")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 260, 711, 41))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 350, 711, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(110, 200, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(350, 200, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(590, 200, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 470, 93, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(20, 410, 21, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_9.setGeometry(QtCore.QRect(60, 410, 113, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(200, 410, 41, 16))
        self.label_20.setObjectName("label_20")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setGeometry(QtCore.QRect(250, 410, 221, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(520, 410, 41, 16))
        self.label_21.setObjectName("label_21")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_10.setGeometry(QtCore.QRect(560, 410, 113, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_7)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 10, 751, 511))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 40, 611, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 40, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(110, 100, 111, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(260, 100, 91, 16))
        self.label_12.setObjectName("label_12")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 460, 93, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(350, 100, 111, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 160, 731, 281))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 90, 91, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(480, 90, 71, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(250, 90, 71, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 150, 71, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(250, 150, 71, 16))
        self.label_18.setObjectName("label_18")
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(10, 210, 71, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(480, 150, 71, 16))
        self.label_24.setObjectName("label_24")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(100, 210, 91, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(570, 150, 91, 22))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(340, 150, 91, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(100, 150, 91, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(570, 90, 91, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(340, 90, 91, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(440, 210, 121, 16))
        self.label_25.setObjectName("label_25")
        self.spinBox = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox.setGeometry(QtCore.QRect(570, 210, 91, 22))
        self.spinBox.setObjectName("spinBox")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label_13.setObjectName("label_13")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_6.setGeometry(QtCore.QRect(100, 30, 81, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(260, 30, 91, 16))
        self.label_22.setObjectName("label_22")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_7.setGeometry(QtCore.QRect(360, 30, 311, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_22.setGeometry(QtCore.QRect(340, 210, 91, 22))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_32 = QtWidgets.QLabel(self.groupBox_3)
        self.label_32.setGeometry(QtCore.QRect(250, 210, 71, 16))
        self.label_32.setObjectName("label_32")
        self.label_26 = QtWidgets.QLabel(self.groupBox_2)
        self.label_26.setGeometry(QtCore.QRect(500, 100, 111, 16))
        self.label_26.setObjectName("label_26")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_17.setGeometry(QtCore.QRect(620, 100, 101, 22))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.groupBox_3.raise_()
        self.lineEdit_4.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.lineEdit_5.raise_()
        self.label_12.raise_()
        self.pushButton_8.raise_()
        self.lineEdit_6.raise_()
        self.label_26.raise_()
        self.lineEdit_17.raise_()
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(40, 90, 741, 471))
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 30, 751, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_27 = QtWidgets.QLabel(self.groupBox_4)
        self.label_27.setGeometry(QtCore.QRect(30, 50, 81, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_18.setGeometry(QtCore.QRect(130, 50, 581, 22))
        self.lineEdit_18.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_28 = QtWidgets.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(30, 90, 91, 16))
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.groupBox_4)
        self.label_29.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_29.setObjectName("label_29")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_19.setGeometry(QtCore.QRect(130, 130, 581, 22))
        self.lineEdit_19.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_20.setGeometry(QtCore.QRect(130, 90, 581, 22))
        self.lineEdit_20.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setGeometry(QtCore.QRect(610, 170, 93, 28))
        self.pushButton_9.setObjectName("pushButton_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 290, 751, 211))
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_30 = QtWidgets.QLabel(self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(20, 50, 101, 16))
        self.label_30.setObjectName("label_30")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 50, 241, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_31 = QtWidgets.QLabel(self.groupBox_6)
        self.label_31.setGeometry(QtCore.QRect(20, 100, 101, 16))
        self.label_31.setObjectName("label_31")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_21.setGeometry(QtCore.QRect(130, 100, 591, 22))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_10.setGeometry(QtCore.QRect(620, 160, 93, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.tabWidget.addTab(self.tab_5, "")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 350, 131, 51))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/Profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon5)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 10, 93, 28))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/Logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Notifications"))
        self.pushButton_2.setText(_translate("MainWindow", "Job Openings"))
        self.pushButton_3.setText(_translate("MainWindow", "My Applications"))
        self.pushButton_5.setText(_translate("MainWindow", "My Account"))
        self.label_33.setText(_translate("MainWindow", "Notifications"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Company Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Branches"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Application Deadline"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Course"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date of Visit"))
        self.lineEdit_23.setPlaceholderText(_translate("MainWindow", "Search"))
        self.pushButton_11.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.groupBox.setTitle(_translate("MainWindow", "My Profile"))
        self.label.setText(_translate("MainWindow", "First Name"))
        self.label_2.setText(_translate("MainWindow", "Last Name"))
        self.label_3.setText(_translate("MainWindow", "Email Address"))
        self.label_4.setText(_translate("MainWindow", "Phone Number"))
        self.label_5.setText(_translate("MainWindow", "Date of Birth"))
        self.label_6.setText(_translate("MainWindow", "Address Line 1"))
        self.label_9.setText(_translate("MainWindow", "Category"))
        self.label_10.setText(_translate("MainWindow", "Address Line 2"))
        self.label_11.setText(_translate("MainWindow", "Gender"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Female"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Other"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "DASA"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "General"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SC"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "ST"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "OBC"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "PH"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Other"))
        self.pushButton_7.setText(_translate("MainWindow", "Update"))
        self.label_19.setText(_translate("MainWindow", "City"))
        self.label_20.setText(_translate("MainWindow", "State"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Andaman and Nicobar Islands"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Andhra Pradesh"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Arunachal Pradesh"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Assam"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "Bihar"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "Chandigarh"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "Chhattisgarh"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "Dadra and Nagar Haveli"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "Daman and Diu"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "National Capital Territory of Delhi"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "Goa"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "Gujarat"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "Haryana"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "Himanchal Pradesh"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "Jammu and Kashmir"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "Jharkhand"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "Karnataka"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "Kerala"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "Lakshwadeep"))
        self.comboBox_5.setItemText(19, _translate("MainWindow", "Madhya Pradesh"))
        self.comboBox_5.setItemText(20, _translate("MainWindow", "Maharashtra"))
        self.comboBox_5.setItemText(21, _translate("MainWindow", "Manipur"))
        self.comboBox_5.setItemText(22, _translate("MainWindow", "Meghalaya"))
        self.comboBox_5.setItemText(23, _translate("MainWindow", "Mizoram"))
        self.comboBox_5.setItemText(24, _translate("MainWindow", "Nagaland"))
        self.comboBox_5.setItemText(25, _translate("MainWindow", "Orissa"))
        self.comboBox_5.setItemText(26, _translate("MainWindow", "Puducherry"))
        self.comboBox_5.setItemText(27, _translate("MainWindow", "Punjab"))
        self.comboBox_5.setItemText(28, _translate("MainWindow", "Rajasthan"))
        self.comboBox_5.setItemText(29, _translate("MainWindow", "Sikkim"))
        self.comboBox_5.setItemText(30, _translate("MainWindow", "Tamil Nadu"))
        self.comboBox_5.setItemText(31, _translate("MainWindow", "Telangana"))
        self.comboBox_5.setItemText(32, _translate("MainWindow", "Tripura"))
        self.comboBox_5.setItemText(33, _translate("MainWindow", "Uttar Pradesh"))
        self.comboBox_5.setItemText(34, _translate("MainWindow", "Uttarakhand"))
        self.comboBox_5.setItemText(35, _translate("MainWindow", "West Bengal"))
        self.comboBox_5.setItemText(36, _translate("MainWindow", "Other"))
        self.label_21.setText(_translate("MainWindow", "Pin"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Personal"))
        self.groupBox_2.setTitle(_translate("MainWindow", "My Profile"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Google Drive Link"))
        self.label_7.setText(_translate("MainWindow", "Resume"))
        self.label_8.setText(_translate("MainWindow", "X Aggregate"))
        self.label_12.setText(_translate("MainWindow", "XII Aggregate"))
        self.pushButton_8.setText(_translate("MainWindow", "Update"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Score Sheet"))
        self.label_14.setText(_translate("MainWindow", "Semester 1"))
        self.label_15.setText(_translate("MainWindow", "Semester 3"))
        self.label_16.setText(_translate("MainWindow", "Semester 2"))
        self.label_17.setText(_translate("MainWindow", "Semester 4"))
        self.label_18.setText(_translate("MainWindow", "Semester 5"))
        self.label_23.setText(_translate("MainWindow", "Semester 7"))
        self.label_24.setText(_translate("MainWindow", "Semester 6"))
        self.label_25.setText(_translate("MainWindow", "Number of Backlogs"))
        self.label_13.setText(_translate("MainWindow", "Course"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "B. Tech."))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "M. Tech."))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "MBA"))
        self.label_22.setText(_translate("MainWindow", "Branch"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Bio-Technology"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "Civil Engineering"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Computer Engineering"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Electrical and Electronics Engineering"))
        self.comboBox_7.setItemText(4, _translate("MainWindow", "Electrical Engineering"))
        self.comboBox_7.setItemText(5, _translate("MainWindow", "Electronics and Communication Engineering"))
        self.comboBox_7.setItemText(6, _translate("MainWindow", "Engineering Physics"))
        self.comboBox_7.setItemText(7, _translate("MainWindow", "Environmental Engineering"))
        self.comboBox_7.setItemText(8, _translate("MainWindow", "Information Technology"))
        self.comboBox_7.setItemText(9, _translate("MainWindow", "Mathematics and Computing"))
        self.comboBox_7.setItemText(10, _translate("MainWindow", "Mechanical Engineering"))
        self.comboBox_7.setItemText(11, _translate("MainWindow",
                                                   "Mechanical Engineering with Specialization in Automotive Engineering"))
        self.comboBox_7.setItemText(12, _translate("MainWindow", "Polymer Science and Chemical Technology"))
        self.comboBox_7.setItemText(13, _translate("MainWindow", "Production and Industrial Engineering"))
        self.comboBox_7.setItemText(14, _translate("MainWindow", "Software Engineering"))
        self.comboBox_7.setItemText(15, _translate("MainWindow", "Bio-Informatics"))
        self.comboBox_7.setItemText(16, _translate("MainWindow", "Computational Design"))
        self.comboBox_7.setItemText(17, _translate("MainWindow", "Computer Science and Engineering"))
        self.comboBox_7.setItemText(18, _translate("MainWindow", "Control and Instrumentation Engineering"))
        self.comboBox_7.setItemText(19, _translate("MainWindow", "Hydraulic and Flood Engineering"))
        self.comboBox_7.setItemText(20, _translate("MainWindow", "Geotechnical Engineering"))
        self.comboBox_7.setItemText(21, _translate("MainWindow", "Microwave and Optical Communication"))
        self.comboBox_7.setItemText(22, _translate("MainWindow", "Nano Science and Technology"))
        self.comboBox_7.setItemText(23, _translate("MainWindow", "Nuclear Science and Engineering"))
        self.comboBox_7.setItemText(24, _translate("MainWindow", "Polymer Technology"))
        self.comboBox_7.setItemText(25, _translate("MainWindow", "Power System"))
        self.comboBox_7.setItemText(26, _translate("MainWindow", "Production Engineering"))
        self.comboBox_7.setItemText(27, _translate("MainWindow", "Renewable Energy Technology"))
        self.comboBox_7.setItemText(28, _translate("MainWindow", "Signal Processing and Digital Design"))
        self.comboBox_7.setItemText(29, _translate("MainWindow", "Structure Engineering"))
        self.comboBox_7.setItemText(30, _translate("MainWindow", "Thermal Engineering"))
        self.comboBox_7.setItemText(31, _translate("MainWindow", "VLSI Design and Embedded System"))
        self.comboBox_7.setItemText(32, _translate("MainWindow", "MBA"))
        self.label_32.setText(_translate("MainWindow", "Semester 8"))
        self.label_26.setText(_translate("MainWindow", "Year of Graduation"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Academic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Page"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Company Name"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Application Status"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Time of Submission"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date of Visit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Page"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Change Password"))
        self.label_27.setText(_translate("MainWindow", "Old Password"))
        self.label_28.setText(_translate("MainWindow", "New Password"))
        self.label_29.setText(_translate("MainWindow", "New Password"))
        self.pushButton_9.setText(_translate("MainWindow", "Update"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Security Question"))
        self.label_30.setText(_translate("MainWindow", "Security Question"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "What was the name of my first pet?"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "What was my first school?"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "What is my mother\'s maiden name?"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Who is my favourite Hollywood star?"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "What is my brother\'s/sister\'s name?"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "Who is my favourite sportsperson?"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "What is my best friend\'s name?"))
        self.label_31.setText(_translate("MainWindow", "Answer"))
        self.pushButton_10.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Page"))
        self.pushButton_4.setText(_translate("MainWindow", "My Profile"))
        self.pushButton_6.setText(_translate("MainWindow", "Sign Out"))


import icons_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())