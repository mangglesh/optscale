FROM --platform=linux/amd64 python

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
COPY rest_api_server/google_calendar_client ./google_calendar_client

RUN python -u write_spec.py
CMD ["python", "-u","/usr/src/app/rest_api_server/server.py"]
EXPOSE 8999
