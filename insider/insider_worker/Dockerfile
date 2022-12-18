FROM python

WORKDIR /usr/src/app/insider_worker
ENV PYTHONPATH=/usr/src/app/

COPY insider_worker/*.py ./
COPY insider_worker/migrations migrations
COPY insider_worker/processors processors
COPY insider_worker/http_client http_client
COPY insider_worker/config_client config_client

CMD ["python", "-u","/usr/src/app/insider_worker/main.py"]
