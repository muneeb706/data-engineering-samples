import json
from faker import Faker
from kafka import KafkaProducer


# Kafka settings
bootstrap_servers = ["localhost:9092"]
topic_name = "test_stream_mult_shards"


# Create Custom Partitioner
def simple_partitioner(key, all_partitions, available_partitions):
    # Custom logic to determine the partition
    if key is None:
        return all_partitions[0]
    # Example: Use the hash of the key to determine the partition
    return hash(key) % len(all_partitions)


# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers, partitioner=simple_partitioner
)

# Generate data and send it to Kafka
fake = Faker()
while True:
    data = {
        "user_id": fake.random_int(min=1, max=1000),
        "order_id": fake.random_int(min=1, max=1000),
        "data": fake.text(),
    }
    producer.send(topic_name, key=b"user_id", value=json.dumps(data).encode("utf-8"))
    print(f"Sent data to Kafka topic ({topic_name}): {data}")
