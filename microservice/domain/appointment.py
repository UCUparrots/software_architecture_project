from pydantic import BaseModel
from type import Type
from uuid import UUID


class Appointment(BaseModel):
    id: UUID
    doctor: UUID
    patient: UUID
    type: Type
