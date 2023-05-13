from domain_objects import Appointment, Message, OptMessage
from uuid import uuid4
class DomainLayer:

    def __init__(self):
        pass

    @staticmethod
    def create_message(json: dict):
        message = Message.parse_obj(json)
        return message

    @staticmethod
    def create_opt_message(json: dict):
        opt = OptMessage.parse_obj(json)
        return opt
    
    @staticmethod
    def create_appointment(data: dict):
        data['id'] = uuid4()
        appointment = Appointment.parse_obj(data)
        return appointment
    
    @staticmethod
    def get_appointment_id(json: dict):
        return json['appointment_id']