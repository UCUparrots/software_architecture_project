import psycopg2
import logging
import sys
from os import path
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from domain.AppointmentNotes import AppointmentNotes
from domain.RelevantUpdateData import RelevantData
from domain.User import UserInfo


class Repository:
    def __init__(self):
        self.connection = psycopg2.connect(database='medcard_db', user='postgres',
                        password='postgres', host='postgres-medcard')
        self.cursor = self.connection.cursor()

    def add_user_info(self, user: UserInfo):
        sql = f"""INSERT INTO UserTable (user_id, email, name, surname, phone, birthdate, doctorPhD, doctor_specialization)
        VALUES
            ('{user.user_id}', '{user.email}', '{user.name}','{user.surname}', '{user.phone}', '{user.birthdate}', '{user.doctorPhD}', '{user.doctor_specialization}');
        """
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            logging.error(f"Error occurred during update: {str(e)}")
            return False

    def get_patient_appointments(self, patient_id) -> list:
        sql = f"SELECT * FROM DiagnosisHistory WHERE patient_id='{patient_id}';"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def get_user_info(self, user_id):
        sql = f"SELECT * FROM UserTable WHERE user_id='{user_id}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if not result:
            uid, email, name, surname, phone, birthdate, phd, spec = [None for _ in range(8)]
        else:
            uid, email, name, surname, phone, birthdate, phd, spec = result[0]
        info = {'name': name, 'surname': surname, 'phone': phone,
                'email': email, 'birthdate': birthdate, 'doctor_phd': phd,
                'doctor_specialization': spec}
        return info

    def add_info(self, apps: AppointmentNotes) -> bool:
        check = f"SELECT COUNT(*) AS count FROM UserTable WHERE user_id = '{apps.patient_id}';"
        self.cursor.execute(check)
        result = self.cursor.fetchall()
        if result[0][0] == 0:
            return False

        if not apps.is_relevant:
            resolved_date = f"'{apps.resolved_date}'"
        else:
            resolved_date = "NULL"
        sql = f"""INSERT INTO DiagnosisHistory (patient_id, doctor_id, diagnosis_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date)
VALUES
    ('{apps.patient_id}', '{apps.doctor_id}', '{apps.diagnosis_id}','{apps.diagnosis}', '{apps.start_date}', '{apps.notes}', '{apps.medicine}', {apps.is_relevant}, {resolved_date});
"""
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            return True
        except Exception as e:
            logging.error(f"Error occurred during update: {str(e)}")
            return False


    def update_is_relevant(self, info: RelevantData) -> bool:
        sql = f"UPDATE DiagnosisHistory SET is_relevant = 0, resolved_date = %s WHERE diagnosis_id = %s;"
        parameters = (info.resolved_date, info.diagnosis_id)

        try:
            self.cursor.execute(sql, parameters)
            self.connection.commit()
            return True
        except Exception as e:
            logging.error(f"Error occurred during update: {str(e)}")
        return False