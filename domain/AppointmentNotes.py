class AppointmentNotes:
    def __init__(self, patient_id, doctor_id, appointment_id, diagnosis=None):
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_id = appointment_id
        self.diagnosis = diagnosis
