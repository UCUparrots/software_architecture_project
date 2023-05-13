from pydantic import BaseModel
from reason import Reason
from uuid import UUID
import pandas as pd
from enum import Enum
from typing import Optional

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

class OptMessage(BaseModel):
    doctor: Optional[UUID] = None
    patient: Optional[UUID] = None
    date: Optional[pd.Timestamp] = None
    type: Optional[Reason] = None
    id: Optional[UUID] = None
