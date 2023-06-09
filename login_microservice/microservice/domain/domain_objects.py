from pydantic import BaseModel
from uuid import UUID
import pandas as pd
from typing import Optional
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
    doctor_phd: Optional[str]
    doctor_specialization: Optional[str]

class LogIn(BaseModel):
    email: str
    password_hash: str
    login_as_doctor: bool

class UserInfoUpdate(BaseModel):
    user_id: UUID
    email: str
    phone: str
    birthdate: date
    is_doctor: bool
    doctor_phd: Optional[str]
    doctor_specialization: Optional[str]

class UserID(BaseModel):
    user_id: UUID
