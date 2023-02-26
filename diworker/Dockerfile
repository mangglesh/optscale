FROM --platform=linux/amd64 optscale-python:latest
WORKDIR /usr/src/app/
ENV PYTHONPATH=/usr/src/app/

COPY requirements.txt .
COPY diworker diworker

CMD ["python", "-u","/usr/src/app/diworker/main.py"]
