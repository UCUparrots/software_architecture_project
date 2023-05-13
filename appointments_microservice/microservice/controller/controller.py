import uvicorn
from fastapi import FastAPI
import sys
import os
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain_objects import Appointment, Message, Reason
from domain import DomainLayer
from service import ServiceLayer



class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()
    
        @self.app.post('/get_appointments')
        def get_appointments(args: dict):
            message = DomainLayer.create_message(args)
            appointments = self.service.get_appointments(message)
            return appointments.to_json()

        @self.app.post('/new_appointment')
        def new_appointment(args: Message):
            message = DomainLayer.create_message(args)
            status = self.service.create_appointment(message)
            return status
        
        @self.app.post('/delete_appointment')
        def delete_appointment(args: dict):
            appointment_id = DomainLayer.get_appointment_id(args)
            status = self.service.delete_appointment(appointment_id)
            return status

        @self.app.post('/confirm_appointment')
        def confirm_appointment(args: dict):
            appointment_id = DomainLayer.get_appointment_id(args)
            status = self.service.confirm_appointment(appointment_id)
            return status


if __name__ == '__main__':
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=50000)
