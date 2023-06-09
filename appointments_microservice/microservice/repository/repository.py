import sys
sys.path.append('./opt/app/domain')
from domain_objects import Appointment, Message, Reason, OptMessage
from domain import DomainLayer
from uuid import UUID
import psycopg2
import time
import requests
import pandas as pd
import json



class RepositoryLayer:
    def __init__(self):
        self.connection = psycopg2.connect(database='test_db', user='postgres', 
                        password='postgres', host='postgres-1')
        self.cursor = self.connection.cursor()

    def delete_timeslot(self, appointment: Appointment):
        app_doctor_id = appointment.doctor
        app_date = appointment.date.strftime('%Y-%m-%d %H:%M:%S')
        schedule_url = "http://scheduleService:8080/get_timeslots"
        get_json = {"doctor": str(app_doctor_id), "date": str(app_date)}
        try:
            response = requests.get(url=schedule_url, json=get_json).json()
            response_data = json.loads(response.strip())
            response_2 = json.loads(response_data)
            # print("get", response_2)
            # print(type(response_2))
            # print(response_2[0])
            # print(response_2[0]["timeslot_id"])
        except Exception as e:
            print(f"Failed to get from Timeslots: {str(e)}")
            return False
        
        if len(response_2) != 1:
            print(f"There should be one timeslot for such appointment, insted {len(response)} were found")
            return False
        timeslot_id = response_2[0]["timeslot_id"]
        # print(timeslot_id)
        schedule_url = "http://scheduleService:8080/delete_timeslot"
        post_json = {"timeslot_id": str(timeslot_id)}
        try:
            response = requests.post(url=schedule_url, json=post_json)
            print("post", response.json())
        except Exception as e:
            print(f"Failed to post to Timeslots: {str(e)}")
            return False
        return True


    def save_appointment(self, appointment: Appointment):
        if not self.delete_timeslot(appointment):
            print("Could not remove timeslot for the appointment")
            return False

        # save appointment to rdbms
        sql = "INSERT INTO FutureAppointments (appointment_id, doctor_id, patient_id, type, date) VALUES (%s, %s, %s, %s, %s);"
        try:
            self.cursor.execute(sql, (str(appointment.id), str(appointment.doctor), str(appointment.patient), str(appointment.type.value), appointment.date.strftime('%Y-%m-%d %H:%M:%S')))
            self.connection.commit()
            return True
        except:
            return False
    
    def get_past_appointments(self, optmessage: OptMessage):
        # retrieve appointments from rdbms
        columns_mapping = {
            0: 'appointment_id',
            1: 'doctor_id',
            2: 'patient_id',
            3: 'type',
            4: 'date'
        }
        if optmessage.type is None:
            filters = [optmessage.id, optmessage.doctor, optmessage.patient, optmessage.type, optmessage.date]
        else:
            filters = [optmessage.id, optmessage.doctor, optmessage.patient, optmessage.type.value, optmessage.date]
       
        print(filters)
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]
        
        print(columns)
        if columns == []:
            try:
                self.cursor.execute("SELECT * FROM PastAppointments")
                result = self.cursor.fetchall()
                return DomainLayer.recreate_appointments(result)
            except:
                return False
            
        condition = [f"{col} = '{values[idx]}'" for idx, col in enumerate(columns)]
        condition = " AND ".join(condition)

        sql = f"SELECT * FROM PastAppointments WHERE {condition}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return DomainLayer.recreate_appointments(result)
    
    def get_future_appointments(self, optmessage: OptMessage):
        # retrieve appointments from rdbms
        columns_mapping = {
            0: 'appointment_id',
            1: 'doctor_id',
            2: 'patient_id',
            3: 'type',
            4: 'date'
        }
        if optmessage.type is None:
            filters = [optmessage.id, optmessage.doctor, optmessage.patient, optmessage.type, optmessage.date]
        else:
            filters = [optmessage.id, optmessage.doctor, optmessage.patient, optmessage.type.value, optmessage.date]
       
        print(filters)
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]
        
        print(columns)
        if columns == []:
            try:
                self.cursor.execute("SELECT * FROM FutureAppointments")
                result = self.cursor.fetchall()
                return DomainLayer.recreate_appointments(result)
            except:
                return False
            
        condition = [f"{col} = '{values[idx]}'" for idx, col in enumerate(columns)]
        condition = " AND ".join(condition)

        sql = f"SELECT * FROM FutureAppointments WHERE {condition}"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return DomainLayer.recreate_appointments(result)
    
    def check_if_future(self, appointment_id: UUID):
        # check
        sql = "SELECT * FROM futureappointments WHERE appointment_id = %s"
        try:
            self.cursor.execute(sql, (appointment_id,))
            result = self.cursor.fetchall()
        except:
            return False
        if result == []:
            return False
        return True
    

    def return_timeslot(self, appointment_id: UUID):
        sql = f"SELECT * FROM FutureAppointments WHERE appointment_id = '{appointment_id}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        if result:
            appointment = result[0]
            app_doctor_id = appointment[1]
            app_start_date = appointment[4]
            app_end_date = app_start_date + pd.Timedelta(minutes=15)
            schedule_url = "http://scheduleService:8080/new_timeslots"
            post_json = {"doctor": app_doctor_id, "start_date": str(app_start_date), "end_date": str(app_end_date)}
            try:
                response = requests.post(url=schedule_url, json=post_json)
                print(response.json())
            except Exception as e:
                print(f"Failed to post to Timeslots: {str(e)}")
                return False
            return True
        else:
            print("No such appointment")
        return False
        
    
    def delete_future_appointment(self, appointment_id: UUID, commit=True):
        if not self.return_timeslot(appointment_id):
            return False
        # delete from rdbms
        try:
            self.cursor.execute("DELETE FROM FutureAppointments WHERE appointment_id = %s", (appointment_id,))
            if commit:
                self.connection.commit()
        except:
            return False
        return True
    
    def delete_past_appointment(self, appointment_id: UUID):
        # delete from rdbms
        try:
            self.cursor.execute("DELETE FROM PastAppointments WHERE appointment_id = %s", (appointment_id,))
            self.connection.commit()
        except:
            return False
        return True
    
    def confirm_appointment(self, appointment_id: UUID):
        # move appointment from future to past
        optmessage = DomainLayer.create_opt_message({'id': appointment_id})
        appointment = self.get_future_appointments(optmessage)
        print(optmessage)
        if not appointment:
            return False
        print(appointment)
        appointment = appointment[0]
        status = self.delete_future_appointment(appointment_id, commit=False)

        if not self.delete_timeslot(appointment):
            print("Could not remove timeslot for the appointment")
            return False
        if status:
            sql = "INSERT INTO PastAppointments (appointment_id, doctor_id, patient_id, type, date) VALUES (%s, %s, %s, %s, %s);"
            try:
                self.cursor.execute(sql, (str(appointment.id), str(appointment.doctor), str(appointment.patient), str(appointment.type.value), appointment.date.strftime('%Y-%m-%d %H:%M:%S')))
                self.connection.commit()
                return True
            except:
                return False
        return False
