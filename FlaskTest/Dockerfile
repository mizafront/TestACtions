# Базовый образ с Python
FROM python:3.10

# Установка зависимостей
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# Копирование приложения в образ
COPY flaskapp /app

# Запуск приложения
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
