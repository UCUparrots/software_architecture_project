import psycopg2
import sys
from os import path
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from domain.AppointmentNotes import AppointmentNotes



class Repository:
    def __init__(self):
        self.connection = psycopg2.connect(database='medcard_db', user='postgres',
                        password='postgres', host='postgres-medcard')
        self.cursor = self.connection.cursor()

    def get_patient_appointments(self, patient_id) -> list:
        sql = f"SELECT * FROM DiagnosisHistory WHERE patient_id='{patient_id}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        import pprint
        pprint.pprint(result)
        return result

    def get_user_info(self, user_id):
        sql = f"SELECT * FROM UserTable WHERE user_id='{user_id}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if not result:
            uid, email, ph, name, surname, phone, birthdate, phd, spec = [None for _ in range(9)]
        else:
            uid, email, ph, name, surname, phone, birthdate, phd, spec = result[0]
        info = {'name': name, 'surname': surname, 'phone': phone, 'email': email, 'birthdate': birthdate, 'doctor_phd': phd, 'doctor_specialization': spec}
        return info

    def add_info(self, apps: AppointmentNotes) -> bool:
        if not apps.is_relevant:
            resolved_date = f"'{apps.resolved_date}'"
        else:
            resolved_date = "NULL"
        sql = f"""INSERT INTO DiagnosisHistory (patient_id, doctor_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date)
VALUES
    ('{apps.patient_id}', '{apps.doctor_id}', '{apps.diagnosis}', '{apps.start_date}', '{apps.notes}', '{apps.medicine}', {apps.is_relevant}, {resolved_date});
"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except:
            return False

    def update_is_relevant(self, appointment_id: str) -> bool:
        # sql =
        # self.cursor.execute(sql)
        return True
