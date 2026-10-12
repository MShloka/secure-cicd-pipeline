FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt \
    && python -m pip install --no-cache-dir --upgrade \
        "msgpack>=1.2.1" \
        "setuptools>=78.1.1" \
        "urllib3>=2.8.0"

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]