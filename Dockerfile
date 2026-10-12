FROM python:3.14.8-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

COPY requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt \
    && useradd --create-home --uid 10001 app

COPY server.py index.html .python-version ./
USER app
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s \
    CMD python -c "from urllib.request import urlopen; import os; urlopen('http://127.0.0.1:' + os.environ.get('PORT', '8080') + '/health', timeout=3)" || exit 1

CMD ["python", "server.py"]
