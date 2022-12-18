FROM python

WORKDIR /usr/src/app/trapper_worker
ENV PYTHONPATH=/usr/src/app/

COPY trapper_worker/*.py ./
COPY trapper_worker/cloud_adapter ./cloud_adapter
COPY trapper_worker/config_client ./config_client
COPY trapper_worker/rest_api_client ./rest_api_client
CMD ["python", "-u","/usr/src/app/trapper_worker/main.py"]
