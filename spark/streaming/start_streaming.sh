sleep 60
pip install pandas
pip install requests
pip install kafka-python==2.0.2
spark-submit --conf spark.jars.ivy=/opt/app --packages "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0" --master spark://spark:7077 --deploy-mode client ../../app/streaming/streaming.py