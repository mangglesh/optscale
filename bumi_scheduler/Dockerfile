FROM --platform=linux/amd64 python

ENV PYTHONPATH /usr/src/app/
WORKDIR /usr/src/app/bumi_scheduler
COPY bumi_scheduler/controllers ./controllers
COPY bumi_scheduler/*.py ./

CMD ["python", "-u","/usr/src/app/bumi_scheduler/main.py"]
