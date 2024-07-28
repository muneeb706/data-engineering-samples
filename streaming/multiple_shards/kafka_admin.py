from kafka.admin import KafkaAdminClient, NewTopic

def create_topic(topic_name, num_partitions, replication_factor):
    """
    Creating a topic with multiple partitions
    """
    admin_client = KafkaAdminClient(bootstrap_servers=['localhost:9092'])
    topic = NewTopic(name=topic_name, 
                     num_partitions=num_partitions, 
                     replication_factor=replication_factor)
    admin_client.create_topics([topic])

create_topic('test_stream_mult_shards', num_partitions=3, replication_factor=1)