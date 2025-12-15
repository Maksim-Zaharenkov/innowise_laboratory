FROM python:3.13.7

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python main.py & python lecture_5/book_api/main.py"]