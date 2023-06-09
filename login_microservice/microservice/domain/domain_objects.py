from pydantic import BaseModel
from uuid import UUID
import pandas as pd
from typing import Union
import json
from datetime import date


class SignUp(BaseModel):
    user_id: UUID
    password_hash: str
    email: str
    firstname: str
    lastname: str
    phone: str
    birthdate: date
    is_doctor: bool
    notification: bool
    doctor_phd:  Union[str, None] = None
    doctor_specialization:  Union[str, None] = None

class LogIn(BaseModel):
    email: str
    password_hash: str
    login_as_doctor: bool

class UserInfoUpdate(BaseModel):
    user_id: UUID
    email:  Union[str, None] = None
    phone:  Union[str, None] = None
    birthdate: Union[date, None] = None
    is_doctor: Union[bool, None] = None
    doctor_phd:  Union[str, None] = None
    doctor_specialization:  Union[str, None] = None

class UserID(BaseModel):
    user_id: UUID
