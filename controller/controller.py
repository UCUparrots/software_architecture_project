import uvicorn
from fastapi import FastAPI
import requests
import sys
sys.path.append('../service')
from service.service import CardService
sys.path.append('../domain')
from domain.AppointmentNotes import AppointmentNotes



class CardController:
    def __init__(self, app: FastAPI):
        @app.get("/medcard_service")
        async def get_patient_information(uuid: str):
            return CardService().form_medcard(uuid)

        @app.post("/medcard_service")
        async def update_medical_card(data: AppointmentNotes):
            return CardService().update_medcard(data)


def startup():
    app = FastAPI()

    CardController(app)
    return app


if __name__ == '__main__':
    uvicorn.run(startup(), host="localhost", port=8000)
