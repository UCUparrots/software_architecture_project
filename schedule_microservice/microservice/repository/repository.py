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
       
        # print(filters)
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]
        
        # print(columns)
        # print(values)
        try:
            if columns == []:
                sql = f"SELECT * FROM Timeslots;"
                rows = self.session.execute(sql)
                return json.dumps(rows.all(), default=DomainLayer.convert_uuid_to_str)
            else:
                condition = " AND ".join(f"{col} = {values[idx]}" for idx, col in enumerate(columns))
                sql = f"SELECT * FROM Timeslots WHERE {condition};"
                rows = self.session.execute(sql)
                return json.dumps(rows.all(), default=DomainLayer.convert_uuid_to_str)
        except NoHostAvailable:
            print("Unable to connect to Cassandra. Check Cassandra service status.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return False

    def delete_timeslot(self, timeslot_id: UUID):
        # delete from cassandra
        try:
            # TODO: call Vlad's microservice to check if there was appointment at that time and delete it if yes
            # TODO: the same should be done in Vlad's microservice when appointment is deleted: 
            # if it is done by patient (not called from here), 
            # the timeslot for that appointment should be added back in schedules DB
            self.execute("DELETE FROM Timeslots WHERE timeslot_id = ?", (DomainLayer.convert_str_to_uuid(timeslot_id),))
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
        return True

    