from decimal import Decimal

from flask import Flask

from abhishek import create_app
from abhishek.config import TestingConfig
from abhishek.extensions import db
from abhishek.models import Product


def test_create_app_returns_flask_instance() -> None:
    app = create_app(TestingConfig)

    assert isinstance(app, Flask)


def test_health_endpoint_returns_ok() -> None:
    app = create_app(TestingConfig)
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_product_detail_page_returns_product() -> None:
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
            product_id = product.id

            client = app.test_client()
            response = client.get(f"/products/{product_id}")

            assert response.status_code == 200
            assert b"Test Laptop" in response.data
            assert b"Laptop for testing" in response.data
            assert b"55000.00" in response.data
        finally:
            db.session.remove()
            db.drop_all()


def test_product_detail_page_returns_404_for_missing_product() -> None:
    app = create_app(TestingConfig)

    with app.app_context():
        db.create_all()
        try:
            client = app.test_client()
            response = client.get("/products/9999")

            assert response.status_code == 404
        finally:
            db.session.remove()
            db.drop_all()
