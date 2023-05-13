import sys
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import Appointment, Message, Reason, OptMessage
from uuid import UUID, uuid4
from repository import RepositoryLayer




class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def get_appointments(self, optmessage: OptMessage):
        past = self.repository.get_past_appointments(optmessage)
        future = self.repository.get_future_appointments(optmessage)
        # print(past)
        # print(future)
        past.extend(future)
        
        return json.dumps(past)
    
    def create_appointment(self, appointment: Appointment):
        return self.repository.save_appointment(appointment)
    
    def delete_appointment(self, appointment_id: UUID):
        check = self.repository.check_if_future(appointment_id)
        if check:
            return self.repository.delete_future_appointment(appointment_id)
        return self.repository.delete_past_appointment(appointment_id)
    
    def confirm_appointment(self, appointment_id: UUID):
        return self.repository.confirm_appointment(appointment_id)