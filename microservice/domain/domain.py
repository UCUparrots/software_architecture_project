from appointment import Appointment, Message

class DomainLayer:

    def __init__(self):
        pass

    @staticmethod
    def create_message(json):
        message = Message(json)
        return message

    @staticmethod
    def create_appointment(data):
        appointment = Appointment(data)
        return appointment
    
    @staticmethod
    def get_appointment_id(json):
        return json['appointment_id']