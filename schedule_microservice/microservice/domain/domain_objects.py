from pydantic import BaseModel
from uuid import UUID
import pandas as pd
from enum import Enum
from typing import Optional
import json

class Timeslot(BaseModel):
    timeslot_id: UUID
    doctor: UUID
    date: pd.Timestamp
    availability: bool # maybe should remove that


class Message(BaseModel):
    doctor: UUID
    date: pd.Timestamp

class OptMessage(BaseModel):
    timeslot_id: Optional[UUID] = None
    doctor: Optional[UUID] = None
    date: Optional[pd.Timestamp] = None
    availability: Optional[bool] = None

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Timeslot):
            return {
                'timeslot_id': str(obj.timeslot_id),
                'doctor': str(obj.doctor),
                'date': obj.date.strftime('%Y-%m-%d %H:%M:%S'),
                'availability': obj.availability
            }
        return super().default(obj)