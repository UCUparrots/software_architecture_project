import uvicorn
from fastapi import FastAPI
import sys
import os
import time
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain_objects import Appointment, Message, Reason
from domain import DomainLayer
from service import ServiceLayer



class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()
    
        @self.app.get('/get_appointments')
        def get_appointments(args: dict):
            optmessage = DomainLayer.create_opt_message(args)
            appointments = self.service.get_appointments(optmessage)
            return appointments

        @self.app.post('/new_appointment')
        def new_appointment(args: dict):
            appointment = DomainLayer.create_appointment(args)
            status = self.service.create_appointment(appointment)
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
    time.sleep(30)
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8080)
