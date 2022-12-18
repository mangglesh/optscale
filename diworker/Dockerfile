FROM python
WORKDIR /src
ENV PYTHONPATH=/src

COPY requirements.txt .
COPY diworker diworker

CMD ["python", "-u","/src/diworker/main.py"]
