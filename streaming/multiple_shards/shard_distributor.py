import json
from kafka import KafkaConsumer, KafkaProducer

# Kafka settings
bootstrap_servers = ['localhost:9092']
topic_name = 'test_stream_mult_shards_data_topic'
shard_topic_prefix = 'shard_'

# Create a Kafka consumer
consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Consume data from Kafka and distribute it to shards
for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    shard_id = data['user_id'] % 4  # Simple sharding strategy
    shard_topic = f'{shard_topic_prefix}{shard_id}'
    producer.send(shard_topic, value=json.dumps(data).encode('utf-8'))
    print(f'Sent data to shard {shard_id}: {data}')