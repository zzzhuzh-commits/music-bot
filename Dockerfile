FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y ffmpeg git

COPY requirements.txt .

RUN pip install pyrogram tgcrypto python-dotenv py-tgcalls

COPY . .

CMD ["python", "main.py"]
