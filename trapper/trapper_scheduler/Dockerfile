FROM python

WORKDIR /usr/src/app/trapper_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY trapper_scheduler/*.py ./
COPY trapper_scheduler/config_client ./config_client
COPY trapper_scheduler/rest_api_client ./rest_api_client

CMD ["python", "-u","/usr/src/app/trapper_scheduler/main.py"]
