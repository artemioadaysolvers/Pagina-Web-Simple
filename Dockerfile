
FROM python:3.14.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY index.html server.py ./

ENV PORT=8080

EXPOSE 8080

CMD ["python", "server.py"]
