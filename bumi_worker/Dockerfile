FROM --platform=linux/amd64 optscale-python:latest

WORKDIR /usr/src/app/bumi_worker
ENV PYTHONPATH /usr/src/app/

COPY bumi_worker/modules ./modules
COPY bumi_worker/*.py ./

CMD ["python", "-u","/usr/src/app/bumi_worker/main.py"]
