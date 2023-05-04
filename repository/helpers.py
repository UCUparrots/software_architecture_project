import sys
sys.path.append('../domain')
from domain.AppointmentNotes import AppointmentNotes

#  Gets info from Patients' diagnosis history database


def get_patient_appointments(patient_id):
    """
    :param patient_id:
    :return: json with all appointments of the patient.
    """
    return None


def get_patient_info(patient_id):
    return None


def get_doctor_info(doctor_id):
    return None


def add_info(apps: AppointmentNotes) -> bool:
    return False


def update_is_relevant(ids: dict) -> bool:
    """
    :param ids: json with patient_id and appointment_id
    :return: True if successfully updated diagnosis status.
    """
    return False
