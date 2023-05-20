import sys
sys.path.append('./opt/app/domain')
from domain_objects import Timeslot, Message, OptMessage
from domain import DomainLayer
from uuid import UUID
from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory


class RepositoryLayer:
    def __init__(self, host, port):
        self.session = None
        self.host = host
        self.port = port
        self.connect_cassandra(keyspace="schedule")

    def connect_cassandra(self, keyspace=None):
        cluster = Cluster([self.host], port=self.port)
        if keyspace is None:
            self.session = cluster.connect()
        else:
            self.session = cluster.connect(keyspace)
            self.session.row_factory = ordered_dict_factory
    
    def execute(self, query, row):
        prepared = self.session.prepare(query)
        self.session.execute(prepared, row)

    def execute_query(self, query):
        self.session.execute(query)

    def save_timeslot(self, timeslot: Timeslot):
        # save timeslot to cssandra
        sql = "INSERT INTO Timeslots (timeslot_id, doctor_id, date, availability) VALUES (%s, %s, %s, %s);"
        try:
            self.execute(sql, (str(timeslot.timeslot_id), str(timeslot.doctor), timeslot.date.strftime('%Y-%m-%d %H:%M:%S'), timeslot.availability))
            return True
        except:
            return False
    
    def get_timeslots(self, optmessage: OptMessage):
        # retrieve timeslots from cassandra
        columns_mapping = {
            0: 'timeslot_id',
            1: 'doctor_id',
            2: 'date',
            3: 'availability'
        }
        filters = [optmessage.timeslot_id, optmessage.doctor, optmessage.date, optmessage.availability]
       
        print(filters)
        columns = [columns_mapping[filters.index(filter_col)] for filter_col in filters if filter_col is not None]
        values = [filter_col for filter_col in filters if filter_col is not None]
        
        print(columns)
        if columns == []:
            try:
                self.execute_query("SELECT * FROM Timeslots")
            except:
                return False
            
        condition = [f"{col} = '{values[idx]}'" for idx, col in enumerate(columns)]
        condition = " AND ".join(condition)

        sql = f"SELECT * FROM Timeslots WHERE {condition}"
        try:
            self.execute_query(sql)
        except:
            return False
        return True

    def delete_future_appointment(self, timeslot_id: UUID):
        # delete from cassandra
        try:
            self.execute("DELETE FROM Timeslots WHERE timeslot_id = %s", (timeslot_id))
        except:
            return False
        return True
