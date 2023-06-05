from pydantic import BaseModel


class RelevantData(BaseModel):
    diagnosis_id: str
    resolved_date: str
