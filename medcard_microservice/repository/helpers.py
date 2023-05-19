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
