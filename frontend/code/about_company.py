# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About_Company.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(903, 667)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(320, 60, 81, 31))
        self.lcdNumber.setObjectName("lcdNumber")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(54, 130, 101, 20))
        self.label_3.setObjectName("label_3")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 150, 821, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 270, 131, 20))
        self.label_4.setObjectName("label_4")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 290, 821, 91))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 410, 131, 20))
        self.label_5.setObjectName("label_5")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(50, 430, 821, 91))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(50, 120, 821, 121))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(50, 260, 821, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(50, 400, 821, 121))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(50, 540, 171, 81))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 101, 20))
        self.label_6.setObjectName("label_6")
        self.textEdit = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit.setGeometry(QtCore.QRect(0, 30, 171, 51))
        self.textEdit.setObjectName("textEdit")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(270, 540, 171, 81))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 101, 20))
        self.label_7.setObjectName("label_7")
        self.textEdit_2 = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_2.setGeometry(QtCore.QRect(0, 30, 171, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(490, 540, 171, 81))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_8 = QtWidgets.QLabel(self.frame_6)
        self.label_8.setGeometry(QtCore.QRect(0, 10, 151, 20))
        self.label_8.setObjectName("label_8")
        self.textEdit_3 = QtWidgets.QTextEdit(self.frame_6)
        self.textEdit_3.setGeometry(QtCore.QRect(0, 30, 171, 51))
        self.textEdit_3.setObjectName("textEdit_3")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(700, 540, 171, 81))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(0, 10, 151, 20))
        self.label_9.setObjectName("label_9")
        self.textEdit_4 = QtWidgets.QTextEdit(self.frame_7)
        self.textEdit_4.setGeometry(QtCore.QRect(0, 30, 171, 51))
        self.textEdit_4.setObjectName("textEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 50, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_notapplicable = QtWidgets.QLabel(self.centralwidget)
        self.label_notapplicable.setGeometry(QtCore.QRect(790, 100, 55, 16))
        self.label_notapplicable.setText("")
        self.label_notapplicable.setObjectName("label_notapplicable")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(410, 50, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame.raise_()
        self.label.raise_()
        self.lcdNumber.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.plainTextEdit.raise_()
        self.label_4.raise_()
        self.plainTextEdit_2.raise_()
        self.label_5.raise_()
        self.plainTextEdit_3.raise_()
        self.frame_4.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.pushButton.raise_()
        self.label_notapplicable.raise_()
        self.label_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Company Name"))
        self.label_2.setText(_translate("MainWindow", "Application Deadline"))
        self.label_3.setText(_translate("MainWindow", "About Company"))
        self.label_4.setText(_translate("MainWindow", "Internship Description"))
        self.label_5.setText(_translate("MainWindow", "Note"))
        self.label_6.setText(_translate("MainWindow", "Stipend"))
        self.label_7.setText(_translate("MainWindow", "Location"))
        self.label_8.setText(_translate("MainWindow", "Coordinator Responsible"))
        self.label_9.setText(_translate("MainWindow", "Date of Visit"))
        self.pushButton.setText(_translate("MainWindow", "Apply"))
        self.label_10.setText(_translate("MainWindow", "Days"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())