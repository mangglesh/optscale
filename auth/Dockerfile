FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/auth_server
ENV PYTHONPATH /usr/src/app/

COPY auth_server/alembic ./alembic
COPY auth_server/controllers ./controllers
COPY auth_server/handlers ./handlers
COPY auth_server/auth_token ./auth_token
COPY auth_server/models ./models
COPY auth_server/*.py ./
COPY auth_server/alembic.template .
COPY auth_server/swagger ./swagger
COPY auth_server/zoho_integrator ./zoho_integrator

RUN python -u write_spec.py

CMD ["python", "-u","/usr/src/app/auth_server/server.py"]
EXPOSE 8905
