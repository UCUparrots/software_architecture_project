from pyspark.sql import SparkSession
from pyspark.sql.streaming import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from kafka import KafkaConsumer
import pyspark
from pyspark.sql.functions import *
import requests
import json


def main(spark):
    # def get_doctor_info(user_id):
        # raise(ConnectionError(type(user_id.value)))
        # if isinstance(user_id.value, pyspark.sql.column.Column):
        #     return user_id
        # else:
        # try:
            # url = "http://login-service:8086/get_info"
            # print(str(user_id.value.expr))
            # print(type(user_id.value.expr))
            # raise(ConnectionError)
            # payload = {"user_id": user_id.value.getItem(0)}
            # headers = {"Content-Type": "application/json"}
            # response = requests.get(url, json=payload, headers=headers)
            # return response
        # except TypeError:
        #     return user_id

    # def process_row(df):
    #     transformed_df = df.select(col("doctor_id"))

    #     return transformed_df
        # raise(ConnectionError(df))

        # doctor_id = json.loads(row.value.decode("utf-8"))["doctor"]
        # doctor_info = json.loads(get_doctor_info(doctor_id).json())
        # raise(ConnectionAbortedError(doctor_info))
        # if (len(doctor_info) == 0) or (doctor_info['notification'] == False):
            
        #     return 10
        
        # email = doctor_info['email']
        # doctor_allert = json.loads(row.value.decode("utf-8"))
        # doctor_allert['email'] = email
        
        # return 10
        
        # doctor_info = response.json()
        # email = doctor_info["email"]
        # row_with_email = row.withColumn("email", lit(email))
        # notification_value = row_with_email["notification"]
        # if notification_value:
        #     return row_with_email
        # else:
        #     return spark.createDataFrame([(None,)], ["empty"])
        # return row
        # pass
        
    # def process_batch(df, epoch_id):
        # # Extract the 'value' column containing the JSON data
        # df = df.selectExpr("CAST(value AS STRING)")

        # # Define the schema for the JSON data
        # schema = StructType([
        #     StructField("appointment_id", StringType()),
        #     StructField("doctor_id", StringType()),
        #     StructField("patient_id", StringType()),
        #     StructField("type", IntegerType()),
        #     StructField("date", TimestampType())
        # ])

        # df = df.select(from_json(df.value, schema).alias("data")).select("data.*")

        
        # doctor_ids = df.select("doctor_id").distinct().collect()

        # for row in doctor_ids:
        #     doctor_id = row["doctor_id"]

        #     # Send a POST request to "some_service" with the doctor_id
        #     response = requests.post("some_service", json={"doctor_id": doctor_id})

        #     if response.status_code == 200:
        #         data = response.json()
        #         notification = data.get("notification")
        #         email = data.get("email")

        #         if notification is True:
        #             # Add a new 'email' column to the DataFrame with the email value
        #             df = df.withColumn("email", lit(email)).where(col("doctor_id") == doctor_id)

        # df.selectExpr("to_json(struct(*)) AS value") \
            # df.writeStream.format("kafka") \
            # .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
            # .option("topic", output_topic_name) \
            # .option("checkpointLocation", "/opt/app/kafka_checkpoint") \
            # .start() \
            # .awaitTermination()
            # pass

    

        


    input_topic_name = "doctor_alert"
    output_topic_name = "patient_email"

    kafka_adress = 'kafka-server'
    kafka_port = 9092

   
    df = spark \
            .readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
            .option("subscribe", input_topic_name) \
            .option("startingOffsets", "latest") \
            .option("failOnDataLoss", "false") \
            .load()
            
            
    df = df.selectExpr("CAST(value AS STRING)")

    schema = StructType() \
        .add("id", StringType()) \
        .add("doctor", StringType()) \
        .add("patient", StringType()) \
        .add("type", StringType()) \
        .add("date", StringType())

    df = df.select(from_json(col("value").cast("string"), schema).alias("parsed_value"))
    
    # Select the "id" field
    df = df.select(col("parsed_value.doctor").alias("value"))
    # doctor_info = get_doctor_info(df)

    query = df.writeStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", f'{kafka_adress}:{kafka_port}') \
            .option("topic", output_topic_name) \
            .option("checkpointLocation", "/opt/app/kafka_checkpoint") \
            .start()
            
    query.awaitTermination()

if __name__ == "__main__":
    spark = SparkSession \
            .builder \
            .appName("Spark Kafka Streaming") \
            .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
            .config("spark.sql.streaming.checkpointLocation", "/opt/app/spark-checkpoint") \
            .getOrCreate()
    main(spark)
    