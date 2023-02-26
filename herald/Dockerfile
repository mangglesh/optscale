FROM --platform=linux/amd64 optscale-python:latest

WORKDIR /usr/src/app/herald_server

ENV PYTHONPATH /usr/src/app/

COPY herald_server/alembic ./alembic
COPY herald_server/controllers ./controllers
COPY herald_server/handlers ./handlers
COPY herald_server/processors ./processors
COPY herald_server/models ./models
COPY herald_server/worker ./worker
COPY herald_server/*.py run.py ./
COPY herald_server/alembic.template .
COPY modules ../modules

CMD ["python", "-u", "run.py"]
EXPOSE 8906
