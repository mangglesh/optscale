FROM --platform=linux/amd64 optscale-python:latest

WORKDIR /usr/src/app/metroculus_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY metroculus_scheduler/*.py ./

CMD ["python", "-u","/usr/src/app/metroculus_scheduler/main.py"]
