FROM python:3.11-alpine

WORKDIR /app

COPY geometric_lib/*.py ./

COPY script.py .

RUN chmod +x script.py

ENTRYPOINT ["python", "/app/script.py"]

