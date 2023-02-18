FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/insider_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY insider_scheduler/*.py ./

CMD ["python", "-u","/usr/src/app/insider_scheduler/main.py"]
