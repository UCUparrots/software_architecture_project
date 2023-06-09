from uuid import uuid4
from domain_objects import Message, Email
class DomainLayer:

    def __init__(self):
        pass

    @staticmethod
    def create_message(json: dict):
        message = Message.parse_obj(json)
        return message

    @staticmethod
    def create_email(json: dict):
        email = Email.parse_obj(json)
        return email
    # @staticmethod
    # def create_opt_message(json: dict):
    #     opt = OptMessage.parse_obj(json)
    #     return opt
    
    # @staticmethod
    # def create_appointment(data: dict):
    #     data['id'] = uuid4()
    #     appointment = Appointment.parse_obj(data)
    #     return appointment
    
    # @staticmethod
    # def recreate_appointment(data: dict):
    #     appointment = Appointment.parse_obj(data)
    #     return appointment
    
    # @staticmethod
    # def get_appointment_id(json: dict):
    #     return json['appointment_id']
    
    # @staticmethod
    # def recreate_appointments(appointments: list[tuple]):
    #     lst_obj = []
    #     for row in appointments:
    #         dct = {
    #             'id': row[0],
    #             'doctor': row[1],
    #             'patient': row[2],
    #             'type': row[3],
    #             'date': row[4]
    #         }
    #         appointment = DomainLayer.recreate_appointment(dct)
    #         lst_obj.append(appointment)
    #     return lst_obj