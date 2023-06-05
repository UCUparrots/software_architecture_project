from pyspark.sql import SparkSession
from pyspark.sql.streaming import *
from pyspark.sql.functions import *
from kafka import KafkaConsumer
from pyspark.sql.functions import *
import requests
import json

import threading

def main(spark):
    def get_doctor_info(user_id):
        url = "http://login-service:8086/get_info"
        payload = {"user_id": user_id}
        headers = {"Content-Type": "application/json"}
        response = requests.get(url, json=payload, headers=headers)
        return response

    def process_row(row):
        
        # doctor_id = json.loads(row.value.decode("utf-8"))["doctor"]
        # doctor_info = json.loads(get_doctor_info(doctor_id).json())
        # # if (len(doctor_info) == 0) or (doctor_info['notification'] == False):
        #     # return row
        
        # email = doctor_info['email']
        # doctor_allert = json.loads(row.value.decode("utf-8"))
        # doctor_allert['email'] = email

        # return row
        # raise(ConnectionError(response))
        
        # doctor_info = response.json()
        # email = doctor_info["email"]
        # row_with_email = row.withColumn("email", lit(email))
        # notification_value = row_with_email["notification"]
        # if notification_value:
        #     return row_with_email
        # else:
        #     return spark.createDataFrame([(None,)], ["empty"])
        return row
        
    

        


    input_topic_name = "doctor_alert"
    output_topic_name = "patient_email"

    kafka_adress = 'kafka-server'
    kafka_port = 9092

    df = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
            .option("subscribe", input_topic_name) \
            .option("startingOffsets", "earliest") \
            .option("failOnDataLoss", "false") \
            .load()
    
    
    df.writeStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
            .option("topic", output_topic_name) \
            .option("checkpointLocation", "/opt/app/kafka_checkpoint") \
            .start() \
            .awaitTermination()
#    .foreach(process_row) \
   
    
            
            
            
            
    
    # kafka_query = df\
    # .writeStream \
    # .format("kafka") \
    # .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
    # .option("topic", output_topic_name) \
    # .option("checkpointLocation", "/opt/app/kafka_checkpoint").start().awaitTermination()
    
    # console_query = df \
    #     .writeStream \
    #     .format("console") \
    #     .outputMode("append") \
    #     .start()


if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .appName("Spark Kafka Streaming") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
            .config("spark.sql.streaming.checkpointLocation", "/opt/app/spark-checkpoint") \
            .getOrCreate()
    main(spark)
    