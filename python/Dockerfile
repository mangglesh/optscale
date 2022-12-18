FROM python:3.8-slim
COPY requirements.txt ./requirements.txt

RUN apt-get update && apt-get install -y libsodium-dev \
    && pip install --use-deprecated=legacy-resolver --no-cache-dir -r requirements.txt \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
