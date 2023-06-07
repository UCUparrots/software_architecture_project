from domain_objects import Timeslot, Message, OptMessage
from uuid import uuid4
import pandas as pd
from uuid import UUID


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
    
    def create_timeslot(self, data: dict):
        data['timeslot_id'] = uuid4()
        timeslot = Timeslot.parse_obj(data)
        return timeslot
    
    def create_timeslots(self, data: dict):
        print("Start create timeslots")
        interval = pd.Timedelta(minutes=15)  # Define the desired interval
        end_date = pd.to_datetime(data["end_date"]) - interval  # Subtract the interval from the end date
        timestamps = pd.date_range(start=data["start_date"], end=end_date, freq=interval).tolist()
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
    
    @staticmethod
    def convert_uuid_to_str(item):
        if isinstance(item, UUID):
            return str(item)
        return item
    
    @staticmethod
    def convert_str_to_uuid(item):
        if not isinstance(item, UUID):
            return UUID(item)
        return item
