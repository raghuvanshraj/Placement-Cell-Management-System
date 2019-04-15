# change test database to production

from sqlalchemy import create_engine
from tables import login_credentials_student, login_credentials_company, geolocation, \
    students, student_applies_for_job, student_applies_for_training, student_manages_company, \
    companies, jobs, branches_eligible, trainings

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


def login_student(connection, username, password):
    command = login_credentials_student.select(whereclause=login_credentials_student.c.username == username)
    result = connection.execute(command)
    row = result.fetchone()

    if row:
        if row[-1] == password:
            return True
        else:
            print('Incorrect Password')
            return False
    else:
        print('Incorrect Username')
        return False


def login_company(connection, username, password):
    command = login_credentials_company.select(whereclause=login_credentials_company.c.username == username)
    result = connection.execute(command)
    row = result.fetchone()

    if row:
        if row[-1] == password:
            return True
        else:
            print('Incorrect Password')
            return False
    else:
        print('Incorrect Username')
        return False


if __name__ == '__main__':
    username = 'lruafctxgsjdsb'
    password = '7f6f9c5c0b160cc13f80a8955323e27b2e52647c62b0e0c94c9c023f99e74c1b'
    host = 'ec2-184-73-216-48.compute-1.amazonaws.com'
    database = 'dffdu4arjfs5ta'

    engine, connection = create_connection(username, password, host, database)

    # code here
    # login_student(connection, 'raghu', 'password')

    connection.close()
