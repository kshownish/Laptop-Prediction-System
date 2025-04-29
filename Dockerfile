FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python3 train_model.py

EXPOSE 5000

CMD ["python3", "app.py"]