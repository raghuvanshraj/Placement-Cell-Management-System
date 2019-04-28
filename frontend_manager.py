from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os
from time import sleep

from db_helper import DBHelper

username = 'lruafctxgsjdsb'
password = '7f6f9c5c0b160cc13f80a8955323e27b2e52647c62b0e0c94c9c023f99e74c1b'
host = 'ec2-184-73-216-48.compute-1.amazonaws.com'
database = 'dffdu4arjfs5ta'

ui_folder = os.path.join('frontend', 'ui')

about_company_ui, _ = loadUiType(os.path.join(ui_folder, 'about_company.ui'))
intern_placement_ui, _ = loadUiType(os.path.join(ui_folder, 'intern_placement.ui'))
login_ui, _ = loadUiType(os.path.join(ui_folder, 'login.ui'))
placement_cell_student_ui, _ = loadUiType(os.path.join(ui_folder, 'placement_cell_student.ui'))
placement_cell_recruiter_ui, _ = loadUiType(os.path.join(ui_folder, 'placement_cell_recruiter.ui'))

is_intern = False


class Student(object):

    def __init__(self, student_username, student_password):
        self.username = student_username
        self.password = student_password
        self.details = db.fetch_student_details(self.username)


class Recruiter(object):

    def __init__(self, company_username, company_password):
        self.username = company_username
        self.password = company_password
        self.details = db.fetch_company_details(self.username)


class InternPlacement(QMainWindow, intern_placement_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.beforeDBConnection()
        self.connectButtons()

    def beforeDBConnection(self):
        self.internPushButton.setEnabled(False)
        self.placementPushButton.setEnabled(False)
        self.statusBar().showMessage('Connecting to Database...')

    def afterDBConnection(self):
        self.internPushButton.setEnabled(True)
        self.placementPushButton.setEnabled(True)
        self.statusBar().showMessage('Database Connected')

    def connectButtons(self):
        self.internPushButton.clicked.connect(self.internPushButtonListener)
        self.placementPushButton.clicked.connect(self.placementPushButtonListener)

    def internPushButtonListener(self):
        stacked_window.setCurrentIndex(2)
        global is_intern
        is_intern = True

    def placementPushButtonListener(self):
        stacked_window.setCurrentIndex(2)
        global is_intern
        is_intern = False


class AboutCompany(QMainWindow, about_company_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


class Login(QMainWindow, login_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.loginDetailsTabWidget.tabBar().setVisible(False)
        self.forgotPasswordFrame.hide()
        self.forgotPasswordCommandLinkButtonStudent.clicked.connect(self.forgotPasswordCommandLinkButtonListener)
        self.forgotPasswordCommandLinkButtonRecruiter.clicked.connect(self.forgotPasswordCommandLinkButtonListener)
        self.loginBackCommandLinkButtonStudent.clicked.connect(lambda: stacked_window.setCurrentIndex(0))
        self.loginBackCommandLinkButtonRecruiter.clicked.connect(lambda: stacked_window.setCurrentIndex(0))
        self.forgotPasswordBackCommandLinkButton.clicked.connect(self.forgotPasswordBackCommandLinkButtonListener)
        self.loginPushButtonStudent.clicked.connect(self.loginStudent)
        self.loginPushButtonRecruiter.clicked.connect(self.loginRecruiter)
        self.studentPushButton.clicked.connect(self.switchToStudentsTab)
        self.recruiterPushButton.clicked.connect(self.switchToRecruiterTab)
        # self.studentUsernameLineEdit.setStyleSheet("border: 1px solid red;")

    def forgotPasswordCommandLinkButtonListener(self):
        self.forgotPasswordFrame.show()
        self.loginDetailsGroupBox.setEnabled(False)

    def forgotPasswordBackCommandLinkButtonListener(self):
        self.forgotPasswordFrame.hide()
        self.loginDetailsGroupBox.setEnabled(True)

    def switchToStudentsTab(self):
        self.loginDetailsTabWidget.setCurrentIndex(0)

    def switchToRecruiterTab(self):
        self.loginDetailsTabWidget.setCurrentIndex(1)

    def loginStudent(self):
        username = self.studentUsernameLineEdit.text()
        password = self.studentPasswordLineEdit.text()
        # db.login_student(is_intern)
        stacked_window.setCurrentIndex(4)

    def loginRecruiter(self):
        # db.login_company(is_intern)
        stacked_window.setCurrentIndex(3)


class PlacementCellRecruiter(QMainWindow, placement_cell_recruiter_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


class PlacementCellStudent(QMainWindow, placement_cell_student_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.mainTabWidget.tabBar().setVisible(False)
        self.jobOpeningsPushButton.clicked.connect(self.switchToJobOpeningsTab)
        self.myApplicationsPushButton.clicked.connect(self.switchToApplicationsTab)
        self.myProfilePushButton.clicked.connect(self.switchToProfileTab)
        self.myAccountPushButton.clicked.connect(self.switchToAccountTab)
        self.signOutPushButton.clicked.connect(self.signOut)
        self.jobOpeningsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.applicationsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def switchToJobOpeningsTab(self):
        self.mainTabWidget.setCurrentIndex(0)

    def switchToApplicationsTab(self):
        self.mainTabWidget.setCurrentIndex(1)

    def switchToProfileTab(self):
        self.mainTabWidget.setCurrentIndex(2)

    def switchToAccountTab(self):
        self.mainTabWidget.setCurrentIndex(3)

    def signOut(self):
        stacked_window.setCurrentIndex(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    stacked_window = QStackedWidget()

    intern_placement_window = InternPlacement()
    about_company_window = AboutCompany()
    login_window = Login()
    placement_cell_recruiter_window = PlacementCellRecruiter()
    placement_cell_student_window = PlacementCellStudent()

    stacked_window.addWidget(intern_placement_window)
    stacked_window.addWidget(about_company_window)
    stacked_window.addWidget(login_window)
    stacked_window.addWidget(placement_cell_recruiter_window)
    stacked_window.addWidget(placement_cell_student_window)

    stacked_window.resize(intern_placement_window.size())
    qt_rectangle = stacked_window.frameGeometry()
    center_point = QDesktopWidget().availableGeometry().center()
    qt_rectangle.moveCenter(center_point)
    stacked_window.move(qt_rectangle.topLeft())
    stacked_window.show()

    # sleep(3)

    # db = DBHelper(username, password, host, database, debug_mode=True)

    intern_placement_window.afterDBConnection()

    sys.exit(app.exec_())
