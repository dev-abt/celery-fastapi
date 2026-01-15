from python:3.10-slim

workdir /app

copy requirements.txt .

run pip install -r requirements.txt

copy . .

cmd ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]