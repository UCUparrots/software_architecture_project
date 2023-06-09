import sys
sys.path.append('./opt/app/domain')
from domain_objects import SignUp, LogIn, UserInfoUpdate, UserID
from uuid import UUID, uuid4
from typing import Union
import psycopg2
import bcrypt
from datetime import datetime
import psycopg2.extras
import json
import requests



class RepositoryLayer:
    def __init__(self):
        self.connection = psycopg2.connect(database='test_user_db', user='postgres', 
                        password='postgres', host='postgres-1')
        self.cursor = self.connection.cursor()
        psycopg2.extras.register_uuid()
    
    def save_user(self, user: SignUp):
        # save user to rdbms
        sql = "INSERT INTO users (user_id, email, password_hash, firstname, surname, phone, birthdate, is_doctor, notification) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

        try:
            salt = bcrypt.gensalt()
  
            # Hashing the password
            hash = bcrypt.hashpw(user.password_hash.encode("utf-8"), salt)
        
            if user.notification is None:
                user.notification = True
                
            self.cursor.execute(sql, (str(user.user_id), str(user.email), str(hash), str(user.firstname), 
                                str(user.lastname), str(user.phone), str(user.birthdate), str(user.is_doctor), str(user.notification)))
            self.connection.commit()
            return user.user_id
        except Exception as e:
            print(e)
            return ""
        

    def post_to_medcard(self, user: SignUp , url: str):
        data = json.dumps( {
            "user_id": str(user.user_id),
            "email": str(user.email),
            "firstname": str(user.firstname),
            "lastname": str(user.lastname),
            "phone": str(user.phone),
            "birthdate": str(user.birthdate),
            "is_doctor": str(user.is_doctor),
            "doctor_phd": str(user.doctor_phd),
            "doctor_specialization": str(user.doctor_specialization)
        })

        print(user.doctor_phd)

        try:
            r = requests.post(url = url, data = data)
        except Exception as e:
            print(e)
    

    def check_user_existence(self, user_info: Union[SignUp, LogIn]):
        # save appointment to rdbms
        email = user_info.email
        
        sql = "SELECT EXISTS(SELECT 1 FROM users WHERE email = %s);"
        
        self.cursor.execute(sql, (str(email), ))

        result = self.cursor.fetchone()

        if result is None:
            return False

        return result[0]

    def check_password_hash(self, login: LogIn):
        email = login.email
        password = login.password_hash.encode('utf-8')  # password should be bytes

        # Fetch the stored password hash for the user
        self.cursor.execute("SELECT password_hash FROM users WHERE email = %s;", (email,))
        result = self.cursor.fetchone()

        if result is None:
            return False 

        stored_password_hash = result[0]

        return bcrypt.checkpw(password, stored_password_hash.encode('utf-8'))


    def authenticate_user(self, login: LogIn):
        """
        Authenticates if user with such email exists and if password hashes are the same
        Returns user id if success, empty string if failure
        """
        if not self.check_user_existence(login) and not self.check_password_hash(login):
            return ""
        self.cursor.execute("SELECT user_id FROM users WHERE email = %s;", (str(login.email),))
        result = self.cursor.fetchone()
        return result[0]

    def update_user(self, user: UserInfoUpdate):
        try:
            fields_to_update = [(field, getattr(user, field)) for field in vars(user) if (getattr(user, field) is not None and field != "user_id") ]

            sql_update_query = "UPDATE users SET " + ", ".join(f"{field[0]} = %s" for field in fields_to_update) + " WHERE user_id = %s;"
            new_values = list(field[1] for field in fields_to_update) + [user.user_id]

            self.cursor.execute(sql_update_query, new_values)
            self.connection.commit()
        except Exception as e:
            print(e)
            return False
        return True
    
    def post_update_to_medcard(self, user: UserInfoUpdate , url: str):

        data = json.dumps( {
            "user_id": str(user.user_id),
            "email": str(user.email),
            "firstname": str(None),
            "lastname": str(None),
            "phone": str(user.phone),
            "birthdate": str(user.birthdate),
            "is_doctor": str(user.is_doctor),
            "doctor_phd": str(user.doctor_phd),
            "doctor_specialization": str(user.doctor_specialization)
        })

        

        try:
            r = requests.post(url = url, data = data)
        except Exception as e:
            print(e)

    def get_user_info(self, user_id: UserID):
        sql = "SELECT * FROM users WHERE user_id = %s;"
        self.cursor.execute(sql, (str(user_id.user_id), ))
        result = self.cursor.fetchall()
        try:
            user_data = result[0]
            data = {
                "email": str(user_data[1]),
                "firstname": str(user_data[3]),
                "lastname": str(user_data[4]),
                "phone": str(user_data[5]),
                "birthdate": user_data[6].strftime('%Y-%m-%d'),
                "is_doctor": user_data[7],
                "notification": user_data[8],
                "doctor_phd": user_data[9],
                "doctor_specialization": user_data[10]
            }
            return data
        except Exception as e:
            print(e)
            return {}

    
