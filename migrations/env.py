from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

import abhishek.models  # noqa: F401
from abhishek import create_app
from abhishek.extensions import db

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Tell Alembic about our Flask-SQLAlchemy models.
target_metadata = db.metadata

# Use the same database URL as the Flask application.
# database_url = Config.SQLALCHEMY_DATABASE_URI
# config.set_main_option("sqlalchemy.url", database_url)

app = create_app()

with app.app_context():
    database_url = db.engine.url.render_as_string(hide_password=False)

config.set_main_option("sqlalchemy.url", database_url)


def run_migrations_offline() -> None:
    """Run migrations without creating a database connection."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations using a live database connection."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
