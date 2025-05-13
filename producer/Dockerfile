FROM python:3.11-slim

WORKDIR /app

# Instala dependências do sistema (netcat para wait-for-it.sh)
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Copia os arquivos do projeto
COPY . .

# Instala dependências Python
RUN pip install --no-cache-dir faker==20.1.0 kafka-python==2.0.2

# Garante que wait-for-it.sh tenha permissões de execução
RUN chmod +x wait-for-it.sh

# O CMD é sobrescrito pelo entrypoint no docker-compose.yml
CMD ["python", "producer.py"]