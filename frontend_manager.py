from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import os

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
        self.internPushButton.clicked.connect(lambda: stacked_window.setCurrentIndex(2))
        self.placementPushButton.clicked.connect(lambda: stacked_window.setCurrentIndex(2))


class AboutCompany(QMainWindow, about_company_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


class Login(QMainWindow, login_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.forgotPasswordGroupBox.hide()
        self.forgotPasswordCommandLinkButton.clicked.connect(self.forgotPasswordListener)

    def forgotPasswordListener(self):
        self.forgotPasswordGroupBox.show()
        self.loginDetailsGroupBox.hide()


class PlacementCellRecruiter(QMainWindow, placement_cell_recruiter_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


class PlacementCellStudent(QMainWindow, placement_cell_student_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)


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
    stacked_window.show()

    sys.exit(app.exec_())
