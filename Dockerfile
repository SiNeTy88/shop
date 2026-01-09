FROM python:3.13-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# 3. Створюємо робочу папку всередині контейнера
WORKDIR /app

# 4. Копіюємо файл з вимогами і встановлюємо бібліотеки
# Ми робимо це ДО копіювання всього коду, щоб Docker закешував цей крок
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# 5. Копіюємо весь наш код у папку /app
COPY . .

# 6. За замовчуванням (якщо не вказано інше) запускаємо сервер
# Але в docker-compose ми це перевизначимо
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]