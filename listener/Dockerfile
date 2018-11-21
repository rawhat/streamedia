FROM python:latest

WORKDIR /opt/app

COPY ../requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "listener.py"]