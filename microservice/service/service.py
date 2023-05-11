import sys
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import Appointment, Message, Reason
from uuid import UUID, uuid4
from repository import RepositoryLayer




class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def get_appointments(self):
        return
    
    def create_appointment(self, message: Message):
        appointment = Appointment(id=uuid4(), doctor=message.doctor, patient=message.patient, type=message.type, date=message.date)
        return self.repository.save_appointment(appointment)
    
    def delete_appointment(self, appointment_id: UUID):
        return
    
    def confirm_appointment(self, appointment_id: UUID):
        return 