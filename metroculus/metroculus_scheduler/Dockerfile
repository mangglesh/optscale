FROM python

WORKDIR /usr/src/app/metroculus_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY metroculus_scheduler/*.py ./
COPY config_client ./config_client
COPY rest_api_client ./rest_api_client

CMD ["python", "-u","/usr/src/app/metroculus_scheduler/main.py"]
