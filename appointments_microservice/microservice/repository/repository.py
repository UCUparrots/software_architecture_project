import sys
sys.path.append('./opt/app/domain')
from domain_objects import Appointment, Message, Reason, OptMessage
from uuid import UUID
import psycopg2



class RepositoryLayer:
    def __init__(self):
        self.connection = psycopg2.connect(database='test_db', user='postgres', 
                        password='postgres', host='postgres-1')

    def save_appointment(self, appointment: Appointment):
        # save appointment to rdbms
        status = True
        return status
    
    def get_past_appointments(self, optmessage: OptMessage):
        # retrieve appointments from rdbms
        result = []
        return result
    
    def get_future_appointments(self, optmessage: OptMessage):
        # retrieve appointments from rdbms
        result = []
        return result
    
    def check_if_future(self, appointment_id: UUID):
        # check
        check=True
        return check
    
    def delete_future_appointment(self, appointment_id: UUID):
        # delete from rdbms
        status = True
        return status
    
    def delete_past_appointment(self, appointment_id: UUID):
        # delete from rdbms
        status = True
        return status
    
    def confirm_appointment(self, appointment_id: UUID):
        # move appointment from future to past
        status = True
        return status