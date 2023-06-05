import uvicorn
from fastapi import FastAPI
import sys
import os
import time
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain_objects import Appointment, Message, Reason, CustomEncoder
from domain import DomainLayer
from service import ServiceLayer

from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic

class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()
        self.kafka_adress = 'kafka-server'
        self.kafka_port = 9092
        
        
        client = KafkaAdminClient(bootstrap_servers=f'{self.kafka_adress}:{self.kafka_port}')
        topic_list = []
        topic_list.append(NewTopic(name='doctor_alert', num_partitions=1, replication_factor=1))
        client.create_topics(new_topics=topic_list, validate_only=False)
        self.producer = KafkaProducer(bootstrap_servers=f'{self.kafka_adress}:{self.kafka_port}')
        

        @self.app.get('/get_appointments')
        def get_appointments(args: dict):
            optmessage = DomainLayer.create_opt_message(args)
            appointments = self.service.get_appointments(optmessage)
            return appointments
        
        @self.app.get('/get_future_appointments')
        def get_appointments(args: dict):
            optmessage = DomainLayer.create_opt_message(args)
            appointments = self.service.get_future_appointments(optmessage)
            return appointments
        
        @self.app.get('/get_past_appointments')
        def get_appointments(args: dict):
            optmessage = DomainLayer.create_opt_message(args)
            appointments = self.service.get_past_appointments(optmessage)
            return appointments

        @self.app.post('/new_appointment')
        def new_appointment(args: dict):
            appointment = DomainLayer.create_appointment(args)
            future = self.producer.send('doctor_alert', json.dumps(appointment, cls=CustomEncoder).encode("utf-8"))
            result = future.get(timeout=60)
            status = self.service.create_appointment(appointment)
            return status
        
        @self.app.post('/delete_appointment')
        def delete_appointment(args: dict):
            appointment_id = DomainLayer.get_appointment_id(args)
            status = self.service.delete_appointment(appointment_id)
            return status

        @self.app.post('/confirm_appointment')
        def confirm_appointment(args: dict):
            appointment_id = DomainLayer.get_appointment_id(args)
            status = self.service.confirm_appointment(appointment_id)
            return status


if __name__ == '__main__':
    time.sleep(30)
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8085)
