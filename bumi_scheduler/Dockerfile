FROM python

WORKDIR /usr/src/app/bumi_scheduler
COPY bumi_scheduler/controllers ./controllers
COPY bumi_scheduler/*.py ./
COPY config_client ./config_client
COPY rest_api_client ./rest_api_client

CMD ["python", "-u","/usr/src/app/bumi_scheduler/main.py"]
