import sys
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/repository')
from domain_objects import SignUp, LogIn, UserInfoUpdate, UserID
from uuid import UUID, uuid4
from repository import RepositoryLayer




class ServiceLayer:
    def __init__(self):
        self.repository = RepositoryLayer()

    def save_user(self, signup: SignUp):
        """
        Pushes user to db, returns user id if success, empty string if failure
        """
        if self.repository.check_user_existence(signup):
            return ""
        return self.repository.save_user(signup)

    def authenticate_user(self, login: LogIn):
        return self.repository.authenticate_user(login)
    
    def update_user(self, user_info: UserInfoUpdate):
        return self.repository.update_user(user_info)

    def get_user_info(self, user_info: UserID):
        return json.dumps(self.repository.get_user_info(user_info))