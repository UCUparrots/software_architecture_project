import sys
sys.path.append('./opt/app/domain')
from domain_objects import Timeslot, Message, OptMessage
from domain import DomainLayer
from uuid import UUID
from cassandra.cluster import Cluster
from cassandra.cluster import NoHostAvailable
from cassandra.query import ordered_dict_factory
import time


class RepositoryLayer:
    def __init__(self, host, port):
        self.session = None
        self.host = host
        self.port = port
        self.connect_cassandra(keyspace="schedule")

    # def connect_cassandra(self, keyspace=None):
    #     cluster = Cluster([self.host], port=self.port)
    #     if keyspace is None:
    #         self.session = cluster.connect()
    #     else:
    #         self.session = cluster.connect(keyspace)
    #         self.session.row_factory = ordered_dict_factory

    def connect_cassandra(self, keyspace=None, max_retries=100, retry_delay=5):
        retry_count = 0
        # while retry_count < max_retries:
        while not self.session:
            try:
                cluster = Cluster([self.host], port=self.port)
                if keyspace is None:
                    self.session = cluster.connect()
                else:
                    self.session = cluster.connect(keyspace)
                    self.session.row_factory = ordered_dict_factory
                print("Successful connection!")
                break  # Connection successful, exit the loop
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
        sql = "INSERT INTO Timeslots (timeslot_id, doctor, date, availability) VALUES (%s, %s, %s, %s);"
        try:
            self.execute(sql, (str(timeslot.timeslot_id), str(timeslot.doctor), timeslot.date.strftime('%Y-%m-%d %H:%M:%S'), timeslot.availability))
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
       
        print(filters)
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]
        
        print(columns)
        print(values)
        # if columns == []:
        #     try:
        #         rows = self.execute("SELECT * FROM Timeslots;")
        #         return rows
        #     except:
        #         return False
            
        # condition = [f"{col} = {values[idx]}" for idx, col in enumerate(columns)]
        # condition = " AND ".join(condition)
        # print(condition)

        # sql = f"SELECT * FROM Timeslots WHERE {condition};"
        # try:
        #     rows = self.execute(sql)
        #     print(rows)
        #     return rows
        try:
            if columns == []:
                rows = self.execute_query("SELECT * FROM Timeslots;")
                return rows
            else:
                condition = " AND ".join(f"{col} = {values[idx]}" for idx, col in enumerate(columns))
                sql = f"SELECT * FROM Timeslots WHERE {condition};"
                rows = self.execute_query(sql)
                return rows
        except NoHostAvailable:
            print("Unable to connect to Cassandra. Check Cassandra service status.")
        except Exception as e:
            print(f"An error occurred: {e}")

        return False

    def delete_future_appointment(self, timeslot_id: UUID):
        # delete from cassandra
        try:
            self.execute("DELETE FROM Timeslots WHERE timeslot_id = %s", (timeslot_id))
        except:
            return False
        return True
