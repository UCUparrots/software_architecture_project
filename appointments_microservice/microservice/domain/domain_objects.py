from pydantic import BaseModel
from reason import Reason
from uuid import UUID
import pandas as pd
from enum import Enum
from typing import Optional
import json

class Reason(Enum):
    CONSULTATION = 1
    OPERATION = 2
    MANIPULATION = 3


class Appointment(BaseModel):
    id: UUID
    doctor: UUID
    patient: UUID
    type: Reason
    date: pd.Timestamp


class Message(BaseModel):
    doctor: UUID
    patient: UUID
    date: pd.Timestamp
    type: Reason


class OptMessage(BaseModel):
    id: Optional[UUID] = None
    doctor: Optional[UUID] = None
    patient: Optional[UUID] = None
    type: Optional[Reason] = None
    date: Optional[pd.Timestamp] = None


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Appointment):
            return {
                'id': str(obj.id),
                'doctor': str(obj.doctor),
                'patient': str(obj.patient),
                'type': obj.type.value,
                'date': obj.date.strftime('%Y-%m-%d %H:%M:%S')
            }
        return super().default(obj)