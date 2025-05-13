import time
import json
from faker import Faker
from kafka import KafkaProducer
import uuid
import random

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'test-topic'

def generate_data():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'address': fake.address(),
        'timestamp': fake.iso8601(),
        "country": fake.country(),
        "currency": random.choice(["USD", "EUR", "GBP", "JPY", "AUD"]),
        "value": round(random.uniform(10.0, 5000.0), 2),
        "item_description": fake.bs(),
        "transaction_id": str(fake.uuid4())
    }

if __name__ == '__main__':
    while True:
        data = generate_data()
        producer.send(topic, value=data)
        time.sleep(1)
