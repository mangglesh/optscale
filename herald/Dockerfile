FROM python

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
COPY auth_client ../auth_client
COPY config_client ../config_client
COPY optscale_exceptions ../optscale_exceptions
COPY optscale_types ../optscale_types

CMD ["python", "-u", "run.py"]
EXPOSE 8906
