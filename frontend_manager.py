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
is_student = True


class Student(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.details = None

    def set_identifiers(self, username, password):
        self.username = username
        self.password = password

    def fetch_details(self):
        self.details = db.fetch_student_details(self.username)

    def del_identifiers(self):
        self.username = ''
        self.password = ''


class Recruiter(object):

    def __init__(self):
        self.username = None
        self.password = None
        self.details = None

    def set_identifiers(self, username, password):
        self.username = username
        self.password = password

    def fetch_details(self):
        self.details = db.fetch_company_details(self.username)

    def del_identifiers(self):
        self.username = ''
        self.password = ''


student = Student()
recruiter = Recruiter()


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
        self.studentUsernameLineEdit.setText('2k16/co/01')
        self.studentPasswordLineEdit.setText('password')
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
        self.studentUsernameLineEdit.textChanged.connect(lambda: self.studentUsernameLineEdit.setStyleSheet(""))
        self.studentPasswordLineEdit.textChanged.connect(lambda: self.studentPasswordLineEdit.setStyleSheet(""))
        self.recruiterUsernameLineEdit.textChanged.connect(lambda: self.recruiterUsernameLineEdit.setStyleSheet(""))
        self.recruiterPasswordLineEdit.textChanged.connect(lambda: self.recruiterPasswordLineEdit.setStyleSheet(""))

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
        login_state = db.login_student(username, password, is_intern)
        if login_state == DBHelper.LOGIN_SUCCESSFUL:
            global is_student
            is_student = True
            student.set_identifiers(username, password)
            stacked_window.setCurrentIndex(4)
        else:
            if login_state == DBHelper.INVALID_USERNAME:
                self.studentUsernameLineEdit.setStyleSheet("border: 1px solid red;")
            elif login_state == DBHelper.INVALID_PASSWORD:
                self.studentPasswordLineEdit.setStyleSheet("border: 1px solid red;")

    def loginRecruiter(self):
        username = self.recruiterUsernameLineEdit.text()
        password = self.recruiterPasswordLineEdit.text()
        login_state = db.login_company(username, password)
        if login_state == DBHelper.LOGIN_SUCCESSFUL:
            global is_student
            is_student = False
            recruiter.set_identifiers(username, password)
            stacked_window.setCurrentIndex(4)
        else:
            if login_state == DBHelper.INVALID_USERNAME:
                self.recruiterUsernameLineEdit.setStyleSheet("border: 1px solid red;")
            elif login_state == DBHelper.INVALID_PASSWORD:
                self.recruiterPasswordLineEdit.setStyleSheet("border: 1px solid red;")


class PlacementCellRecruiter(QMainWindow, placement_cell_recruiter_ui):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.mainTabWidget.tabBar().setVisible(False)
        self.companyInfoPushButton.clicked.connect(self.switchToCompanyInfoTab)
        self.applicationsPushButton.clicked.connect(self.switchToApplicationsTab)
        self.selectionsPushButton.clicked.connect(self.switchToSelectionsTab)
        self.myAccountPushButton.clicked.connect(self.switchToAccountTab)
        self.signOutPushButton.clicked.connect(self.signOut)
        self.applicationsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.jobsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.selectionsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.bTechCheckBox.toggled.connect(self.checkBoxStateChanged)
        self.mTechCheckBox.toggled.connect(self.checkBoxStateChanged)

    def checkBoxStateChanged(self):
        self.bTechCourseComboBox.setEnabled(self.bTechCheckBox.isChecked())
        self.mTechCourseComboBox.setEnabled(self.mTechCheckBox.isChecked())

    def populateJobsTable(self):
        jobs = db.fetch_jobs_company(recruiter.username, is_intern)
        for row, job in enumerate(jobs):
            for col, item in enumerate(job):
                self.jobsTableWidget.setItem(
                    row, col, QTableWidgetItem(str(item))
                )

            self.jobsTableWidget.insertRow(0)

    def populateCompanyInfoTab(self):
        company_details = db.fetch_company_details(recruiter.username)
        pcs = db.fetch_pc_responsible_for_company(recruiter.username)
        self.nameLineEdit.setText(company_details['name'])
        self.aboutCompanyTextEdit.setText(company_details['about_company'])

        pcs_string = ''
        for pc in pcs:
            pcs_string = pcs_string + ', ' + pc
        self.pcLineEdit.setText(pcs_string)

    def populateApplicationsTable(self):
        applications = db.fetch_applications_company(recruiter.username)
        for row, application in enumerate(applications):
            for col, item in enumerate(application):
                self.applicationsTableWidget.setItem(
                    row, col, QTableWidgetItem(str(item))
                )

            self.applicationsTableWidget.insertRow(0)

    def populateFinalSelectionsTable(self):
        selections = db.fetch_selections_company(recruiter.username)
        for row, selection in enumerate(selections):
            for col, item in enumerate(selection):
                self.selectionsTableWidget.setItem(
                    row, col, QTableWidgetItem(str(item))
                )

            self.selectionsTableWidget.insertRow(0)

    def truncateJobFields(self):
        self.jobProfileLineEdit.setText('')
        self.cutoffLineEdit.setText('')
        self.jobDescTextEdit.setText('')
        self.eligibleCoursesListWidget.clear()
        self.locationLineEdit.setText('')
        self.bTechCheckBox.setChecked(False)
        self.mTechCheckBox.setChecked(False)
        self.locationLineEdit.setText('')
        self.stipendLineEdit.setText('')

    def addJob(self):
        self.addJobPushButton.setEnabled(False)
        job_details = dict()
        job_details['job_title'] = self.jobProfileLineEdit.text()
        job_details['description'] = self.jobDescTextEdit.text()
        job_details['cutoff'] = self.cutoffLineEdit.text()
        job_details['deadline'] = self.deadlineDateEdit.date()
        job_details['dov'] = self.dovDateEdit.text()
        job_details['process_ongoing'] = True
        job_details['for_intern'] = is_intern

        if is_intern:
            job_details['stipend_intern'] = self.stipendLineEdit.text()
        else:
            job_details['package_placement'] = self.stipendLineEdit.text()

        job_details['location'] = self.locationLineEdit.text()
        job_details['company_tin'] = recruiter.username

        branches = []
        for index in range(self.eligibleCoursesListWidget.count()):
            branches.append(self.eligibleCoursesListWidget.item(index))

        db.add_job(job_details, branches)

        self.addJobPushButton.setEnabled(False)
        self.truncateJobFields()
        self.populateJobsTable()

    def switchToCompanyInfoTab(self):
        self.mainTabWidget.setCurrentIndex(0)

    def switchToApplicationsTab(self):
        self.mainTabWidget.setCurrentIndex(1)

    def switchToSelectionsTab(self):
        self.mainTabWidget.setCurrentIndex(2)

    def switchToAccountTab(self):
        self.mainTabWidget.setCurrentIndex(3)

    def signOut(self):
        recruiter.del_identifiers()
        stacked_window.setCurrentIndex(2)


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
        self.oldPasswordLineEdit.textChanged.connect(lambda: self.oldPasswordLineEdit.setStyleSheet(""))
        self.confirmNewPasswordLineEdit.textChanged.connect(lambda: self.confirmNewPasswordLineEdit.setStyleSheet(""))

    def populateJobOpeningsTable(self):
        job_profiles, deadlines, dovs = db.fetch_jobs_student(student.username)

        for i in range(len(job_profiles)):
            self.jobOpeningsTableWidget.insertRow(0)
            self.jobOpeningsTableWidget.setItem(
                i, 0, QTableWidgetItem(job_profiles[i])
            )

        for i in range(len(deadlines)):
            self.jobOpeningsTableWidget.setItem(
                i, 1, QTableWidgetItem(str(deadlines[i].date()))
            )

        for i in range(len(dovs)):
            self.jobOpeningsTableWidget.setItem(
                i, 2, QTableWidgetItem(str(dovs[i]))
            )

        # for i in range(len)
        # for row, job in enumerate(jobs):
        #     for col, item in enumerate(job):
        #         self.jobOpeningsTableWidget.setItem(
        #             row, col, QTableWidgetItem(str(item))
        #         )
        #
        #     self.jobOpeningsTableWidget.insertRow(0)

    def populateApplicationsTable(self):
        applications = db.fetch_applications_student(student.username)
        for row, application in enumerate(applications):
            for col, item in enumerate(application):
                self.applicationsTableWidget.setItem(
                    row, col, QTableWidgetItem(str(item))
                )

            self.applicationsTableWidget.insertRow(0)

    def populateProfileTab(self):

        # resolve pincode based issues

        student_details = db.fetch_student_details(student.username)
        print()
        print(student_details)
        print()
        self.firstNameLineEdit.setText(student_details['f_name'])
        self.lastNameLineEdit.setText(student_details['l_name'])
        self.emailLineEdit.setText(student_details['email_id'])
        self.phoneLineEdit.setText(student_details['contact_no'])
        self.dobDateEdit.setDate(QDate(student_details['dob']))

        genderComboBoxIndex = self.genderComboBox.findText(student_details['gender'], Qt.MatchFixedString)
        self.genderComboBox.setCurrentIndex(genderComboBoxIndex)

        categoryComboBoxIndex = self.categoryComboBox.findText(student_details['category'], Qt.MatchFixedString)
        self.categoryComboBox.setCurrentIndex(categoryComboBoxIndex)

        self.addressLine1TextEdit.setText(student_details['address_line_1'])
        self.addressLine2TextEdit.setText(student_details['address_line_2'])
        # self.cityLineEdit.setText(student_details['city'])

        # stateComboBoxIndex = self.stateComboBox.findText(student_details['state'], Qt.MatchFixedString)
        # self.stateComboBox.setCurrentIndex(stateComboBoxIndex)

        self.pinLineEdit.setText(student_details['pincode'])
        self.resumeLineEdit.setText(student_details['resume_link'])
        self.marks10LineEdit.setText(str(student_details['marks_10']))
        self.marks12LineEdit.setText(str(student_details['marks_12']))
        self.gradYearLineEdit.setText(str(student_details['grad_year']))

        courseComboBoxIndex = self.courseComboBox.findText(student_details['course'], Qt.MatchFixedString)
        self.courseComboBox.setCurrentIndex(courseComboBoxIndex)

        branchComboBoxIndex = self.branchComboBox.findText(student_details['branch'], Qt.MatchFixedString)
        self.branchComboBox.setCurrentIndex(branchComboBoxIndex)

        self.sem1LineEdit.setText(str(student_details['gpa_1']))
        self.sem2LineEdit.setText(str(student_details['gpa_2']))
        self.sem3LineEdit.setText(str(student_details['gpa_3']))
        self.sem4LineEdit.setText(str(student_details['gpa_4']))
        self.sem5LineEdit.setText(str(student_details['gpa_5']))
        self.sem6LineEdit.setText(str(student_details['gpa_6']))
        self.sem7LineEdit.setText(str(student_details['gpa_7']))
        self.backlogsLineEdit.setText(str(student_details['no_of_backlogs']))

    def updateProfileInfo(self):
        self.updateInfoPushButton.setEnabled(False)
        student_info = dict()
        student_info['roll_no'] = student.username
        student_info['fname'] = self.firstNameLineEdit.text()
        student_info['lname'] = self.lastNameLineEdit.text()
        student_info['contact_no'] = self.phoneLineEdit.text()
        student_info['address_line_1'] = self.addressLine1LineEdit.text()
        student_info['address_line_2'] = self.addressLine2LineEdit.text()
        student_info['address_line_3'] = self.addressLine3LineEdit.text()
        student_info['pincode'] = self.pinLineEdit.text()
        student_info['gender'] = self.genderComboBox.currentText()
        student_info['resume_link'] = self.resumeLineEdit.text()
        student_info['email_id'] = self.emailLineEdit.text()
        student_info['gpa_1'] = float(self.sem1LineEdit.text())
        student_info['gpa_2'] = float(self.sem2LineEdit.text())
        student_info['gpa_3'] = float(self.sem3LineEdit.text())
        student_info['gpa_4'] = float(self.sem4LineEdit.text())
        student_info['gpa_5'] = float(self.sem5LineEdit.text())
        student_info['gpa_6'] = float(self.sem6LineEdit.text())
        student_info['gpa_7'] = float(self.sem7LineEdit.text())
        student_info['branch'] = self.branchComboBox.currentText()
        student_info['category'] = self.categoryComboBox.currentText()
        student_info['grad_year'] = self.gradYearLineEdit.text()
        student_info['dob'] = self.dobDateEdit.date()
        student_info['no_of_backlogs'] = int(self.backlogsLineEdit.text())
        student_info['marks_10'] = float(self.marks10LineEdit.text())
        student_info['marks_12'] = float(self.marks12LineEdit.text())

        db.update_student_details(student_info)

        self.updateInfoPushButton.setEnabled(True)

    def updatePassword(self):
        self.updatePasswordPushButton.setEnabled(False)
        if self.oldPasswordLineEdit.text() == student.password:
            if self.newPasswordLineEdit.text() == self.confirmNewPasswordLineEdit.text():
                db.change_student_password(student.username, student.password)
            else:
                self.confirmNewPasswordLineEdit.setStyleSheet("border: 1px solid red;")
        else:
            self.oldPasswordLineEdit.setStyleSheet("border: 1px solid red;")

    def switchToJobOpeningsTab(self):
        self.mainTabWidget.setCurrentIndex(0)
        self.populateJobOpeningsTable()

    def switchToApplicationsTab(self):
        self.mainTabWidget.setCurrentIndex(1)
        self.populateApplicationsTable()

    def switchToProfileTab(self):
        self.mainTabWidget.setCurrentIndex(2)
        self.populateProfileTab()

    def switchToAccountTab(self):
        self.mainTabWidget.setCurrentIndex(3)

    def signOut(self):
        student.del_identifiers()
        stacked_window.setCurrentIndex(2)


if __name__ == '__main__':
    db = DBHelper(username, password, host, database, debug_mode=True)

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

    intern_placement_window.afterDBConnection()

    sys.exit(app.exec_())
