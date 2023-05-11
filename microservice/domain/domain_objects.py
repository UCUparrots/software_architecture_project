from pydantic import BaseModel
from reason import Reason
from uuid import UUID
import pandas as pd
from enum import Enum

class Reason(Enum):
    CONSULTATION = 1
    OPERATION = 2
    MANIPULATION = 3


class Appointment(BaseModel):
    id: UUID
    doctor: UUID
    patient: UUID
    date: pd.Timestamp
    type: Reason


class Message(BaseModel):
    doctor: UUID
    patient: UUID
    date: pd.Timestamp
    type: Reason
