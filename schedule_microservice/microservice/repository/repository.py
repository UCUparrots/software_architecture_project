import sys
sys.path.append('./opt/app/domain')
from domain_objects import Appointment, Message, Reason, OptMessage
from domain import DomainLayer
from uuid import UUID
import psycopg2



class RepositoryLayer:
    def __init__(self):
        self.connection = psycopg2.connect(database='test_db', user='postgres', 
                        password='postgres', host='postgres-1')
        self.cursor = self.connection.cursor()

    def save_appointment(self, appointment: Appointment):
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
        
    
    def delete_future_appointment(self, appointment_id: UUID, commit=True):
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
        if status:
            sql = "INSERT INTO PastAppointments (appointment_id, doctor_id, patient_id, type, date) VALUES (%s, %s, %s, %s, %s);"
            try:
                self.cursor.execute(sql, (str(appointment.id), str(appointment.doctor), str(appointment.patient), str(appointment.type.value), appointment.date.strftime('%Y-%m-%d %H:%M:%S')))
                self.connection.commit()
                return True
            except:
                return False
        return False