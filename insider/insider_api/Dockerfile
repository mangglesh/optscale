FROM python

WORKDIR /usr/src/app/insider_api
ENV PYTHONPATH /usr/src/app/


COPY insider_api/controllers ./controllers
COPY insider_api/handlers ./handlers
COPY insider_api/swagger ./swagger
COPY insider_api/*.py ./

COPY insider_api/cloud_adapter ./cloud_adapter
COPY insider_api/config_client ./config_client
COPY insider_api/optscale_exceptions ./optscale_exceptions
RUN python -u write_spec.py

CMD ["python", "-u","/usr/src/app/insider_api/server.py"]
EXPOSE 8945
