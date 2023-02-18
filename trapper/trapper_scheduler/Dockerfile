FROM --platform=linux/amd64 python

WORKDIR /usr/src/app/trapper_scheduler
ENV PYTHONPATH=/usr/src/app/

COPY trapper_scheduler/*.py ./

CMD ["python", "-u","/usr/src/app/trapper_scheduler/main.py"]
