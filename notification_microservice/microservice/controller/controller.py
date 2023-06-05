import uvicorn
from fastapi import FastAPI
import sys
import os
import time
import threading
import json
sys.path.append('./opt/app/domain')
sys.path.append('./opt/app/service')

from domain import DomainLayer
from service import ServiceLayer
from kafka import KafkaConsumer



class ControlerLayer():
    def __init__(self) -> None:
        
        self.app = FastAPI()
        self.service = ServiceLayer()
        self.kafka_adress = 'kafka-server'
        self.kafka_port = 9092
        
        self.consumer = KafkaConsumer('patient_email', bootstrap_servers=f'{self.kafka_adress}:{self.kafka_port}', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        # self.consumer = KafkaConsumer('patient_email', bootstrap_servers=f'{self.kafka_adress}:{self.kafka_port}', value_deserializer=lambda m: m.decode('utf-8'))
        consumer_thread = threading.Thread(target=self.read_mq)
        consumer_thread.start()
    
        
    def read_mq(self):
        for message in self.consumer:
            # raise(ChildProcessError)
            print(message.value)
            self.service.add_message(message.value)
    


if __name__ == '__main__':
    time.sleep(30)
    controller = ControlerLayer()
    uvicorn.run(controller.app, host='0.0.0.0', port=8090)
