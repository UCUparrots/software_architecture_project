import sys
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import Appointment, Message, Reason
from uuid import UUID, uuid4
from repository import RepositoryLayer




class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def get_appointments(self, message):
        past = self.repository.get_past_appointments(message)
        future = self.repository.get_future_appointsments(message)

        result = past.extend(future)
        return result
    
    def create_appointment(self, message: Message):
        appointment = Appointment(id=uuid4(), doctor=message.doctor, patient=message.patient, type=message.type, date=message.date)
        return self.repository.save_appointment(appointment)
    
    def delete_appointment(self, appointment_id: UUID):
        check = self.repository.check_if_future(appointment_id)
        if check:
            return self.repository.delete_future_appointment(appointment_id)
        return self.repository.delete_past_appointment(appointment_id)
    
    def confirm_appointment(self, appointment_id: UUID):
        return self.repository.confirm_appointmnet(appointment_id)