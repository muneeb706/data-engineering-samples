# Data Engineering Samples
Contains sample implementation of data engineering tasks.

- [How to Shard Streaming Data with Apache Kafka](https://github.com/muneeb706/data-engineering-samples/tree/main/streaming/multiple_shards)
    1. Set up a Kafka cluster on your local machine and run it on port 9092 ([Quickstart guide](https://kafka.apache.org/quickstart)).
    2. Create a shard topic with multiple partitions `python kafka_admin.py'
    3. Run the producer to send messages to partitions of the topic `python producer.py`
    5. Run consumers to consume data from each partition e-g `python consumers/part_1_consumer.py`
    6. Monitor partition assignment `python monitor.py`

