#!/bin/sh

# Ждем, пока база данных будет готова
echo "Waiting for database..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 0.1
done
echo "Database is ready!"

# Применяем миграции
python manage.py migrate

# Запускаем сервер
python manage.py runserver 0.0.0.0:8000