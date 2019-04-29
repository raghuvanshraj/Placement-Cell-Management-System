# change test database to production

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, BigInteger, String, Boolean, Float, \
    Date, Time, DateTime, MetaData, ForeignKey
from sqlalchemy import and_
from sqlalchemy.sql import select
import math


class DBHelper(object):
    INVALID_USERNAME = 0
    INVALID_PASSWORD = -1
    LOGIN_SUCCESSFUL = 1

    def __init__(self, username, password, host, database, debug_mode):
        self.uri = 'postgres://' + username + ':' + password + '@' + host + '/' + database
        self.engine = create_engine(self.uri, echo=debug_mode)

        try:
            self.connection = self.engine.connect()
        except Exception as err:
            print("Connection Failed:", err)

        self.meta = MetaData(bind=self.engine)

        self.login_credentials_student = Table(
            'login_credentials_student', self.meta,
            Column('username', String, primary_key=True),
            Column('password', String, nullable=False),
            Column('for_intern', Boolean, nullable=False)
        )

        self.login_credentials_company = Table(
            'login_credentials_company', self.meta,
            Column('username', String, primary_key=True),
            Column('password', String, nullable=False),
        )

        self.geolocation = Table(
            'geolocation', self.meta,
            Column('pincode', String, primary_key=True),
            Column('city', String),
            Column('state', String)
        )

        self.students = Table(
            'students', self.meta,
            Column('roll_no', String, primary_key=True),
            Column('f_name', String),
            Column('l_name', String),
            Column('contact_no', String),
            Column('address_line_1', String),
            Column('address_line_2', String),
            Column('address_line_3', String),
            Column('pincode', String, ForeignKey(self.geolocation.c.pincode)),
            Column('gender', String),
            Column('resume_link', String),
            Column('email_id', String),
            Column('gpa_1', Float),
            Column('gpa_2', Float),
            Column('gpa_3', Float),
            Column('gpa_4', Float),
            Column('gpa_5', Float),
            Column('gpa_6', Float),
            Column('gpa_7', Float),
            Column('course', String),
            Column('branch', String),
            Column('category', String),
            Column('grad_year', String),
            Column('dob', Date),
            Column('no_of_backlogs', Integer),
            Column('marks_10', Float),
            Column('marks_12', Float),
            Column('is_PC', Boolean)
        )

        self.companies = Table(
            'companies', self.meta,
            Column('company_tin', String, primary_key=True),
            Column('about_company', String),
            Column('name', String),
            Column('for_intern', Boolean),
            Column('for_placement', Boolean),
            Column('for_training', Boolean),
            Column('contact_no', String),
            Column('email_id', String),
            Column('location', String),
        )

        self.student_manages_company = Table(
            'student_manages_company', self.meta,
            Column('roll_no', String, primary_key=True),
            Column('company_tin', String, primary_key=True)
        )

        self.jobs = Table(
            'jobs', self.meta,
            Column('job_id', BigInteger, primary_key=True, autoincrement=True),
            Column('job_title', String),
            Column('description', String),
            Column('cutoff', Float),
            Column('deadline', DateTime(timezone=True)),
            Column('dov', Date),
            Column('process_ongoing', Boolean),
            Column('package_placement', BigInteger),
            Column('stipend_intern', BigInteger),
            Column('duration_intern', Integer),
            Column('location', String),
            Column('for_intern', Boolean),
            Column('company_tin', String, ForeignKey(self.companies.c.company_tin))
        )

        self.branches_eligible = Table(
            'branches_eligible', self.meta,
            Column('branch', String, primary_key=True),
            Column('course', String, primary_key=True),
            Column('job_id', BigInteger, ForeignKey(self.jobs.c.job_id), primary_key=True)
        )

        self.trainings = Table(
            'trainings', self.meta,
            Column('training_id', BigInteger, primary_key=True, autoincrement=True),
            Column('subject_matter', String),
            Column('date', Date),
            Column('time', Time(timezone=True)),
            Column('company_tin', String, ForeignKey(self.companies.c.company_tin))
        )

        self.student_applies_for_job = Table(
            'student_applies_for_job', self.meta,
            Column('roll_no', String, ForeignKey(self.students.c.roll_no), primary_key=True),
            Column('job_id', BigInteger, ForeignKey(self.jobs.c.job_id), primary_key=True),
            Column('is_shortlisted', Boolean),
            Column('is_rejected', Boolean),
            Column('is_selected', Boolean)
        )

        self.student_applies_for_training = Table(
            'student_applies_for_training', self.meta,
            Column('roll_no', String, ForeignKey(self.students.c.roll_no), primary_key=True),
            Column('training_id', BigInteger, ForeignKey(self.trainings.c.training_id), primary_key=True),
        )

        self.branch_course = Table(
            'branch_course', self.meta,
            Column('branch', String, primary_key=True),
            Column('course', String, primary_key=True)
        )

    def create_tables(self):
        self.meta.create_all(self.engine)

    def login_student(self, username, password, for_intern):
        command = self.login_credentials_student.select(
            whereclause=and_(
                self.login_credentials_student.c.username == username,
                self.login_credentials_student.c.for_intern == for_intern
            )
        )
        result = self.connection.execute(command)
        row = result.fetchone()
        print(row)

        if row:
            if row[-2] == password:
                return DBHelper.LOGIN_SUCCESSFUL
            else:
                print('Incorrect Password')
                return DBHelper.INVALID_PASSWORD
        else:
            print('Incorrect Username')
            return DBHelper.INVALID_USERNAME

    def login_company(self, username, password):
        command = self.login_credentials_company.select(
            whereclause=self.login_credentials_company.c.username == username,
        )
        result = self.connection.execute(command)
        row = result.fetchone()

        if row:
            if row[-1] == password:
                return DBHelper.LOGIN_SUCCESSFUL
            else:
                print('Incorrect Password')
                return DBHelper.INVALID_PASSWORD
        else:
            print('Incorrect Username')
            return DBHelper.INVALID_USERNAME

    def fetch_job_details(self, job_id):
        command = self.jobs.select(
            whereclause=self.jobs.c.job_id == job_id
        )
        result = self.connection.execute(command).fetchone()[1:]
        columns = [column.key for column in self.jobs.columns]

        return dict(zip(columns, result))

    def fetch_company_details(self, company_tin):
        command = self.companies.select(
            whereclause=self.companies.c.company_tin == company_tin
        )
        result = self.connection.execute(command).fetchone()[1:]
        columns = [column.key for column in self.companies.columns]

        return dict(zip(columns, result))

    def fetch_student_details(self, roll_no):
        command = self.students.select(
            whereclause=self.students.c.roll_no == roll_no
        )
        result = self.connection.execute(command).fetchone()
        columns = [column.key for column in self.students.columns]

        return dict(zip(columns, result))

    def populate_geolocation_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        indian_pincodes = pd.read_csv(path)
        indian_pincodes_np = np.array(indian_pincodes)

        unique_pincodes = []

        for row in indian_pincodes_np:
            if row[0] in unique_pincodes:
                continue

            unique_pincodes.append(row[0])
            command = self.geolocation.insert().values(pincode=row[0], city=row[1], state=row[2])
            self.connection.execute(command)

    def fetch_unique_states(self):
        command = select([self.geolocation.c.state]).distinct()
        result = self.connection.execute(command)

        return result

    def fetch_unique_cities(self):
        command = select([self.geolocation.c.city]).distinct()
        result = self.connection.execute(command).fetchall()

        return result

    def fetch_location_with_pincode(self, pincode):
        command = self.geolocation.select(
            whereclause=self.geolocation.c.pincode == pincode
        )
        result = self.connection.execute(command).fetchone()[1:]
        columns = [column.key for column in self.geolocation.columns]

        return dict(zip(columns, result))

    def fetch_locations_with_city(self, city):
        command = self.geolocation.select(
            whereclause=self.geolocation.c.city == city
        )
        result = self.connection.execute(command).fetchall()
        result_restructured = list(zip(*result))[1:]
        columns = [column.key for column in self.geolocation.columns]

        return dict(zip(columns, result_restructured))

    def fetch_locations_with_state(self, state):
        command = self.geolocation.select(
            whereclause=self.geolocation.c.state == state
        )
        result = self.connection.execute(command).fetchall()
        result_restructured = list(zip(*result))[1:]
        columns = [column.key for column in self.geolocation.columns]

        return dict(zip(columns, result_restructured))

    def change_student_password(self, rollno, new_password):
        command = self.login_credentials_student.update().where(
            self.login_credentials_student.c.roll_no == rollno
        ).values(password=new_password)
        self.connection.execute(command)

    def change_recruiter_password(self, username, new_password):
        command = self.login_credentials_company.update().where(
            self.login_credentials_company.c.username == username
        ).values(password=new_password)
        self.connection.execute(command)

    def update_student_details(self, student_details):
        command = self.students.update().where(
            self.students.c.roll_no == student_details['rollno']
        ).values(student_details)
        self.connection.execute(command)

    def update_company_details(self, company_details):
        command = self.companies.update().where(self.companies.c.username == company_details['username']).values(
            company_details
        )
        self.connection.execute(command)

    def add_job(self, job_details, branches):
        jobs_command = self.jobs.insert().values(job_details)
        self.connection.execute(jobs_command)

        jobs_count_command = self.jobs.count()
        job_id = self.connection.execute(jobs_count_command).fetchone()[-1]
        for branch in branches:
            branches_eligible_command = self.branches_eligible.insert({'job_id': job_id, 'branch': branch})
            self.connection.execute(branches_eligible_command)

    def populate_branch_course_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        branch_course = pd.read_csv(path)
        branch_course_np = np.array(branch_course)

        unique_branch_course = []

        for row in branch_course_np:
            if row[0] in unique_branch_course:
                continue

            unique_branch_course.append(row[0])
            command = self.branch_course.insert().values(branch=row[0], course=row[1])
            self.connection.execute(command)

    def fetch_unique_branches_with_course(self, course):
        command = self.branches.select(
            whereclause=self.branches.c.course == course
        )

        result = self.connection.execute(command).fetchall()
        result_restructured = list(zip(*result))[1:]
        columns = [column.key for column in self.branches.columns]

        return dict(zip(columns, result_restructured))

    def populate_branches_eligible_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        branch_eli = pd.read_csv(path)
        branch_eli_np = np.array(branch_eli)

        unique_branch_eli = []

        for row in branch_eli_np:
            if row[0] in unique_branch_eli:
                continue

            unique_branch_eli.append(row[0])
            command = self.branches_eligible.insert().values(branch=row[0], course=row[1], job_id=row[2])
            self.connection.execute(command)

    def populate_companies_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        companies_data = pd.read_csv(path)
        companies_data_np = np.array(companies_data)

        unique_company_data = []

        for row in companies_data_np:
            if row[0] in unique_company_data:
                continue

            unique_company_data.append(row[0])
            command = self.companies.insert().values(company_tin=row[0], name=row[1], for_intern=row[2],
                                                     for_placement=row[3], for_training=row[4], contact_no=row[5],
                                                     email_id=row[6], location=row[7])
            self.connection.execute(command)

    def populate_jobs_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        print(type(job_np[0, 6]), type(job_np[0, 7]))
        for row in job_np:
            row[6] = int(row[6]) if not math.isnan(row[6]) else None
            row[7] = int(row[7]) if not math.isnan(row[7]) else None
            row[8] = int(row[8]) if not math.isnan(row[8]) else None
            command = self.jobs.insert().values(job_title=row[0], description=row[1],
                                                cutoff=row[2], deadline=row[3], dov=row[4],
                                                process_ongoing=row[5],
                                                package_placement=row[6], stipend_intern=row[7],
                                                duration_intern=row[8], location=row[9],
                                                for_intern=row[10], company_tin=row[11])
            self.connection.execute(command)

    def populate_login_credentials_student_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.login_credentials_student.insert().values(username=row[0], password=row[1],
                                                                     for_intern=row[2])
            self.connection.execute(command)

    def populate_login_credentials_company_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.login_credentials_company.insert().values(username=row[0], password=row[1])
            self.connection.execute(command)

    def populate_student_applies_for_job_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.student_applies_for_job.insert().values(roll_no=row[0], job_id=row[1],
                                                                   is_shortlisted=row[2], is_selected=row[3])
            self.connection.execute(command)

    def populate_student_applies_for_training_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.student_applies_for_training.insert().values(roll_no=row[0], training_id=row[1])
            self.connection.execute(command)

    def populate_student_manages_company_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.student_manages_company.insert().values(roll_no=row[0], company_tin=row[1])
            self.connection.execute(command)

    def populate_students_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.students.insert().values(roll_no=row[0], f_name=row[1], l_name=row[2], contact_no=row[3],
                                                    address_line_1=row[4], address_line_2=row[5], address_line_3=row[6],
                                                    pincode=row[7], gender=row[8], resume_link=row[9],
                                                    email_id=row[10], gpa_1=row[11], gpa_2=row[12], gpa_3=row[13],
                                                    gpa_4=row[14], gpa_5=row[15], gpa_6=row[16], gpa_7=row[17],
                                                    course=row[18], branch=row[19], category=row[20], grad_year=row[21],
                                                    dob=row[22], no_of_backlogs=row[23], marks_10=row[24],
                                                    marks_12=row[25], is_PC=row[26])
            self.connection.execute(command)

    def populate_trainings_table(self, filename):
        import pandas as pd
        import numpy as np
        import os
        path = os.path.join('csv_files', filename)
        job = pd.read_csv(path)
        job_np = np.array(job)

        for row in job_np:
            command = self.trainings.insert().values(subject_matter=row[0], date=row[1],
                                                     time=row[2], company_tin=row[3])
            self.connection.execute(command)

    def populate_tables(self):
        self.populate_geolocation_table('pincodes_delhi_haryana.csv')

        self.populate_students_table('students.csv')
        self.populate_companies_table('companies.csv')
        self.populate_trainings_table('trainings.csv')

        self.populate_branch_course_table('branch_course.csv')
        self.populate_login_credentials_company_table('login_credentials_company.csv')
        self.populate_login_credentials_student_table('login_credentials_student.csv')
        self.populate_student_applies_for_training_table('student_applies_for_training.csv')
        self.populate_student_manages_company_table('student_manages_company.csv')

        self.populate_jobs_table('jobs.csv')
        self.populate_branches_eligible_table('branches_eligible.csv')
        self.populate_student_applies_for_job_table('student_applies_for_job.csv')

    def fetch_applications_student(self, roll_no):
        get_job_id_command = select([self.student_applies_for_job.c.job_id]).where(
            self.student_applies_for_job.c.roll_no == roll_no
        )
        job_ids = self.connection.execute(get_job_id_command).fetchall()[:][-1]

        print(job_ids)

        company_tins = []
        for job_id in job_ids:
            get_company_id_command = select([self.jobs.c.company_tin]).where(
                self.jobs.c.job_id == job_id
            )
            company_tins.append(self.connection.execute(get_company_id_command).fetchone()[-1])

        company_names = []
        dovs = []
        for company_tin in company_tins:
            get_company_details_command = select([self.companies.c.name, self.companies.c.dov]).where(
                self.companies.c.company_tin == company_tin
            )
            result = self.connection.execute(get_company_details_command).fetchone()[1:]
            company_names.append((result[0]))
            dovs.append(result[1])

        job_profiles = []
        for job_id in job_ids:
            get_job_profile_command = select([self.jobs.c.title]).where(
                self.jobs.c.job_id == job_id
            )
            job_profiles.append(self.connection.execute(get_job_profile_command).fetchone()[-1])

        application_statuses = []
        for job_id in job_ids:
            get_application_status_command = select([self.student_applies_for_job.c.is_shortlisted,
                                                     self.student_applies_for_job.c.is_rejected,
                                                     self.student_applies_for_job.c.is_selected]).where(
                and_(
                    self.student_applies_for_job.job_id == job_id,
                    self.student_applies_for_job.roll_no == roll_no
                )
            )
            result = self.connection.execute(get_application_status_command).fetchone()[1:]
            if result[0]:
                application_statuses.append('Shortlisted')
            elif result[1]:
                application_statuses.append('Rejected')
            elif result[2]:
                application_statuses.append('Selected')
            else:
                application_statuses.append('Pending')

        return [company_names, job_profiles, application_statuses, dovs]

    def fetch_jobs_student(self, roll_no):
        get_branch_command = select([self.students.c.branch]).where(
            self.students.c.roll_no == roll_no
        )
        student_branch = self.connection.execute(get_branch_command).fetchone()[-1]
        print()
        print(student_branch)
        print()

        get_job_ids_command = select([self.branches_eligible.c.job_id]).where(
            self.branches_eligible.c.branch == student_branch
        )
        print(get_job_ids_command)
        job_ids = self.connection.execute(get_job_ids_command).fetchall()[0]

        deadlines = []
        company_tins = []
        print()
        print(job_ids)
        print()
        for job_id in job_ids:
            get_deadline_command = select([self.jobs.c.deadline, self.jobs.c.company_tin]).where(
                self.jobs.c.job_id == job_id
            )
            result = self.connection.execute(get_deadline_command).fetchone()
            print()
            print(result)
            print()
            deadlines.append(result[0])
            company_tins.append(result[1])

        names = []
        dovs = []
        for company_tin in company_tins:
            get_company_details_command = select([self.jobs.c.job_title, self.jobs.c.dov]).where(
                self.jobs.c.company_tin == company_tin
            )
            result = self.connection.execute(get_company_details_command).fetchone()
            names.append(result[0])
            dovs.append(result[1])

        print(names)
        print(deadlines)
        print(dovs)
        return [names, deadlines, dovs]

    def fetch_jobs_company(self, company_tin, for_intern):
        get_job_details_command = select([self.jobs.c.job_title,
                                          self.jobs.c.cutoff,
                                          self.jobs.c.stipend_intern if for_intern else self.jobs.c.package_placement,
                                          self.jobs.c.deadline]).where(
            self.jobs.c.company_tin == company_tin
        ).distinct()
        result = self.connection.execute(get_job_details_command).fetchall()[:][1:]
        job_profiles = result[:][0]
        cutoffs = result[:][1]
        stipends = result[:][2]
        deadlines = result[:][3]

        return [job_profiles, cutoffs, stipends, deadlines]

    def fetch_pc_responsible_for_company(self, company_tin):
        get_pc_command = select([self.student_manages_company.c.roll_no]).where(
            self.student_manages_company.c.company_tin == company_tin
        )

        pcs = self.connection.execute(get_pc_command).fetchall()[:][-1]

        return pcs

    def fetch_selections_company(self, company_tin):
        get_job_ids_command = select([self.jobs.c.job_id]).where(
            self.jobs.c.company_tin == company_tin
        )
        job_ids = self.connection.execute(get_job_ids_command).fetchall()[:][-1]

        job_ids_ret = []
        roll_nos = []
        for job_id in job_ids:
            get_roll_nos_command = select([self.student_applies_for_job.c.job_id,
                                           self.student_applies_for_job.c.roll_no]).where(
                and_(
                    self.student_applies_for_job.c.job_id == job_id,
                    self.student_applies_for_job.c.is_selected == True
                )
            )

            result = self.connection.execute(get_roll_nos_command).fetchall()[:][1:]
            job_ids_ret.append(result[0])
            roll_nos.append(result[1])

        job_titles = []
        for job_id in job_ids_ret:
            get_title_command = select([self.jobs.c.job_title]).where(
                self.jobs.c.job_id == job_id
            )
            job_titles.append(self.connection.execute(get_title_command).fetchone()[-1])

        names = []
        for roll_no in roll_nos:
            get_names_command = select([self.students.c.name]).where(
                self.students.c.roll_no == roll_no
            )

            names.append(self.connection.execute(get_names_command).fetchall()[:][-1])

        return [job_titles, roll_nos, names]

    def fetch_applications_company(self, company_tin):
        get_job_ids_command = select([self.jobs.c.job_id]).where(
            self.jobs.c.company_tin == company_tin
        )
        job_ids = self.connection.execute(get_job_ids_command).fetchall()[:][-1]

        job_ids_ret = []
        roll_nos = []
        for job_id in job_ids:
            get_roll_nos_command = select([self.student_applies_for_job.c.job_id,
                                           self.student_applies_for_job.c.roll_no]).where(
                and_(
                    self.student_applies_for_job.c.job_id == job_id,
                )
            )

            result = self.connection.execute(get_roll_nos_command).fetchall()[:][1:]
            job_ids_ret.append(result[0])
            roll_nos.append(result[1])

        job_titles = []
        for job_id in job_ids_ret:
            get_title_command = select([self.jobs.c.job_title]).where(
                self.jobs.c.job_id == job_id
            )
            job_titles.append(self.connection.execute(get_title_command).fetchone()[-1])

        names = []
        resumes = []
        for roll_no in roll_nos:
            get_details_command = select([self.students.c.name,
                                          self.students.c.resume_link]).where(
                self.students.c.roll_no == roll_no
            )

            result = self.connection.execute(get_details_command).fetchone()[1:]
            names.append(result[0])
            resumes.append(result[1])


if __name__ == '__main__':
    username = 'lruafctxgsjdsb'
    password = '7f6f9c5c0b160cc13f80a8955323e27b2e52647c62b0e0c94c9c023f99e74c1b'
    host = 'ec2-184-73-216-48.compute-1.amazonaws.com'
    database = 'dffdu4arjfs5ta'

    db = DBHelper(username, password, host, database, debug_mode=False)
    # db.create_tables()
    # db.populate_tables()
