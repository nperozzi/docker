FROM python:3.12-slim

WORKDIR /app

COPY subscriber.py .
RUN pip install paho-mqtt

CMD ["python", "subscriber.py"]