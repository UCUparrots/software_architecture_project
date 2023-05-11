import sys
sys.path.append('./opt/app/domain')
from domain_objects import Appointment, Message, Reason
from uuid import UUID


class RepositoryLayer:
    def __init__(self):
        pass

    def 