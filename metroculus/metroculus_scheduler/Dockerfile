FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/metroculus_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY metroculus_scheduler/*.py ./

CMD ["python", "-u","/usr/src/app/metroculus_scheduler/main.py"]
