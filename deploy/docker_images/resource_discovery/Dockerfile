FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/
ENV PYTHONPATH=/usr/src/app/

COPY scheduler.py worker.py ./
CMD ["python", "-u", "/usr/src/app/scheduler.py"]
