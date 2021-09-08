# Data Engineering: Speech-to-text data collection with Kafka, Airflow, and Spark

After starting your Zookeeper server and Kafka broker, execute the example code below

```
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic audiostore
```