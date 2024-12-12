FROM python:3.9-slim

WORKDIR /app

COPY producer.py /app/

RUN pip install requests

CMD ["python", "producer.py"]
