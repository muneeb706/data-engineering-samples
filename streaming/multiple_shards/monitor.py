"""
Monitor partitioning assignment
"""

from kafka import KafkaConsumer
import json
import time


def create_consumer(topic_name):
    return KafkaConsumer(
        topic_name,
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="partions_monitor",
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )


consumer = create_consumer("test_stream_mult_shards")


def print_assignment(consumer):
    # Start polling to ensure the consumer joins the group
    consumer.poll(timeout_ms=1000)
    while True:
        partitions = consumer.assignment()
        if partitions:
            print("Current partition assignment:")
            for partition in partitions:
                print(f"Topic: {partition.topic}, Partition: {partition.partition}")
            break
        else:
            print("No partitions assigned yet.")
        time.sleep(2)  # Check every 2 seconds


print_assignment(consumer)
