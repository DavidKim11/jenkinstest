
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY ./*.* .

#RUN pip install uvicorn
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#uvicorn api:app --reload --host 0.0.0.0 --port 8000 --ssl-keyfile=key.pem --ssl-certfile=cert.pem

ENTRYPOINT ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "7000", "--ssl-keyfile", "key.pem", "--ssl-certfile", "cert.pem"]