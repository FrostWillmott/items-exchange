# Обмен Объявлениями

Платформа с API для создания, просмотра и обмена объявлениями. Построена с использованием Django, Django REST Framework, django-filter и drf-yasg для интерактивной документации.

---

## Возможности

- Аутентификация пользователей и владение объявлениями
- CRUD-операции над объявлениями через REST API
- Поиск по заголовку/описанию, фильтрация по категории и состоянию
- Пагинация и сортировка
- Предложения обмена между пользователями (с изменением статуса)
- Интерактивная документация Swagger UI (`/docs/`)
- Конфигурация через файл окружения `.env`
- Набор тестов на базе pytest и pytest-django

---

## Требования

- Python 3.12
- [Poetry](https://python-poetry.org/) для управления зависимостями

---

## Установка

1. **Склонируйте репозиторий**

   ```bash
   git clone https://github.com/FrostWillmott/items_exchange.git
   cd items_exchange
   ```

2. **Настройте Poetry** (виртуальное окружение в проекте)

   ```bash
   poetry config virtualenvs.in-project true --local
   poetry install
   ```

3. **Создайте файл `.env`** в корне проекта:

   ```ini
   # .env
   DJANGO_SECRET_KEY=ваш-секретный-ключ
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

   # Настройки базы данных (по умолчанию SQLite)
   DB_ENGINE=django.db.backends.sqlite3
   DB_NAME=db.sqlite3

   # (Опционально) Пример для PostgreSQL:
   # DB_ENGINE=django.db.backends.postgresql
   # DB_NAME=mydb
   # DB_USER=myuser
   # DB_PASSWORD=mypass
   # DB_HOST=localhost
   # DB_PORT=5432
   ```

4. **Примените миграции**

   ```bash
   poetry run python manage.py migrate
   ```

---

## Запуск сервера разработки

```bash
poetry run python manage.py runserver
```

- Откройте в браузере: `http://127.0.0.1:8000/`
- Корневой API доступен по пути `/api/`
- Внимание: встроенный сервер разработки предназначен только для локальной разработке и не подходит для продакшена.
Для развёртывания в продакшен используйте WSGI/ASGI серверы (Gunicorn, uWSGI, Daphne и т.д.).
Подробнее: https://docs.djangoproject.com/en/5.2/howto/deployment/
---

## Документация API (Swagger)

Перейдите по адресу:

```
http://127.0.0.1:8000/docs/
```

Используйте интерактивный интерфейс для изучения эндпоинтов, параметров и пробных запросов.

---

## Запуск тестов

```bash
poetry run pytest
```

Это запустит все модульные и интеграционные тесты с использованием временной тестовой базы.

---

## Линтинг и форматирование

- **Ruff** для статического анализа: `poetry run ruff .`
- Настройте редактор, чтобы он использовал правила из `pyproject.toml` и `ruff.toml`.

---

## Переменные окружения

`settings.py` загружает настройки из переменных окружения через `python-dotenv`. Основные переменные:

- **`DJANGO_SECRET_KEY`**: секретный ключ Django
- **`DJANGO_DEBUG`**: включение/отключение режима отладки
- **`DJANGO_ALLOWED_HOSTS`**: список разрешённых хостов через запятую
- **`DB_*`**: параметры подключения к базе данных

---


## Лицензия

Этот проект лицензирован под MIT. Подробнее в файле [LICENSE](LICENSE).
