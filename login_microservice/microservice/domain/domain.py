from domain_objects import SignUp, LogIn, UserInfoUpdate, UserID
from uuid import uuid4

from uuid import uuid4
class DomainLayer:

    def __init__(self):
        pass

    @staticmethod
    def create_signup(json: dict):
        print(json)
        json["user_id"] = uuid4()
        message = SignUp.parse_obj(json)
        print(message)
        return message

    @staticmethod
    def create_login(json: dict):
        opt = LogIn.parse_obj(json)
        return opt

    @staticmethod
    def create_user_update_info(json: dict):
        opt = UserInfoUpdate.parse_obj(json)
        return opt

    @staticmethod
    def create_user_id_info(json: dict):
        opt = UserID.parse_obj(json)
        return opt
    