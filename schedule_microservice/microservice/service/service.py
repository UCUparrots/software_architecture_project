import sys
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import Timeslot, Message, OptMessage, CustomEncoder
from typing import List
from uuid import UUID, uuid4
from repository import RepositoryLayer


class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer(host='cassandra-node', port=9042)

    def get_timeslots(self, optmessage: OptMessage):
        timeslots = self.repository.get_timeslots(optmessage)
        return json.dumps(timeslots, cls=CustomEncoder)
    
    def new_timeslots(self, timeslots: List[Timeslot]):
        result = True
        for timeslot in timeslots:
            print(timeslot, "!!!")
            curr_res = self.repository.save_timeslot(timeslot)
            if not curr_res:
                result = False
        return result
    
    def delete_timeslot(self, timeslot_id: UUID):
        # need to somehow communicate with Vlad's microservice to find out if timeslot is taken for an appointment
        return self.repository.delete_timeslot(timeslot_id)
