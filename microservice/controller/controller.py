import uvicorn
from fastapi import FastAPI
import requests
from random import randint
# import sys
# sys.path.append('../../app')
from domain.appointment import Appointment
# from facadeService import ServiceLayer



class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        # self.service = ServiceLayer()
        # self.LOGGING_URL = ['http://logging-service-1:8081/', 'http://logging-service-2:8081/', 'http://logging-service-3:8081/']
        # # self.LOGGING_URL = ['http://logging-service:8081/']
        # self.MESSAGES_URL = 'http://messages-service:8082/'

        # @self.app.get('/')
        # async def get():
            # logging_url = self.LOGGING_URL[randint(0,2)]
            
            # ans1 = requests.get(url=logging_url)
            
            # ans2 = requests.get(url=self.MESSAGES_URL)
            # return {"logging":ans1.json(), "messages":ans2.json()}

        # @self.app.post('/')
        # async def post(args: Message):
        #     # logging_url = self.LOGGING_URL[0]
        #     # print(args)
        #     message = self.service.create_message(args)
        #     dct = requests.post(url=self.LOGGING_URL[randint(0,2)], json = {"key": message.key, "msg": message.msg})
        #     return dct.json()




if __name__ == '__main__':
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=50000)
