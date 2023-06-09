import sys
sys.path.append('./opt/app/domain')
import pandas as pd
from domain_objects import Timeslot, Message, OptMessage
from domain import DomainLayer
from uuid import UUID
from cassandra.cluster import Cluster
from cassandra.cluster import NoHostAvailable
from cassandra.query import ordered_dict_factory
import time
import json
import psycopg2



class RepositoryLayer:
    def __init__(self, host, port):
        self.session = None
        self.host = host
        self.port = port
        self.connect_cassandra(keyspace="schedule")
    
    
    def connect_cassandra(self, keyspace=None, max_retries=100, retry_delay=5):
        retry_count = 0
        while retry_count < max_retries and not self.session:
            try:
                cluster = Cluster([self.host], port=self.port)
                if keyspace is None:
                    self.session = cluster.connect()
                else:
                    self.session = cluster.connect(keyspace, wait_for_all_pools=True)
                    self.session.row_factory = ordered_dict_factory
                    self.session.execute('USE schedule')
                print("Successful connection!")
            except Exception as e:
                print(f"Failed to connect to Cassandra: {str(e)}")
                print("Retrying connection...")
                retry_count += 1
                time.sleep(retry_delay)

        if retry_count == max_retries:
            print("Failed to connect to Cassandra after multiple retries. Exiting...")
    
    def execute(self, query, row):
        prepared = self.session.prepare(query)
        self.session.execute(prepared, row)

    def execute_query(self, query):
        self.session.execute(query)

    def save_timeslot(self, timeslot: Timeslot):
        # save timeslot to cassandra
        sql = "INSERT INTO Timeslots (timeslot_id, doctor, date, availability) VALUES (?, ?, ?, ?);"
        try:
            self.execute(sql, (timeslot.timeslot_id, timeslot.doctor, timeslot.date.strftime('%Y-%m-%d %H:%M:%S'), timeslot.availability))
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    
    def get_timeslots(self, optmessage: OptMessage):
        # retrieve timeslots from cassandra
        columns_mapping = {
            0: 'timeslot_id',
            1: 'doctor',
            2: 'date',
            3: 'availability'
        }
        filters = [optmessage.timeslot_id, optmessage.doctor, optmessage.date, optmessage.availability]
       
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]

        try:
            if columns == []:
                sql = f"SELECT * FROM Timeslots;"
                rows = self.session.execute(sql)
                result = rows.all()
                return json.dumps(result, default=DomainLayer.convert_uuid_to_str)
            else:
                condition = " AND ".join(f"{col} = {DomainLayer.convert_to_str(values[idx])}" for idx, col in enumerate(columns))
                sql = f"SELECT * FROM Timeslots WHERE {condition} ALLOW FILTERING;"
                rows = self.session.execute(sql)
                result = rows.all()
                return json.dumps(result, default=DomainLayer.convert_uuid_to_str)
        except NoHostAvailable:
            print("Unable to connect to Cassandra. Check Cassandra service status.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return False
    
    def check_exesting_appointment(self, timeslot_id: UUID):
        connection = psycopg2.connect(database='test_db', user='postgres', 
                        password='postgres', host='postgres-1')
        cursor = connection.cursor()

        sql = f"SELECT * FROM Timeslots WHERE timeslot_id = {DomainLayer.convert_str_to_uuid(timeslot_id)};"
        rows = self.session.execute(sql)
        timeslot_info = rows.all()[0]
        timeslot_date = timeslot_info["date"]
        timeslot_doctor = timeslot_info["doctor"]
        condition = f"doctor_id = '{DomainLayer.convert_uuid_to_str(timeslot_doctor)}' AND date = '{timeslot_date}'"

        sql = f"SELECT * FROM PastAppointments WHERE {condition}"
        cursor.execute(sql)
        result = cursor.fetchall()
        if result: # not empty, there is such appointment
            # should cancel appointment
            appointment = result[0][0]
            try:
                cursor.execute("DELETE FROM PastAppointments WHERE appointment_id = %s", (appointment,))
                connection.commit()
            except Exception as e:
                print(f"An error occurred: {e}")
                return False
            return True
        return True


    def delete_timeslot(self, timeslot_id: UUID):
        # delete from cassandra
        try:
            self.check_exesting_appointment(timeslot_id)
            self.execute("DELETE FROM Timeslots WHERE timeslot_id = ?", (DomainLayer.convert_str_to_uuid(timeslot_id),))
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        return True

    