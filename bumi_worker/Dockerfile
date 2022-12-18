FROM python

WORKDIR /usr/src/app/bumi_worker
ENV PYTHONPATH /usr/src/app/

COPY bumi_worker/modules ./modules
COPY bumi_worker/*.py ./
COPY cloud_adapter cloud_adapter/
COPY config_client config_client/
COPY herald_client herald_client/
COPY rest_api_client rest_api_client/
COPY insider_client insider_client/
COPY metroculus_client metroculus_client/

CMD ["python", "-u","/usr/src/app/bumi_worker/main.py"]
