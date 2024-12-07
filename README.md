# Email Sender Django App

Сервис рассылки электронных писем, построенный с использованием Django и Django REST Framework.

## Технологии

-   Python 3.12
-   Django 5.1.4
-   Django REST Framework 3.15.2
-   PostgreSQL 15
-   Docker & Docker Compose
-   SMTP

## Установка и Запуск

### Предварительные требования

-   Docker
-   Docker Compose

### Настройка окружения

1. Клонируйте репозиторий:

```bash
git clone https://github.com/w1sq/email_sender_django_app
cd email_sender_django_app
```

2. Создайте файл `.env` в корневой директории проекта по примеру `.env.example`:

### Запуск проекта

1. Запустите контейнеры:

```bash
docker-compose up --build
```

2. Создайте суперпользователя:

```bash
docker-compose exec web python manage.py createsuperuser
```

3. Примените миграции:

```bash
docker-compose exec web python manage.py migrate
```

Приложение будет доступно по адресу: `http://localhost:8000`

## API Endpoints

### Аутентификация

-   Используется базовая аутентификация Django
-   Доступ к API требует аутентификации

### Рассылка писем

-   `GET /api/mailing/send/<id>/` - Отправить рассылку

## Административный интерфейс

Доступен по адресу: `http://localhost:8000/admin/`

### Функциональность админ-панели

-   Управление пользователями
-   Создание и редактирование рассылок
-   Мониторинг статуса отправки

## Разработка

### Структура проекта

```
email_sender_django_app/
├── config/             # Настройки проекта
├── users/             # Приложение пользователей
├── mailing/           # Приложение рассылок
├── requirements.txt   # Зависимости Python
├── Dockerfile        # Конфигурация Docker
├── docker-compose.yml # Конфигурация Docker Compose
├── .env              # Переменные окружения
└── entrypoint.sh     # Скрипт для запуска проекта
```

## Безопасность

-   Все секретные данные хранятся в переменных окружения
-   Используется TLS для SMTP-соединения
-   Реализована базовая аутентификация для API
