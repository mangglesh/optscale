FROM python
WORKDIR /src

COPY scheduler.py worker.py ./
COPY rest_api_client ./rest_api_client
COPY config_client ./config_client

CMD ["python3", "/src/scheduler.py"]
