import sys
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
# from domain_objects import Appointment, Message, Reason, OptMessage, CustomEncoder
from uuid import UUID, uuid4
from repository import RepositoryLayer

class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def add_message(self, message):
        status = self.validate(message)
        if status:
            pass
    
    def validate(self, message):
        pass
    
    def send_email(self, message):
        pass
