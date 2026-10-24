import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///abhishek_shop.db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False
    DEBUG = False

    @classmethod
    def validate(cls) -> None:
        if not cls.SECRET_KEY:
            raise RuntimeError(
                "SECRET_KEY is not configured. Set the SECRET_KEY environment variable."
            )


class TestingConfig(Config):
    SECRET_KEY = "test-secret-key"  # noqa: S105
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
