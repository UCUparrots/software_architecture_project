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

MEDCARD_URL_PLACEHOLDER = "http://localhost:8081/"


class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()

        @self.app.post('/signup')
        def signup(args: dict):
            user = DomainLayer.create_signup(args)
            status = self.service.save_user(user)
            self.service.post_medcard_info(user, MEDCARD_URL_PLACEHOLDER)
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
            self.service.post_update_to_medcard(user, MEDCARD_URL_PLACEHOLDER)
            return status
        
        @self.app.get('/get_info')
        def get_user(user_id: UUID):
            user = DomainLayer.create_user_id_info({"user_id": str(user_id)})
            status = self.service.get_user_info(user)
            return status
        


if __name__ == '__main__':
    time.sleep(20)
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8086)
