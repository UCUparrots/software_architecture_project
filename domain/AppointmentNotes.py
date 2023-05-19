from pydantic import BaseModel


class AppointmentNotes(BaseModel):
    patient_id: str
    doctor_id: str
    appointment_id: str
    diagnosis: str
