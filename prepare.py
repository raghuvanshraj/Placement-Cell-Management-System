# change test database to production

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Boolean, Float, \
    Date, Time, DateTime, MetaData, ForeignKey

debug_mode = True


def create_connection(username, password, host, database):
    try:
        uri = 'postgres://' + username + ':' + password + '@' + host + '/' + database
        engine = create_engine(uri, echo=debug_mode)
        connection = engine.connect()
    except Exception as err:
        print('Connection Failed:', err)
        return None, None

    return engine, connection


def create_tables(engine):
    meta = MetaData()

    login_credentials = Table(
        'login_credentials', meta,
        Column('username', String, primary_key=True),
        Column('password', String, nullable=False)
    )

    geolocation = Table(
        'geolocation', meta,
        Column('pincode', String, primary_key=True),
        Column('city', String),
        Column('state', String)
    )

    students = Table(
        'students', meta,
        Column('roll_no', String, primary_key=True),
        Column('f_name', String),
        Column('l_name', String),
        Column('contact_no', String),
        Column('address_line_1', String),
        Column('address_line_2', String),
        Column('address_line_3', String),
        Column('pincode', String, ForeignKey(geolocation.c.pincode)),
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

    companies = Table(
        'companies', meta,
        Column('company_tin', String, primary_key=True),
        Column('name', String),
        Column('for_intern', Boolean),
        Column('for_placement', Boolean),
        Column('for_training', Boolean),
        Column('contact_no', String),
        Column('email_id', String),
        Column('location', String),
    )

    student_manages_company = Table(
        'student_manages_company', meta,
        Column('roll_no', String, primary_key=True),
        Column('company_tin', String, primary_key=True)
    )

    jobs = Table(
        'jobs', meta,
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
        Column('company_tin', String, ForeignKey(companies.c.company_tin))
    )

    branches_eligible = Table(
        'branches_eligible', meta,
        Column('branch', String, primary_key=True),
        Column('job_id', String, primary_key=True)
    )

    trainings = Table(
        'trainings', meta,
        Column('training_id', String, primary_key=True),
        Column('subject_matter', String),
        Column('date', Date),
        Column('time', Time(timezone=True)),
        Column('company_tin', String, ForeignKey(companies.c.company_tin))
    )

    student_applies_for_job = Table(
        'student_applies_for_job', meta,
        Column('roll_no', String, primary_key=True),
        Column('job_id', String, primary_key=True),
        Column('is_shortlisted', Boolean),
        Column('is_selected', Boolean)
    )

    student_applies_for_training = Table(
        'student_applies_for_training', meta,
        Column('roll_no', String, primary_key=True),
        Column('training_id', String, primary_key=True),
    )

    meta.create_all(engine)


if __name__ == '__main__':
    username = 'lruafctxgsjdsb'
    password = '7f6f9c5c0b160cc13f80a8955323e27b2e52647c62b0e0c94c9c023f99e74c1b'
    host = 'ec2-184-73-216-48.compute-1.amazonaws.com'
    database = 'dffdu4arjfs5ta'

    # engine, connection = create_connection(username, password, host, database)
    # if engine:
    #     create_tables(engine)
