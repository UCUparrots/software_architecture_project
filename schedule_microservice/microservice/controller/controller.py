import uvicorn
from fastapi import FastAPI
import sys
import os
import time
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain_objects import Timeslot, Message, OptMessage # no idea if that's what I need
from domain import DomainLayer
from service import ServiceLayer


class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()
    
        @self.app.post('/new_timeslots')
        def new_timeslots(args: dict):
            timeslots = DomainLayer().create_timeslots(args)
            print(timeslots)
            status = self.service.new_timeslots(timeslots)
            return status
        
        @self.app.get('/get_timeslots')
        def get_timeslots(args: dict):
            optmessage = DomainLayer.create_opt_message(args)
            timeslots = self.service.get_timeslots(optmessage)
            return timeslots
        
        @self.app.post('/delete_timeslot')
        def delete_timeslot(args: dict):
            timeslot__id = DomainLayer.get_timeslot_id(args)
            status = self.service.delete_timeslot(timeslot__id)
            return status


if __name__ == '__main__':
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8080)
