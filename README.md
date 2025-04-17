# Items Exchange

API-driven platform for users to create, browse, and exchange classified ads. Built with Django, Django REST Framework, Django Filter, and drf-yasg for interactive API documentation.

---

## Features

- User authentication and ad ownership
- CRUD operations on Ads via RESTful endpoints
- Search by title/description, filter by category and condition
- Pagination and ordering
- Exchange proposals between users (with status flow)
- Interactive Swagger UI documentation (`/docs/`)
- Environment-based configuration with `.env`
- Test suite powered by pytest and pytest-django

---

## Prerequisites

- Python 3.12
- [Poetry](https://python-poetry.org/) for dependency management

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/items_exchange.git
   cd items_exchange
   ```

2. **Configure Poetry** (in-project virtualenv)

   ```bash
   poetry config virtualenvs.in-project true --local
   poetry install
   ```

3. **Create a `.env` file** at project root:

   ```ini
   # .env
   DJANGO_SECRET_KEY=your-secret-key
   DJANGO_DEBUG=True
   DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

   # Database (SQLite default)
   DB_ENGINE=django.db.backends.sqlite3
   DB_NAME=db.sqlite3

   # (Optional) PostgreSQL example:
   # DB_ENGINE=django.db.backends.postgresql
   # DB_NAME=mydb
   # DB_USER=myuser
   # DB_PASSWORD=mypass
   # DB_HOST=localhost
   # DB_PORT=5432
   ```

4. **Apply migrations**

   ```bash
   poetry run python manage.py migrate
   ```

---

## Running the Development Server

```bash
poetry run python manage.py runserver
```

- Browse the site at `http://127.0.0.1:8000/`
- API root lives under `/api/`

---

## API Documentation (Swagger)

Navigate to:

```
http://127.0.0.1:8000/docs/
```

Use the interactive UI to explore endpoints, parameters, and try out calls.

---

## Running Tests

```bash
poetry run pytest
```

This will run all unit and integration tests with a temporary test database.

---

## Linting & Formatting

- **Ruff** for linting: `poetry run ruff .`
- Configure your editor to respect `pyproject.toml` and `ruff.toml` rules.

---

## Environment Settings

`settings.py` reads from environment variables via `python-dotenv`. Key settings include:

- **`DJANGO_SECRET_KEY`**: cryptographic key for Django
- **`DJANGO_DEBUG`**: enable/disable debug mode
- **`DJANGO_ALLOWED_HOSTS`**: comma-separated hosts
- **`DB_*`**: database engine and credentials

---

## Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -am "Add feature"`)
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

---

## License

This project is MIT licensed. See [LICENSE](LICENSE) for details.
