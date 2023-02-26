FROM --platform=linux/amd64 optscale-python:latest

WORKDIR /usr/src/app/metroculus_worker
ENV PYTHONPATH=/usr/src/app/
RUN pip install clickhouse-migrator==1.0.2
COPY metroculus_worker/*.py ./
COPY metroculus_worker/migrations migrations

CMD ["python", "-u","/usr/src/app/metroculus_worker/main.py"]
