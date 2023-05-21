from pydantic import BaseModel


class AppointmentNotes(BaseModel):
    patient_id: str
    doctor_id: str
    diagnosis_id: str
    diagnosis: str
    start_date: str
    notes: str
    medicine: str
    is_relevant: int
    resolved_date: str
