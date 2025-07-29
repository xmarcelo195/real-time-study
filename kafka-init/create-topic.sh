#!/bin/bash

# Wait for Kafka to be ready
until nc -z kafka 9092; do
  echo "Waiting for Kafka..."
  sleep 20
done

# Create Topic
kafka-topics --create -if-not-exists --topic btc --bootstrap-server kafka:9092 --partitions 10 --replication-factor 1
