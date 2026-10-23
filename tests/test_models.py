from decimal import Decimal

from abhishek import create_app
from abhishek.config import TestingConfig
from abhishek.extensions import db
from abhishek.models import Product, User


def test_product_can_be_saved_to_database() -> None:
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()
        try:
            product = Product(
                name="Test Laptop",
                description="Laptop for testing",
                price=Decimal("55000.00"),
            )
            db.session.add(product)
            db.session.commit()

            saved_product = db.session.get(Product, product.id)

            assert saved_product is not None
            assert saved_product.name == "Test Laptop"
            assert saved_product.price == Decimal("55000.00")
        finally:
            db.session.remove()
            db.drop_all()


def test_user_can_be_saved_to_database() -> None:
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()
        try:
            user = User(
                username="testuser",
                email="test@example.com",
                password_hash="test-password-hash",
            )
            db.session.add(user)
            db.session.commit()

            saved_user = db.session.get(User, user.id)

            assert saved_user is not None
            assert saved_user.username == "testuser"
            assert saved_user.email == "test@example.com"
        finally:
            db.session.remove()
            db.drop_all()
