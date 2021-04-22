FROM python:3.9-slim

WORKDIR /app
COPY write_data.py .

CMD python /app/write_data.py
