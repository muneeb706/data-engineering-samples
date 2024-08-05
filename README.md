# Data Engineering Samples
Contains sample implementation of data engineering tasks.

- [How to Shard Streaming Data with Apache Kafka](https://github.com/muneeb706/data-engineering-samples/tree/main/streaming/multiple_shards)
    1. Set up a Kafka cluster on your local machine and run it on port 9092 ([Quickstart guide](https://kafka.apache.org/quickstart)).
    2. Create a shard topic with multiple partitions `python kafka_admin.py`
    3. Run the producer to send messages to partitions of the topic `python producer.py`
    5. Run consumers to consume data from each partition e-g `python consumers/part_1_consumer.py`
    6. Monitor partition assignment `python monitor.py`

- [How to build patient profile by aggregating data from various sources using PySpark](https://github.com/muneeb706/data-engineering-samples/tree/main/map_reduce/build_patient_profile)

    This project demonstrate how to reads patient data from multiple CSV files, combine and process the data using PySpark, and save the resulting patient profiles to a MongoDB collection for further analysis and querying.
    1. Install Requirements `pip install -r requirements.txt`.
    2. Generate sample data `python data_generator.py`
    3. Run script to read, aggregate, and save data to MongoDB using PySpark `python read_data_spark.py`. Data will be saved in db (medical_db.patient).
    5. Run script to read and print data for patient with given patient_id e-g `python read_data_mongo.py --patient_id=patient_99`