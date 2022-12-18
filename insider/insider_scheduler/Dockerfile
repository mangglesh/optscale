FROM python

WORKDIR /usr/src/app/insider_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY insider_scheduler/*.py ./
COPY insider_scheduler/config_client ./config_client

CMD ["python", "-u","/usr/src/app/insider_scheduler/main.py"]
