import uvicorn
from fastapi import FastAPI
import sys
import os
import time
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain_objects import SignUp, LogIn, UserInfoUpdate
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

        @self.app.post('/signup')
        def signup(args: dict):
            print("SIGNING UP ATTEMPT")
            user = DomainLayer.create_signup(args)
            status = self.service.save_user(user)
            print("SIGNUP STATUS", status)
            return status
        
        @self.app.post('/login')
        def login(args: dict):
            user = DomainLayer.create_login(args)
            status = self.service.authenticate_user(user)
            return status

        @self.app.post('/update_info')
        def update_user(args: dict):
            user = DomainLayer.create_user_update_info(args)
            status = self.service.update_user(user)
            return status
        
        @self.app.get('/get_info')
        def update_user(args: dict):
            user = DomainLayer.create_user_id_info(args)
            status = self.service.get_user_info(user)
            return status
        


if __name__ == '__main__':
    time.sleep(1)
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8080)
