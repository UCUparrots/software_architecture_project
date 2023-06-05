import uvicorn
from fastapi import FastAPI
import sys
from os import path

ROOT_DIR = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(ROOT_DIR)
from service.service import CardService
from domain.AppointmentNotes import AppointmentNotes
from domain.RelevantUpdateData import RelevantData



class CardController:
    def __init__(self, app: FastAPI):
        @app.get("/form_medcard")
        async def get_patient_information(uuid: str):
            return CardService().form_medcard(uuid)

        @app.post("/update_medcard")
        async def update_medical_card(data: AppointmentNotes):
            return CardService().update_medcard(data)

        @app.post("/update_diagnosis_status")
        async def update_medical_card(data: RelevantData):
            return CardService().resolve_sickness(data)


def startup():
    app = FastAPI()

    CardController(app)
    return app


if __name__ == '__main__':
    uvicorn.run(startup(), host="0.0.0.0", port=8080)
