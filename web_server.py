from flask import Flask, render_template
from flask_socketio import SocketIO
from kafka import KafkaConsumer
import json
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

def consume_kafka():
    consumer = KafkaConsumer(
        'network-traffic',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    for message in consumer:
        socketio.emit('traffic_data', message.value)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    t = threading.Thread(target=consume_kafka)
    t.daemon = True
    t.start()
    socketio.run(app, host='0.0.0.0', port=5000)
