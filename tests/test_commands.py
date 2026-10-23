from abhishek import create_app
from abhishek.config import TestingConfig
from abhishek.extensions import db
from abhishek.models import Product


def test_seed_command_adds_sample_products() -> None:
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()
        try:
            runner = app.test_cli_runner()
            result = runner.invoke(args=["seed"])

            assert result.exit_code == 0
            assert "Added 3 new product(s)." in result.output
            assert db.session.query(Product).count() == 3
        finally:
            db.session.remove()
            db.drop_all()


def test_seed_command_does_not_add_duplicates() -> None:
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()
        try:
            runner = app.test_cli_runner()

            first_result = runner.invoke(args=["seed"])
            second_result = runner.invoke(args=["seed"])

            assert first_result.exit_code == 0
            assert second_result.exit_code == 0
            assert "Added 0 new product(s)." in second_result.output
            assert db.session.query(Product).count() == 3
        finally:
            db.session.remove()
            db.drop_all()
