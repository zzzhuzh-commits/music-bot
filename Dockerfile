FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg git

COPY requirements.txt .

RUN pip install --no-cache-dir py-tgcalls

COPY . .

CMD ["python", "main.py"]
