import json
from faker import Faker
from kafka import KafkaProducer

fake = Faker()
user_id = fake.random_int(min=1, max=1000)

# Kafka settings
bootstrap_servers = ['localhost:9092']
topic_name = 'test_stream_mult_shards_data_topic'

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

# Generate data and send it to Kafka
while True:
    data = {
        'user_id': fake.random_int(min=1, max=1000),
        'order_id': fake.random_int(min=1, max=1000),
        'data': fake.text()
    }
    producer.send(topic_name, value=json.dumps(data).encode('utf-8'))
    print(f'Sent data to Kafka topic ({topic_name}): {data}')