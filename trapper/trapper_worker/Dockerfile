FROM --platform=linux/amd64 optscale-python:latest

WORKDIR /usr/src/app/trapper_worker
ENV PYTHONPATH=/usr/src/app/

COPY trapper_worker/*.py ./
CMD ["python", "-u","/usr/src/app/trapper_worker/main.py"]
