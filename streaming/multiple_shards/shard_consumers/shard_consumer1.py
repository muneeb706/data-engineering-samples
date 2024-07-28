import json
from kafka import KafkaConsumer

# Kafka settings
bootstrap_servers = ['localhost:9092']
shard_topic = 'shard_1'

# Create a Kafka consumer
consumer = KafkaConsumer(shard_topic, bootstrap_servers=bootstrap_servers)

# Consume data from Kafka and process it
for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    print(f'Received data from shard 1: {data}')