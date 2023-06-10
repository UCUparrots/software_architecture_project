import sys
import json
import requests
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import Message
from uuid import UUID, uuid4
from repository import RepositoryLayer
from domain import DomainLayer

class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def add_message(self, message):
        status = self.validate(message)
        if not isinstance(status, dict):
            status = json.loads(status)
        
        if status == {}:
            return False
        print(status)
        print(type(status))
        if status['notification']:
            payload = {
                'email': status['email'],
                'firstname': status['firstname'],
                'lastname': status['lastname'],
                'phone': status['phone']
            }
            email = DomainLayer.create_email(payload)
            return self.send_email(email)
        return True
    
    def validate(self, message):
        # print(str(message.id))
        url = f"http://login-service:8086/get_info?user_id={str(message.id)}"
        # print(url)
        # payload = {"user_id": str(message.id)}
        # headers = {"Content-Type": "application/json"}
        # response = requests.get(url, json=payload, headers=headers)
        response = requests.get(url)
        return response.json()
        
    
    def send_email(self, message):
        # Complicated logic, API calls, ...
        print('Message sent!')
        print(message)
        return True
