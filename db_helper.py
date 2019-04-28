# change test database to production

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, Float, \
    Date, Time, DateTime, MetaData, ForeignKey
from sqlalchemy.sql.expression import select
from sqlalchemy import and_, or_


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
            Column('resume_uploaded', Boolean),
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
            Column('job_id', String, primary_key=True),
            Column('job_title', String),
            Column('description', String),
            Column('cutoff', Float),
            Column('deadline', DateTime(timezone=True)),
            Column('dov', Date),
            Column('process_ongoing', Boolean),
            Column('package_placement', Integer),
            Column('stipend_intern', Integer),
            Column('duration_intern', Integer),
            Column('company_tin', String, ForeignKey(self.companies.c.company_tin))
        )

        self.branches_eligible = Table(
            'branches_eligible', self.meta,
            Column('branch', String, primary_key=True),
            Column('course', String, primary_key=True),
            Column('job_id', String, primary_key=True)
        )

        self.trainings = Table(
            'trainings', self.meta,
            Column('training_id', String, primary_key=True),
            Column('subject_matter', String),
            Column('date', Date),
            Column('time', Time(timezone=True)),
            Column('company_tin', String, ForeignKey(self.companies.c.company_tin))
        )

        self.student_applies_for_job = Table(
            'student_applies_for_job', self.meta,
            Column('roll_no', String, primary_key=True),
            Column('job_id', String, primary_key=True),
            Column('is_shortlisted', Boolean),
            Column('is_selected', Boolean)
        )

        self.student_applies_for_training = Table(
            'student_applies_for_training', self.meta,
            Column('roll_no', String, primary_key=True),
            Column('training_id', String, primary_key=True),
        )

        self.branches = Table(
            'branches', self.meta,
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

        if row:
            if row[-1] == password:
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
        result = self.connection.execute(command).fetchone()[1:]
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
        command = self.students.update().where(self.students.c.roll_no == student_details['rollno']).values(
            student_details
        )
        self.connection.execute(command)

    def update_company_details(self, company_details):
        command = self.companies.update().where(self.companies.c.username == company_details['username']).values(
            company_details
        )
        self.connection.execute(command)

    def add_job(self, job_details, branches):
        jobs_command = self.jobs.insert().values(job_details)
        self.connection.execute(jobs_command)

        braches_eligible_command = self.branches_eligible.insert().values()

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
            command = self.branches.insert().values(branch=row[0], course=row[1])
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

        unique_jobs = []

        for row in job_np:
            if row[0] in unique_jobs:
                continue

            unique_jobs.append(row[0])
            command = self.jobs.insert().values(job_id=row[0], job_title=row[1], description=row[2],
                                                cutoff=row[3], deadline=row[4], dov=row[5],
                                                process_ongoing=row[6],
                                                package_placement=row[7], stipend_intern=row[8],
                                                duration_intern=row[9], company_tin=row[10])
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
                                                    pincode=row[7], gender=row[8], resume_uploaded=row[9],
                                                    email_id=row[10], gpa_1=row[11], gpa_2=row[12], gpa_3=row[13],
                                                    gpa_4=row[14], gpa_5=row[15], gpa_6=row[16], gpa_7=row[17],
                                                    course=row[18], branch=row[19], category=row[20], grad_year=row[21],
                                                    dob=row[22], no_of_backlogs=row[23], marks_10=row[24],
                                                    marks_12=row[25],  is_PC=row[26])
            self.connection.execute(command)

    def populate_trainings_table(self, filename):
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
            command = self.trainings.insert().values(training_id=row[0], subject_matter=row[1], date=row[2],
                                                     time=row[3], company_tin=row[4])
            self.connection.execute(command)


if __name__ == '__main__':
    username = 'lruafctxgsjdsb'
    password = '7f6f9c5c0b160cc13f80a8955323e27b2e52647c62b0e0c94c9c023f99e74c1b'
    host = 'ec2-184-73-216-48.compute-1.amazonaws.com'
    database = 'dffdu4arjfs5ta'

    db = DBHelper(username, password, host, database, debug_mode=True)
    # db.create_tables()
    # db.populate_geolocation_table()
