import sqlite3
import datetime
from dateutil.relativedelta import relativedelta


class BaseORM:
    _SQLITE_VERSION_QUERY = "select sqlite_version();"
    _SELECT_QUERY = """select * from {} where {} = ?"""
    _SELECT_FIELD_QUERY = """select {} from {} where {} = ?"""
    _UPDATE_FIELD_QUERY = """update {} set {} = ? where {} = ?"""

    table_name = None
    connection = None

    def __init__(self):
        self.connection = sqlite3.connect('example_database.db')

    def read_database_version(self):
        try:
            cursor= self.get_cursor()
            cursor.execute(self._SQLITE_VERSION_QUERY)
            db_version = cursor.fetchone()
            print("You are connected to SQLite version: ", db_version)
            self.close_connection()
        except (Exception, sqlite3.Error) as error:
            print("Error while getting data", error)

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('example_database.db')
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def get_cursor(self):
        conn = self.get_connection()
        return conn.cursor()

class HospitalORM(BaseORM):
    table_name = 'Hospital'

    def _print_details(self, record):
        for row in record:
            print("    Id:", row[0])
            print("    Name:", row[1])
            print("    Joining Date:", row[3])
            print("    Specialty:", row[4])
            print("    Salary:", row[5])
            print("    Experience:", row[6])
    
    def get_hospital_detail(self, hospital_id):
        try:
            cursor = self.get_cursor()
            cursor.execute(
                self._SELECT_QUERY.format(self.table_name, "Hospital_Id"),
                (hospital_id,)
            )
            record = cursor.fetchall()
            print("Hospital record:")
            self._print_details()
            self.close_connection()
        except (Exception, sqlite3.Error) as error:
            print("Error while getting requested hospital data", error)

class DoctorORM(BaseORM):
    table_name = 'Doctor'

    def _print_details(self, record):
        for row in record:
            print("    Id:", row[0])
            print("    Name:", row[1])
            print("    Joining Date:", row[3])
            print("    Specialty:", row[4])
            print("    Salary:", row[5])
            print("    Experience:", row[6])

    def get_doctor(self, id_to_search, column_to_search):
        try:
            cursor = self.get_cursor()
            cursor.execute(
                self._SELECT_QUERY.format(self.table_name, column_to_search),
                (id_to_search,)
            )
            record = cursor.fetchall()
            print("Doctor record:")
            self._print_details(record)
            self.close_connection()
        except (Exception, sqlite3.Error) as error:
            print("Error while getting requested doctor data", error)

    def update_years_experience(self, doctor_id):
        try:
            cursor = self.get_cursor()
            cursor.execute(
                self._SELECT_FIELD_QUERY.format("Joining_Date", self.table_name, "Doctor_Id"),
                (doctor_id,)
            )
            joining_date = cursor.fetchone()
            
            # calculate Experience in years
            joining_date_1 = datetime.datetime.strptime(
                ''.join(map(str, joining_date)),
                '%Y-%m-%d'
            )
            experience = relativedelta(
                datetime.datetime.now(),
                joining_date_1
            ).years

            # Update doctor's Experience now
            cursor = self.get_cursor()
            cursor.execute(
                self._UPDATE_FIELD_QUERY.format(self.table_name, "Experience", "Doctor_Id"),
                (experience, doctor_id,)
            )
            self.get_connection().commit()
            print("Doctor Id:", doctor_id, " Experience updated to ", experience, " years")
            self.close_connection()
        except (Exception, sqlite3.Error) as error:
            print("Error while getting requested doctor data", error)

if __name__ == "__main__":
    print("Question 1: Print Database version")

    do = DoctorORM()

    do.read_database_version()
    do.get_doctor(2, 'Hospital_Id')
    

    do.update_years_experience(104)
    do.get_doctor(104, 'Doctor_Id')
    