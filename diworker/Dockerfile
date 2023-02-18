FROM --platform=linux/amd64 python
WORKDIR /usr/src/app/
ENV PYTHONPATH=/usr/src/app/

COPY requirements.txt .
COPY diworker diworker

CMD ["python", "-u","/usr/src/app/diworker/main.py"]
