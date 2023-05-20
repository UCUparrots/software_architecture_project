from domain_objects import Timeslot, Message, OptMessage
from uuid import uuid4
import pandas as pd


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
    
    # @staticmethod
    def create_timeslot(data: dict):
        data['timeslot_id'] = uuid4()
        timeslot = Timeslot.parse_obj(data)
        return timeslot
    
    # @staticmethod
    def create_timeslots(self, data: dict):
        interval = pd.Timedelta(minutes=15)  # Define the desired interval
        timestamps = pd.date_range(start=data["start_date"], end=data["end_date"], freq=interval).tolist()
        timeslots = []

        for timestamp in timestamps:
            tmstmp_dct = {}
            tmstmp_dct["doctor"] = data["doctor"]
            tmstmp_dct["date"] = timestamp
            tmstmp_dct["availability"] = True
            timeslot = self.create_timeslot(tmstmp_dct)
            timeslots.append(timeslot)
        return timeslots
    
    @staticmethod
    def get_timeslot_id(json: dict):
        return json['timeslot_id']
