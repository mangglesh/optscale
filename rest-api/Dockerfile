FROM python

WORKDIR /usr/src/app/rest_api_server
ENV PYTHONPATH /usr/src/app/
#COPY live_demo.json ./
COPY rest_api_server/alembic ./alembic
COPY rest_api_server/controllers ./controllers
COPY rest_api_server/handlers ./handlers
COPY rest_api_server/models ./models
COPY rest_api_server/*.py ./
COPY rest_api_server/alembic.template .
COPY rest_api_server/swagger ./swagger
COPY rest_api_server/auth_client ./auth_client
COPY rest_api_server/google_calendar_client ./google_calendar_client
COPY rest_api_server/config_client ./config_client
COPY rest_api_server/cloud_adapter ./cloud_adapter
COPY rest_api_server/herald_client ./herald_client
COPY rest_api_server/katara_client ./katara_client
COPY rest_api_server/metroculus_client ./metroculus_client
COPY rest_api_server/optscale_exceptions ./optscale_exceptions

#COPY rest_api_server/recommendation_cleanup_scripts ./recommendation_cleanup_scripts
#RUN python -u write_spec.py

CMD ["python", "-u","/usr/src/app/rest_api_server/server.py"]
EXPOSE 8999
