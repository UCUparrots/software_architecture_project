from pydantic import BaseModel

class UserInfo(BaseModel):
    user_id: str
    email: str
    name: str
    surname: str
    phone: str
    birthdate: str
    doctorPhD: str
    doctor_specialization: str
