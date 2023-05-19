import sys
from os import path
ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from domain.AppointmentNotes import AppointmentNotes
from domain.MedCardInfo import MedCardInfo
from repository.helpers import get_doctor_info, get_patient_info, get_patient_appointments, add_info, update_is_relevant


class CardService:

    def form_medcard(self, patient_uuid):
        """
        :param patient_uuid: ID of the patient.
        :return: MedCardInfo object.
        """
        user = get_patient_info(patient_uuid)
        apps = self.form_appointment_info(get_patient_appointments(patient_uuid))

        return vars(MedCardInfo(user['name'], user['email'],
                                user['phone'], user['birthdate'], apps))

    @staticmethod
    def form_appointment_info(apps) -> list:
        appointments = []
        for app in apps:
            doctor = get_doctor_info(app['doctor_id'])
            appointments.append({'doctor_type': doctor['doctor_specialization'],
                                 'doctor_name': doctor['name'],
                                 # 'appointment_type': app['type'],
                                 'diagnosis': app['diagnosis'],
                                 'notes_from_doctor': app['notes_from_doctor'],
                                 'is_relevant': app['is_relevant'],
                                 'resolved_date': app['resolved_date'],
                                 'start_date': app['start_date'],
                                 'medicine': app['medicine']})
        return appointments

    @staticmethod
    def update_medcard(app_notes: AppointmentNotes) -> bool:
        # add appointment to database
        return add_info(app_notes)

    @staticmethod
    def resolve_sickness(patient_id, appointment_id) -> bool:
        return update_is_relevant({'patient_id': patient_id, 'appointment_id': appointment_id})
