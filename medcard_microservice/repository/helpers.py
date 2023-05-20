import sys
from os import path
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from domain.AppointmentNotes import AppointmentNotes

#  Gets info from Patients' diagnosis history database


def get_patient_appointments(patient_id) -> list:
    """
    :param patient_id:
    :return: json with all appointments of the patient.
    """
    return [{'doctor_id': '1', 'diagnosis': 'flu', 'start_date': 'yesterday',
             'notes_from_doctor': 'blablabla', 'medicine': 'strepsils',
             'is_relevant': True, 'resolved_date': None},
            {'doctor_id': '2', 'diagnosis': 'covid', 'start_date': '05.05.2020',
             'notes_from_doctor': 'blablabla', 'medicine': 'strepsils',
             'is_relevant': False, 'resolved_date': '05.06.2020'},
            ]


def get_patient_info(patient_id):
    return {'name': 'Alina', 'email': 'a@ucu.edu.ua', 'birthdate': '01.01.1995',
            'phone': '1234567890'}


def get_doctor_info(doctor_id):
    return {'name': 'Doctor', 'email': 'doctor@ucu.edu.ua', 'birthdate': '01.01.1995',
            'phone': '1234567890', 'doctor_PhD': 'UCU', 'doctor_specialization': 'Cool'}


def add_info(apps: AppointmentNotes) -> bool:
    return True


def update_is_relevant(ids: dict) -> bool:
    """
    :param ids: json with patient_id and appointment_id
    :return: True if successfully updated diagnosis status.
    """
    return True


import psycopg2



class Repository:
    def __init__(self):
        self.connection = psycopg2.connect(database='test_db', user='postgres',
                        password='postgres', host='postgres-1')
        self.cursor = self.connection.cursor()

    def get_patient_appointments(self, patient_id) -> list:
        sql = f"SELECT * FROM DiagnosisHistory WHERE patient_id='{patient_id}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
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
        start_date, notes, medicine, is_relevant, resolved_date = '2023-05-20 10:00:00', 'notes_1', '', 1, '2023-05-21 12:00:00'
        sql = f"""INSERT INTO DiagnosisHistory (patient_id, doctor_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date)
VALUES
    ('{apps.patient_id}', '{apps.doctor_id}', '{apps.diagnosis}', '{start_date}', '{notes}', '{medicine}', {is_relevant}, '{resolved_date}');
"""
        self.cursor.execute(sql)

        sql = f"""INSERT INTO UserTable (user_id, email, password_hash, name, surname, phone, birthdate, doctorPhD, doctor_specialization)
        VALUES
            ('{apps.patient_id}', '', '', 'New', 'Sur', '+380', '{'2023-05-20 10:00:00'}', 'doctorPhD', 'doctor_specialization');
        """
        self.cursor.execute(sql)
        return True

    def update_is_relevant(self, appointment_id: str) -> bool:
        # sql =
        # self.cursor.execute(sql)
        return True
