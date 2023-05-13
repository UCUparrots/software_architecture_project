import sys
sys.path.append('./opt/app/domain')
from domain_objects import Appointment, Message, Reason
from uuid import UUID


class RepositoryLayer:
    def __init__(self):
        self.rdbms_ip = ''

    def save_appointment(appointment: Appointment):
        # save appointment to rdbms
        status = True
        return status
    
    def get_past_appointments(message: Message):
        # retrieve appointments from rdbms
        status = True
        return status
    
    def get_future_appointments(message: Message):
        # retrieve appointments from rdbms
        status = True
        return status
    
    def check_if_future(appointment_id: UUID):
        # check
        check=True
        return check
    
    def delete_future_appointment(appointment_id: UUID):
        # delete from rdbms
        status = True
        return status
    
    def delete_past_appointment(appointment_id: UUID):
        # delete from rdbms
        status = True
        return status
    
    def confirm_appointment(appointment_id: UUID):
        # move appointment from future to past
        status = True
        return status