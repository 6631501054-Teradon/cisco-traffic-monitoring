import time
import json
import psutil
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("Starting Traffic Collector...")
while True:
    net_io = psutil.net_io_counters()
    data = {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'timestamp': time.time()
    }
    producer.send('network-traffic', data)
    time.sleep(2)
