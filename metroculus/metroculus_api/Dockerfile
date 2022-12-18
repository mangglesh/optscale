FROM python

WORKDIR /usr/src/app/metroculus_api
ENV PYTHONPATH /usr/src/app/

COPY metroculus_api/controllers ./controllers
COPY metroculus_api/handlers ./handlers
COPY metroculus_api/swagger ./swagger
COPY metroculus_api/*.py ./
COPY config_client ./config_client
COPY rest_api_client ./rest_api_client
COPY cloud_adapter ./cloud_adapter
COPY optscale_exceptions ./optscale_exceptions
RUN python -u write_spec.py

CMD ["python", "-u","/usr/src/app/metroculus_api/server.py"]
EXPOSE 8969
