FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/metroculus_api
ENV PYTHONPATH /usr/src/app/

COPY metroculus_api/controllers ./controllers
COPY metroculus_api/handlers ./handlers
COPY metroculus_api/swagger ./swagger
COPY metroculus_api/*.py ./
RUN python -u write_spec.py

CMD ["python", "-u","/usr/src/app/metroculus_api/server.py"]
EXPOSE 8969
