#!/bin/bash

# Aguardar o Kafka estar pronto
echo "Aguardando Kafka..."
sleep 10

# Criar o tópico test-topic
kafka-topics --create --if-not-exists --topic test-topic \
  --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1

# Listar tópicos para verificação
kafka-topics --list --bootstrap-server kafka:9092
