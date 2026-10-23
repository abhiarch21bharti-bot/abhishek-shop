# Abhishek Shop

A modular shopping web application built with Flask and SQLAlchemy. This project emphasizes clean architecture, database migrations, automated testing, and maintainable Python code.

## Features

- Product listing page
- Individual product detail pages
- SQLAlchemy models for users and products
- Database migrations using Alembic
- CLI command to seed sample products
- Health-check endpoint
- Automated tests using pytest
- Code quality checks using Ruff and mypy
- Pre-commit hooks for development consistency

## Tech Stack

- **Language:** Python 3.14
- **Web framework:** Flask
- **Database layer:** Flask-SQLAlchemy and SQLAlchemy
- **Database migrations:** Alembic
- **Testing:** pytest and pytest-cov
- **Code quality:** Ruff and mypy
- **Git hooks:** pre-commit

## Project Structure

```text
abhishek-shop/
├── migrations/                 # Database migration scripts
├── src/
│   └── abhishek/
│       ├── static/
│       │   └── css/
│       ├── templates/
│       ├── __init__.py         # Application factory
│       ├── commands.py         # Flask CLI commands
│       ├── config.py           # Application configuration
│       ├── extensions.py       # Flask extensions
│       ├── models.py            # Database models
│       └── routes.py            # Application routes
├── tests/                      # Automated tests
├── alembic.ini                 # Alembic configuration
├── pyproject.toml              # Project and tool configuration
├── requirements.txt            # Runtime dependencies
├── requirements-dev.txt        # Development dependencies
├── pre-commit-config.yaml      # Pre-commit configuration
├── .editorconfig
├── .gitattributes
├── .gitignore
└── README.md
```

## Prerequisites

- Python 3.14
- Git
- Python virtual environment support

## Getting Started

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd abhishek-shop
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the URL of your GitHub repository.

### 2. Create a virtual environment

On Linux:

```bash
python3.14 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pip install -e .
```

### 4. Configure the application

Set a secret key for the application:

```bash
export SECRET_KEY="replace-with-a-random-secret"
```

The application uses SQLite by default. You can configure a different database using the `DATABASE_URL` environment variable.

Do not commit real secrets or local environment files to version control.

### 5. Initialize the database

Database migrations are managed using Alembic. Use the repository's Alembic configuration and migration scripts to initialize the database.

Before running migrations, verify the configured database URL and follow the migration instructions appropriate to the environment.

### 6. Seed sample products

Once the database schema has been initialized, run:

```bash
flask --app abhishek:create_app seed
```

The seed command adds sample products without duplicating products that already exist with the same names.

### 7. Run the application

```bash
flask --app abhishek:create_app run
```

Open the application in your browser at:

`http://127.0.0.1:5000`

The health-check endpoint is available at:

`http://127.0.0.1:5000/health`

## Running Tests

Run the test suite:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=abhishek --cov-report=term-missing
```

## Code Quality

Run Ruff lint checks:

```bash
ruff check .
```

Check code formatting:

```bash
ruff format --check .
```

Run mypy:

```bash
mypy
```

Run all configured pre-commit hooks:

```bash
pre-commit run --all-files
```

## Configuration

The application supports the following environment variables:

| Variable | Purpose |
|---|---|
| `SECRET_KEY` | Secret key required by the application |
| `DATABASE_URL` | Database connection URL; SQLite is used by default |

Keep credentials and other sensitive configuration out of source control.

## Development Roadmap

Potential future improvements include:

- Product images
- User authentication
- Shopping cart and checkout
- Additional product management features
- Continuous integration with GitHub Actions

## License

See the repository's `LICENSE` file for licensing information.
