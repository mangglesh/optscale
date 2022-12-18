FROM python

WORKDIR /usr/src/app/metroculus_worker
ENV PYTHONPATH=/usr/src/app/
RUN pip install clickhouse-migrator==1.0.2
COPY metroculus_worker/*.py ./
COPY metroculus_worker/migrations migrations
COPY config_client ./config_client
COPY rest_api_client ./rest_api_client
COPY cloud_adapter ./cloud_adapter

CMD ["python", "-u","/usr/src/app/metroculus_worker/main.py"]
