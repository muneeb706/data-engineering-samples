import json
from kafka import KafkaConsumer, TopicPartition

def create_consumer(topic_name, partition):
    consumer = KafkaConsumer(
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='part-1-consumer',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    # Assign the consumer to a specific partition
    consumer.assign([TopicPartition(topic_name, partition)])
    return consumer

consumer = create_consumer('test_stream_mult_shards', 1)

# Consume data from Kafka and process it
for message in consumer:
    print(f"Received: {message.value} from partition {message.partition}")