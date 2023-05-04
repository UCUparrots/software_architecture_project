import sys
sys.path.append('../domain')
from domain.AppointmentNotes import AppointmentNotes
from domain.MedCardInfo import MedCardInfo
sys.path.append('../repository')
from repository.helpers import get_doctor_info, get_patient_info, get_patient_appointments, add_info, update_is_relevant


class CardService:

    def form_medcard(self, patient_uuid):
        """
        :param patient_uuid: ID of the patient.
        :return: MedCardInfo object.
        """
        user = get_patient_info(patient_uuid)
        apps = self.form_appointment_info(get_patient_appointments(patient_uuid))

        return MedCardInfo(user.name, user.email, user.phone, user.birthdate, apps)

    @staticmethod
    def form_appointment_info(apps) -> list:
        appointments = []
        for app in apps:
            doctor = get_doctor_info(app.doctor_id)
            appointments.append({'doctor_type': doctor.type, 'doctor_name': doctor.name,
                                 'appointment_type': app.type, 'diagnosis': app.diagnosis, 'notes': app.notes})
        return appointments

    @staticmethod
    def update_medcard(app_notes: AppointmentNotes) -> bool:
        # add appointment to database
        return add_info(app_notes)

    @staticmethod
    def resolve_sickness(patient_id, appointment_id) -> bool:
        return update_is_relevant({'patient_id': patient_id, 'appointment_id': appointment_id})
