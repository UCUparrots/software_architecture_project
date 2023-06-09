import sys
from os import path

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from domain.AppointmentNotes import AppointmentNotes
from domain.MedCardInfo import MedCardInfo
from domain.RelevantUpdateData import RelevantData
from domain.User import UserInfo
from repository.repository import Repository


class CardService:
    def __init__(self):
        self.repository = Repository()

    def form_medcard(self, patient_uuid) -> dict:
        """
        :param patient_uuid: ID of the patient.
        :return: vars of MedCardInfo object.
        """
        user = self.repository.get_patient_appointments(patient_uuid)
        apps = self.form_appointment_info(user)
        user_info = self.repository.get_user_info(patient_uuid)
        if not user_info:
            print('user onfo', user_info)
            return None

        return vars(MedCardInfo(user_info['name'] + ' ' + user_info['surname'], user_info['email'],
                                user_info['phone'], user_info['birthdate'], apps))

    def parse_appointment_tuple(self, appoint: tuple) -> dict:
        if not appoint:
            return {}
        patient_id, doctor_id, diagnosis_id, diagnosis, start_date, notes, medicine, is_relevant, resolved_date = appoint

        return {'patient_id': patient_id, 'doctor_id': doctor_id, 'diagnosis_id': diagnosis,
                'diagnosis': diagnosis, 'start_date': start_date,
                'notes': notes, 'medicine': medicine, 'is_relevant': is_relevant,
                'resolved_date': resolved_date}


    def form_appointment_info(self, apps) -> list:
        if not apps:
            return []
        appointments = []
        for app in apps:
            app = self.parse_appointment_tuple(app)
            doctor = self.repository.get_user_info(app['doctor_id'])
            appointments.append({'doctor_type': doctor['doctor_specialization'],
                                 'doctor_name': doctor['name'],
                                 'diagnosis': app['diagnosis'],
                                 'notes_from_doctor': app['notes'],
                                 'is_relevant': app['is_relevant'],
                                 'resolved_date': app['resolved_date'],
                                 'start_date': app['start_date'],
                                 'medicine': app['medicine']})
        return appointments

    def update_medcard(self, app_notes: AppointmentNotes) -> bool:
        # add appointment to database
        return self.repository.add_info(app_notes)

    def resolve_sickness(self, info: RelevantData) -> bool:
        return self.repository.update_is_relevant(info)

    def add_user_to_db(self, info: UserInfo) -> bool:
        return self.repository.add_user_info(info)
