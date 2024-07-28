# Data Engineering Samples
Contains sample implementation of data engineering tasks.

- [How to distribute incoming streaming data to multiple shards using Apache Kafa](https://github.com/muneeb706/data-engineering-samples/tree/main/streaming/multiple_shards)
    1. Set up a single-node Kafka cluster on your local machine and run it on port 9092 ([Quickstart guide](https://kafka.apache.org/quickstart)).
    2. Generate fake data `python data_generator.py`
    3. Distribute data in shards `python shard_distributor.py`
    4. Run consumers e-g `python shard_consumers/shard_consumer0.py`


