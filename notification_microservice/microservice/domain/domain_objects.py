from pydantic import BaseModel
from uuid import UUID


class Message(BaseModel):
    id: UUID

class Email(BaseModel):
    email: str
    firstname: str
    lastname: str
    phone: str
    