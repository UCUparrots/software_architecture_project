from pydantic import BaseModel
from reason import Reason
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
    timestamp_id: Optional[UUID] = None
    doctor: Optional[UUID] = None
    date: Optional[pd.Timestamp] = None


# class CustomEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Appointment):
#             return {
#                 'id': str(obj.id),
#                 'doctor': str(obj.doctor),
#                 'patient': str(obj.patient),
#                 'type': obj.type.value,
#                 'date': obj.date.strftime('%Y-%m-%d %H:%M:%S')
#             }
#         return super().default(obj)